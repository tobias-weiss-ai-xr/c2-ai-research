#!/usr/bin/env python3
"""Multi-source fetcher for thin categories — wargaming, C2 reviews, etc.

Sources: DBLP, CrossRef, Europe PMC. Uses session-based retry and longer
pauses between queries.

Usage:
    python3 scripts/fetch/fetch_other_sources.py
    python3 scripts/fetch/fetch_other_sources.py --dry-run
"""

import argparse
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_new_papers import (  # noqa: E402
    ARXIV_ID_PATTERN,
    classify_subcategory,
    load_existing_papers,
)

BASE = Path(__file__).resolve().parent.parent.parent

ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})")

# Queries: (source, query_string, category, subcategory_hint)
# Broader single-term queries to maximize recall.
QUERIES = [
    # --- Wargaming (DBLP: 53 results for bare "wargaming") ---
    ("dblp", "wargaming", "wargaming", "application"),
    ("dblp", "wargaming reinforcement learning", "wargaming", "method"),
    ("dblp", "wargaming multi-agent", "wargaming", "application"),
    ("dblp", "wargaming deep learning", "wargaming", "method"),
    ("dblp", "wargaming game theory", "wargaming", "theory"),
    ("dblp", "wargaming simulation", "wargaming", "systems"),
    ("dblp", "wargaming machine learning", "wargaming", "method"),
    ("dblp", "wargaming agent", "wargaming", "application"),
    ("dblp", "wargame reinforcement learning", "wargaming", "method"),
    ("dblp", "wargame agent", "wargaming", "application"),
    ("dblp", "wargame artificial intelligence", "wargaming", "review"),
    ("dblp", "wargaming neural network", "wargaming", "method"),
    ("dblp", "wargaming LLM", "wargaming", "development"),
    ("dblp", "wargaming survey", "wargaming", "review"),
    # --- Wargaming (CrossRef) ---
    ("crossref", "wargaming reinforcement learning", "wargaming", "method"),
    ("crossref", "wargaming deep learning", "wargaming", "method"),
    ("crossref", "wargaming multi-agent", "wargaming", "application"),
    ("crossref", "wargaming autonomous", "wargaming", "application"),
    ("crossref", "wargame artificial intelligence", "wargaming", "review"),
    ("crossref", "wargaming survey review", "wargaming", "review"),
    # --- Wargaming (Europe PMC) ---
    ("europepmc", "wargaming AI", "wargaming", "application"),
    ("europepmc", "wargaming reinforcement", "wargaming", "method"),
    # --- C2 reviews/evaluations ---
    ("dblp", "command control survey", "command-and-control", "review"),
    ("dblp", "command control benchmark evaluation", "command-and-control", "evaluation"),
    ("dblp", "battle management autonomous", "command-and-control", "systems"),
    ("dblp", "situation awareness AI", "command-and-control", "mechanism"),
    ("dblp", "command control framework", "command-and-control", "development"),
    # --- Opponent modeling reviews ---
    ("dblp", "opponent modeling survey", "opponent-modeling", "review"),
    ("crossref", "opponent modeling survey review", "opponent-modeling", "review"),
]

# Create persistent sessions
session = requests.Session()
session.headers.update({"User-Agent": "C2-AI-Research/1.0 (mailto:research@tobias-weiss-ai-xr.de)"})


def fetch_with_retry(fn, retries=3, base_wait=15):
    """Call fn() with exponential backoff on failure."""
    for attempt in range(retries):
        try:
            return fn()
        except (requests.ConnectionError, requests.Timeout) as e:
            wait = base_wait * (attempt + 1)
            print(f"    connection error, retry in {wait}s...", flush=True)
            time.sleep(wait)
        except Exception as e:
            print(f"    error: {e}", flush=True)
            return []
    print(f"    gave up after {retries} retries", flush=True)
    return []


def fetch_dblp(query, max_results=20):
    def _do():
        r = session.get(
            "https://dblp.org/search/publ/api",
            params={"q": query, "format": "json", "h": str(max_results)},
            timeout=30,
        )
        r.raise_for_status()
        hits = r.json().get("result", {}).get("hits", {}).get("hit", [])
        results = []
        for h in hits:
            info = h.get("info", {})
            title = info.get("title", "")
            if not title:
                continue
            year = info.get("year", "")
            venue = info.get("venue", "")
            key = info.get("key", "")
            doi = info.get("doi", "")
            url = f"https://dblp.org/rec/{key}" if key else ""
            authors_raw = info.get("authors", {}).get("author", [])
            if isinstance(authors_raw, dict):
                authors_raw = [authors_raw]
            authors = [a.get("@_text", "") for a in authors_raw[:3] if isinstance(a, dict)]
            ee = info.get("ee", [])
            if isinstance(ee, str):
                ee = [ee]
            for e_url in ee:
                if "arxiv" in e_url:
                    url = e_url.replace("http://", "https://")
                    break
            results.append({
                "title": title, "date": f"{year}-01" if year and year.isdigit() else "",
                "url": url, "authors": authors, "abstract": "",
                "venue": venue, "doi": doi,
            })
        return results
    return fetch_with_retry(_do)


