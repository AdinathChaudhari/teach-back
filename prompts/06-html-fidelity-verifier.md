# 06 HTML fidelity verifier (mid model)

You verify one story-shaped page against its verified ledger. The ledger is correct (already checked against the code). Your job is **fidelity**: the page must say what the ledger says. Edit only the page.

Page: `{{PAGE}}`. Ledger: `{{LEDGER}}`. Drift report: given in your task message (made by `{{TEACHBACK}}/scripts/check_drift.py`). Read `02-shared-rules.md` for privacy and era tags.

## Steps

1. Read the drift report. It lists (a) numbers on the page that do not appear in the ledger and (b) sentences about what "you" or "I" did, decided, told, wrote, found, ran, read or asked. Many number hits are noise (section numbers, minutes, a citation line list with a trailing comma). Skip those after a glance.
2. For each flagged number that is a real claim: find it in the ledger. If the page's number or era tag differs, fix the page to match the ledger. If the ledger lacks it, remove the claim.
3. For each user-action sentence: the ledger must support it with the same meaning (and, for levels 3 and 4, a build-log citation). If the page says the reader did something the ledger credits to the AI session, or says the reader felt or decided something the ledger does not, rewrite it to match the ledger.
4. Spot-check at least 40 `<code class="src">` chips (all, if fewer): find the same citation in the ledger and confirm the page sentence makes the same claim as the ledger sentence. Fix any drift.
5. Handle any known issues named in your task message.
6. Do not change design, CSS, JS or structure, except to fix a bug named in your task.

## Checks (wait for each)

- `python3 {{TEACHBACK}}/scripts/check_cites.py {{PAGE}} --ledger {{LEDGER}} --root {{SNAPSHOT_DIR}}/<repo>` reports 0 bad.
- The HTML parses.
- `grep -c '—' {{PAGE}}` prints 0.

## Final message (under 250 words)

Numbers fixed, user-action sentences fixed, chips spot-checked and fixed (count, and each change as old to new), known issues handled, check outputs.
