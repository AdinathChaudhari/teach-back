#!/usr/bin/env python3
"""Flag possible drift between an HTML page and its verified markdown ledger.

Usage:
    check_drift.py PAGE LEDGER

Prints two reports:
  1) NUMBERS not in ledger: numbers in the visible HTML text (scripts and styles
     skipped) that never appear in the ledger. Many hits are noise (section
     numbers, minutes); the real ones are claims the ledger does not back.
  2) USER-ACTION sentences: lines that say "you" or "I" chose, decided, told,
     wrote, found, ran, read, asked, built, noticed, picked or said something.
     The ledger must support each one, or the page invents what the reader did.

Always exits 0: it is a report for a human or a verifier agent, not a gate.
"""
import argparse
import html
import re
from html.parser import HTMLParser

NUM = r"(?<![\w.])\$?\d[\d,]*(?:\.\d+)?%?"
ACTION = re.compile(r"\b(you|I) (chose|decided|told|wrote|found|ran|read|asked|built|noticed|picked|said)\b", re.I)


class Visible(HTMLParser):
    """Collect visible text; skip <style> and <script>; break lines at block tags."""

    def __init__(self):
        super().__init__()
        self.skip = 0
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("style", "script"):
            self.skip -= 1
        if tag in ("p", "li", "td", "th", "h1", "h2", "h3", "div", "summary"):
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Flag possible drift between an HTML page and its verified markdown ledger.")
    ap.add_argument("page", help="HTML page to inspect")
    ap.add_argument("ledger", help="verified markdown ledger")
    args = ap.parse_args(argv)

    v = Visible()
    v.feed(open(args.page, encoding="utf-8", errors="ignore").read())
    text = html.unescape("".join(v.out))
    ledger = open(args.ledger, encoding="utf-8", errors="ignore").read()

    odd = sorted(n for n in set(re.findall(NUM, text)) - set(re.findall(NUM, ledger))
                 if len(n.strip("$%").replace(",", "")) >= 2)
    print("NUMBERS not in ledger:", ", ".join(odd) if odd else "none")
    lines = [l.strip() for l in text.split("\n") if ACTION.search(l)]
    print(f"USER-ACTION sentences: {len(lines)}")
    for l in lines:
        print("  -", l[:220])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