def fetch_crossref(query, max_results=10):
    def _do():
        r = session.get(
            "https://api.crossref.org/works",
            params={
                "query": query, "rows": str(max_results),
                "select": "DOI,title,abstract,author,published-print,published-online,container-title,type,URL",
            },
            timeout=30,
        )
        if r.status_code == 429:
            print(f"    CrossRef 429, waiting 20s...", flush=True)
            time.sleep(20)
            return fetch_crossref(query, max_results)
        r.raise_for_status()
        items = r.json().get("message", {}).get("items", [])
        results = []
        for item in items:
            title = (item.get("title") or [""])[0]
            doi = item.get("DOI", "")
            abstract = re.sub(r"<[^>]+>", "", item.get("abstract", "")).strip()
            authors = [
                f'{a.get("given", "")} {a.get("family", "")}'.strip()
                for a in item.get("author", [])[:3]
            ]
            venue = (item.get("container-title") or [""])[0]
            pp = item.get("published-print") or item.get("published-online") or {}
            dp = pp.get("date-parts", [[]])[0] if pp else []
            year = str(dp[0]) if dp else ""
            month = f"{dp[1]:02d}" if len(dp) > 1 else "01"
            url = item.get("URL", "") or f"https://doi.org/{doi}" if doi else ""
            if title:
                results.append({
                    "title": title, "date": f"{year}-{month}" if year.isdigit() else "",
                    "url": url, "authors": authors,
                    "abstract": abstract[:300], "venue": venue, "doi": doi,
                })
        return results
    return fetch_with_retry(_do)


def fetch_europe_pmc(query, max_results=10):
    def _do():
        r = session.get(
            "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
            params={"query": query, "format": "json", "pageSize": str(max_results), "resultType": "core"},
            timeout=30,
        )
        r.raise_for_status()
        results_list = r.json().get("resultList", {}).get("result", [])
        results = []
        for hit in results_list:
            title = hit.get("title", "")
            if not title:
                continue
            year = hit.get("pubYear", "")
            doi = hit.get("doi", "")
            pmcid = hit.get("pmcid", "")
            pmid = hit.get("pmid", "")
            abstract = hit.get("abstractText", "") or ""
            src = hit.get("source", "")
            authors_raw = hit.get("authorList", {}).get("author", [])
            if isinstance(authors_raw, dict):
                authors_raw = [authors_raw]
            authors = [a.get("fullName", a.get("authorName", "")) for a in authors_raw[:3] if isinstance(a, dict)]
            url = f"https://doi.org/{doi}" if doi else f"https://europepmc.org/article/pmc/{pmcid}" if pmcid else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}" if pmid else ""
            results.append({
                "title": title, "date": f"{year}-01" if year and year.isdigit() else "",
                "url": url, "authors": authors,
                "abstract": abstract[:300], "venue": src, "doi": doi,
            })
        return results
    return fetch_with_retry(_do)


FETCHERS = {"dblp": fetch_dblp, "crossref": fetch_crossref, "europepmc": fetch_europe_pmc}


def is_dup(entry, by_id, titles_lower):
    url = entry.get("url", "")
    doi = entry.get("doi", "")
    t = entry.get("title", "").lower().strip()
    m = ARXIV_ID_RE.search(url)
    if m and m.group(1) in by_id:
        return True
    if doi and f"doi:{doi}" in by_id:
        return True
    if url and url in by_id:
        return True
    return any(t == tl for tl in titles_lower)


def main():
    parser = argparse.ArgumentParser(description="Multi-source fetch for thin categories")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--sleep", type=float, default=5.0)
    args = parser.parse_args()

    yaml_path = BASE / "papers.yaml"
    by_id, titles_lower = load_existing_papers(yaml_path)
    # Build extended dedup index
    for key, p in list(by_id.items()):
        doi = p.get("doi", "")
        if doi:
            by_id[f"doi:{doi}"] = p
        by_id[p.get("url", "")] = p

    # Count unique papers by title to get accurate count
    print(f"Loaded {len(titles_lower)} existing papers", flush=True)

    all_new = []
    for qi, (source, query, category, hint) in enumerate(QUERIES):
        fetcher = FETCHERS.get(source)
        if not fetcher:
            continue
        label = f"[{qi+1}/{len(QUERIES)}] {source}/{category}: {query[:50]}"
        print(label, flush=True)
        entries = fetcher(query)
        new = 0
        for e in entries:
            if not e.get("title") or not e.get("url"):
                continue
            if is_dup(e, by_id, titles_lower):
                continue
            e["category"] = category
            e["subcategory"] = classify_subcategory(e["title"], e.get("abstract", ""))
            all_new.append(e)
            doi = e.get("doi", "")
            if doi:
                by_id[f"doi:{doi}"] = e
            by_id[e["url"]] = e
            titles_lower.append(e["title"].lower().strip())
            new += 1
        print(f"  → {new} new (from {len(entries)} results)", flush=True)
        time.sleep(args.sleep)

    print(f"\nTotal new papers: {len(all_new)}", flush=True)
    if args.dry_run:
        for e in all_new[:10]:
            print(f"  [{e['category']}] {e['title'][:80]}")
        if len(all_new) > 10:
            print(f"  ... and {len(all_new)-10} more")
    else:
        append_to_yaml(yaml_path, all_new)
        print(f"Appended to papers.yaml", flush=True)

    from collections import Counter
    cats = Counter(e["category"] for e in all_new)
    for c, n in cats.most_common():
        print(f"  {c}: +{n}")


def append_to_yaml(yaml_path, new_papers):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    papers = data.get("papers", [])
    for e in new_papers:
        entry = {"title": e["title"], "date": e.get("date", ""), "url": e["url"],
                 "category": e["category"], "subcategory": e["subcategory"],
                 "authors": e.get("authors", [])}
        if e.get("abstract"):
            entry["abstract"] = e["abstract"]
        if e.get("doi"):
            entry["doi"] = e["doi"]
        if e.get("venue"):
            entry["venue"] = e["venue"]
        papers.append(entry)
    data["papers"] = papers
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


if __name__ == "__main__":
    main()
