#!/usr/bin/env bash
# Reveal test: does every commit-first card unlock and reveal in a real browser?
#
# Usage:  bash scripts/reveal_test.sh PAGE.html
# Env:    CHROME  path to a Chrome/Chromium binary
#                 (default: the macOS Google Chrome app)
#
# Copies PAGE to a temp folder with scripts/probe.js appended, loads it in
# headless Chrome with --dump-dom, and prints the title the probe sets:
#   answers=N stillHidden=M   N answer blocks found, M still hidden (want 0)
#   JSERROR <message>         the page threw a JavaScript error
# Your page is never modified.
set -euo pipefail

PAGE="${1:-}"
if [ -z "$PAGE" ] || [ ! -f "$PAGE" ]; then
  echo "usage: bash scripts/reveal_test.sh PAGE.html" >&2
  exit 2
fi
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
if [ ! -x "$CHROME" ]; then
  echo "Chrome not found at: $CHROME (set \$CHROME)" >&2
  exit 2
fi

HERE="$(cd "$(dirname "$0")" && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cat "$PAGE" "$HERE/probe.js" > "$TMP/page.html"

# Chrome may print log noise on stderr; the DOM goes to stdout.
DOM="$("$CHROME" --headless=new --disable-gpu --no-sandbox --virtual-time-budget=4000 \
  --dump-dom "file://$TMP/page.html" 2>/dev/null || true)"
TITLE="$(printf '%s' "$DOM" | tr '\n' ' ' | sed -n 's/.*<title>\([^<]*\)<\/title>.*/\1/p')"

case "$TITLE" in
  "RESULT "*) echo "${TITLE#RESULT }" ;;
  "JSERROR "*) echo "$TITLE"; exit 1 ;;
  *) echo "no probe result (page title: ${TITLE:-none})"; exit 1 ;;
esac
