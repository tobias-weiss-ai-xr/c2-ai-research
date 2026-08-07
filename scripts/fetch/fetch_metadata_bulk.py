#!/usr/bin/env python3
"""Bulk-fetch metadata (authors, abstract, venue hint) from arXiv API.

Uses arXiv's id_list batch endpoint (~100 IDs per request) for speed.
Skips papers that already have authors populated.

Adopted & adapted from agent-learning-research corpus tooling.

Usage:
    python3 scripts/fetch/fetch_metadata_bulk.py
    python3 scripts/fetch/fetch_metadata_bulk.py --id ISBN --id 2110.06066
"""

import argparse
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
import yaml

ARXIV_ID_PATTERN = re.compile(r"(\d{4}\.\d{4,5})")
ARXIV_API = "http://export.arxiv.org/api/query"
BATCH_SIZE = 50
API_DELAY = 3


def extract_arxiv_id(url):
    match = ARXIV_ID_PATTERN.search(url)
    return match.group(1) if match else None


def fetch_batch(arxiv_ids):
    results = {}
    id_list = ",".join(arxiv_ids)
    for attempt in range(4):
        try:
            resp = requests.get(ARXIV_API, params={"id_list": id_list, "max_results": len(arxiv_ids)}, timeout=60)
            if resp.status_code == 429:
                wait = 30 * (attempt + 1)
                print(f"    429, waiting {wait}s (attempt {attempt + 1}/4)...", flush=True)
                time.sleep(wait)
                continue
            if resp.status_code == 503:
                print("    503, waiting 60s...", flush=True)
                time.sleep(60)
                continue
            resp.raise_for_status()
            root = ET.fromstring(resp.text)
            ns = {
                "atom": "http://www.w3.org/2005/Atom",
                "arxiv": "http://arxiv.org/schemas/atom",
            }
            for entry in root.findall("atom:entry", ns):
                id_elem = entry.find("atom:id", ns)
                if id_elem is None or not id_elem.text:
                    continue
                m = ARXIV_ID_PATTERN.search(id_elem.text.strip())
                if not m:
                    continue
                aid = m.group(1)
                authors = []
                for author in entry.findall("atom:author", ns):
                    name = author.find("atom:name", ns)
                    if name is not None and name.text:
                        authors.append(name.text.strip())
                # journal_ref is the closest thing to a venue in arXiv metadata
                journal = None
                jref = entry.find("arxjv:journal_ref", ns)
                if jref is not None and jref.text:
                    journal = jref.text.strip()
                # first <link title="..." /> is typically the paper title
                title = None
                t_elem = entry.find("atom:title", ns)
                if t_elem is not None and t_elem.text:
                    title = " ".join(t_elem.text.split())
                results[aid] = {
                    "authors": authors,
                    "title": title or "",
                    "venue": journal or "",
                }
            return results
        except Exception as e:
            print(f"  WARNING: batch error: {e}", flush=True)
            return {}


def enrich(papers, only_ids=None):
    """Enrich papers in-place, returning how many were updated."""
    to_fetch = []
    for p in papers:
        aid = extract_arxiv_id(p.get("url", ""))
        if not aid:
            continue
        if only_ids is not None and p.get("url", "") not in only_ids and aid not in only_ids:
            continue
        if p.get("authors"):
            continue
        to_fetch.append((aid, p))

    updated = 0
    for i in range(0, len(to_fetch), BATCH_SIZE):
        batch = to_fetch[i:i + BATCH_SIZE]
        ids = [aid for aid, _ in batch]
        print(f"Fetching {len(ids)} IDs...", flush=True)
        results = fetch_batch(ids)
        for aid, p in batch:
            meta = results.get(aid)
            if not meta:
                continue
            if not p.get("authors") and meta["authors"]:
                p["authors"] = meta["authors"]
                updated += 1
            if not p.get("title") and meta["title"]:
                p["title"] = meta["title"]
            if meta["venue"] and not p.get("venue"):
                p["venue"] = meta["venue"]
        time.sleep(API_DELAY)
    return updated


def main():
    parser = argparse.ArgumentParser(description="Bulk-fetch arXiv metadata for the corpus")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--id", dest="only_ids", action="append", default=None)
    args = parser.parse_args()

    yaml_path = Path(__file__).resolve().parent.parent.parent / "papers.yaml"
    with open(yaml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    papers = data.get("papers", [])

    only = set(args.only_ids) if args.only_ids else None
    updated = enrich(papers, only_ids=only)

    print(f"\nEnriched {updated} papers ({len(papers)} total)")
    if args.dry_run:
        print("Dry run — not saved")
        return

    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    print("Saved papers.yaml")


if __name__ == "__main__":
    main()