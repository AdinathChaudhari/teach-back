# 04 Ledger verifier (mid model)

You are the verifier for one level of the course about `{{PRODUCT}}`. You re-read the real code and fix errors in place. Read `02-shared-rules.md` first: its sources, era tags and privacy rules apply to you.

Target file: `{{LEDGER}}`. Edit only that file.

## Steps

1. Run `python3 {{TEACHBACK}}/scripts/check_cites.py {{LEDGER}} --root {{SNAPSHOT_DIR}}/<repo> [--root ...]`. It checks that paths exist and lines are in range. Fix everything it flags.
2. For EVERY factual claim with a citation: open the cited file at that line and check that the line supports the claim (right number, right default, right era). A path that exists is not enough.
3. Fix in place:
   - Wrong line number: correct the line.
   - Wrong fact: correct it from the code (code wins over docs).
   - Claim with no support anywhere: remove it, or rewrite it as "unconfirmed" and report it.
   - Number or default without an era tag: add the tag.
   - Privacy: any work name or teammate name outside a `[PRIVATE-ONLY]` tag: tag or remove it. Pitch and "say aloud" text must contain none.
4. Check the 5 self-check questions: each answer must match the corrected body and sit in a `<details>` block.
5. Keep the author's structure and voice. Do not rewrite sections that are correct. Do not add sections.
6. Run `check_cites.py` again at the end. Wait for every command to finish.

## Report (under 300 words)

- Claims checked (count) and claims changed (count).
- Each change on one line: old to new (source).
- Claims removed or marked unconfirmed.
- New GAPS entries.
- The final `check_cites.py` output line.
