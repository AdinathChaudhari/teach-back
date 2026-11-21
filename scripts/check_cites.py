#!/usr/bin/env python3
"""Check that every `path:line` citation in a page or ledger resolves in the real code.

Usage:
    check_cites.py PAGE [--ledger LEDGER] --root DIR [--root DIR ...]

PAGE     An .html page or a .md ledger. HTML tags are stripped before the scan.
--root   A folder to look in (repeat for several; first match wins). Use the
         snapshot of the code you are teaching, for example the `git archive`
         folder, plus any folder that holds your build log.
--ledger Optional verified markdown ledger. When given, every citation on the
         page must also appear in the ledger (basename match is allowed, and a
         `:NNN` shorthand after a full `path:NNN` counts as the same file).

A citation looks like `src/app/store.py:42` or `src/app/store.py:42-47`.
Known extensions: md py toml json sh yaml jsonl.

Output lines, then a summary `N citations, M bad`:
    BARE          path has no folder, but resolves to exactly one file; use the full path
    MISSING       no root holds that file
    OUT-OF-RANGE  the cited line is past the end of the file
    NOT-IN-LEDGER the page cites a line the ledger never mentions

Exit code: 0 when nothing is bad, 1 otherwise.
"""
import argparse
import os
import re
import sys

EXT = r"(?:md|py|toml|json|sh|yaml|jsonl)"
CITE = re.compile(r"([A-Za-z0-9_./-]+\." + EXT + r"):(\d+)(?:-(\d+))?")


def read_ledger(path):
    """Return the set of (path, line) pairs the ledger mentions."""
    text = open(path, encoding="utf-8", errors="ignore").read()
    pairs, last = set(), None
    # full path:line pairs, plus shorthand `:NNN` that follows a full pair (same file)
    pat = re.compile(r"([A-Za-z0-9_./-]+\." + EXT + r"):(\d+)|(?<![\w.])`?:(\d+)")
    for m in pat.finditer(text):
        if m.group(1):
            last = m.group(1)
            pairs.add((m.group(1), m.group(2)))
        elif last:
            pairs.add((last, m.group(3)))
    return pairs


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Check that every path:line citation in a page resolves in the real code.",
        epilog="Exit code 0 means no bad citations.",
    )
    ap.add_argument("page", help="HTML page or markdown ledger to scan")
    ap.add_argument("--ledger", help="verified markdown ledger; every cite must appear in it")
    ap.add_argument("--root", action="append", required=True, metavar="DIR",
                    help="folder to resolve citations against (repeatable)")
    args = ap.parse_args(argv)

    raw = open(args.page, encoding="utf-8", errors="ignore").read()
    text = re.sub(r"<[^>]+>", "", raw) if args.page.endswith(".html") else raw
    ledger = read_ledger(args.ledger) if args.ledger else None
    roots = [r for r in args.root if os.path.isdir(r)]
    for r in args.root:
        if not os.path.isdir(r):
            print(f"WARNING root not found: {r}", file=sys.stderr)

    cites = sorted(set(CITE.findall(text)))
    bad = 0
    for path, a, b in cites:
        end = int(b or a)
        found = None
        for root in roots:
            p = os.path.join(root, path)
            if os.path.isfile(p):
                found = p
                break
        if not found and "/" not in path:
            hits = [os.path.join(d, path) for root in roots
                    for d, _, fs in os.walk(root) if path in fs]
            if len(hits) == 1:
                rel = os.path.relpath(hits[0], roots[0])
                print(f"BARE (resolves to {rel}) {path}:{a}")
                bad += 1
                found = hits[0]
        if not found:
            print(f"MISSING  {path}:{a}")
            bad += 1
            continue
        n = sum(1 for _ in open(found, errors="ignore"))
        if ledger is not None and (path, a) not in ledger and not any(
                os.path.basename(lp) == os.path.basename(path) and la == a for lp, la in ledger):
            print(f"NOT-IN-LEDGER {path}:{a}")
            bad += 1
        if end > n:
            print(f"OUT-OF-RANGE {path}:{a}-{end} (file has {n})")
            bad += 1
    print(f"{len(cites)} citations, {bad} bad")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
