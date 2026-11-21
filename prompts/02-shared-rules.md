# 02 Shared rules (every worker and verifier reads this fully)

Project: a study course that teaches the reader their own product, `{{PRODUCT}}`, so they can explain and defend it with no AI beside them.

## Sources (read only; never edit them)

- Frozen code: `{{SNAPSHOT_DIR}}/`
- Build history: `{{BUILD_LOG}}`
- The approved plan: `{{OUT_DIR}}/run/plan.md`. Read the shared sections and your level's outline. Follow the outline's section order.

## Hard rules

1. **Cite everything.** Every factual claim cites `path:line`, repo-relative to the snapshot (for example `src/app/store.py:42`), or a log path with a line. Open the file and confirm the line before you cite it. If you cannot confirm, do not write the claim; put it in your GAPS entries.
2. **Code beats docs.** Where docs disagree with code, teach the code and note the disagreement.
3. **Era tags.** Every number and every default carries its era: `E1`, `E2`, ... as defined in the plan. Only the newest era describes what ships now. Old numbers stay, tagged, as history.
4. **Privacy.** Anything from work-only docs, employer or client names, internal numbers, or test data tied to private repos gets a `[PRIVATE-ONLY]` tag. Never write a teammate's or third party's name. The pitch and anything meant to be said aloud must be public-safe.
5. **Plain words.** Short sentences. No idioms. No hedging words. No em dashes. No "not X but Y". Use headers so the reader can skim back. Tables and small ASCII diagrams are welcome.
6. **Five self-checks.** End with exactly 5 self-check questions. Hide each answer: `<details><summary>Answer</summary>...</details>`.
7. **Fresh text.** Write your own words. Do not copy text from any other course or tool.
8. **Write only your own file.** Do not create or edit any other file. Wait for every background command before you report.

## Report back (final message, under 300 words)

- Path written and word count (`wc -w`).
- Sections written, matching the outline.
- GAPS entries: bullets of claims you could not confirm, contradictions, things that need a run. One line each with the source.
- Any place you departed from the outline, and why.
