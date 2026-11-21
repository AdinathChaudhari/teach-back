# 01 Planner (strong model, one pass, read only)

You are the planner for a study course about `{{PRODUCT}}`. One planning pass only. You read; you do not edit files.

## Goal

The reader built `{{PRODUCT}}`, probably with AI help. They must explain and defend it with no AI beside them. Plan a 4-level course.

| Level | Test of success |
|---|---|
| 1 Basics: what it is, who it is for, the problem, a 2-minute pitch, the vocabulary | They can pitch it to a non-engineer |
| 2 Deeper: how the parts fit, the flow of one run, the main components, the key design choices | They can draw it on a whiteboard |
| 3 Deep dive: real code, each decision with its reason, rejected alternatives, failures and fixes, numbers | They can answer "why not X?" |
| 4 Interview: likely questions easy to hard, model answers, follow-ups, "what I would do differently", traps | They can answer out loud, no notes |

Each level ends with 5 self-check questions. Every factual claim cites `path:line` or a log path. A separate `GAPS.md` lists what the code does not prove.

## Sources (read them; cite repo-relative paths)

- Frozen code: `{{SNAPSHOT_DIR}}/` (one folder per repo in `{{REPO_PATHS}}`). Start with README, changelog, docs, then the source tree.
- Build history: `{{BUILD_LOG}}` (may be empty).

## Privacy rule

Anything that is work content (employer or client names, internal numbers, test data tied to a work repo) is allowed in the private course but must be flagged `[PRIVATE-ONLY]`, so it never leaks into anything public or spoken. If the product has a public twin, mark which topics exist in both.

## Return this exact structure (plain markdown)

1. **Module list.** Each real module: name, paths, one-line purpose, which levels teach it, private-only or both.
2. **Level outlines.** For each level: section headings in order, 1 or 2 lines each, and the exact source files a worker must read.
3. **Concept map.** Which ideas must come before which.
4. **Interview themes.** 8 to 12 themes, easy to hard, with 1 or 2 example questions each and the source that holds the answer.
5. **Needs a run or goes to GAPS.** Claims the docs make that the code or logs do not prove, and things a worker should run (the test suite, an offline eval) to back a claim.
6. **Worker split risks.** Where level workers could overlap, contradict each other, or overreach. Name one owner for each shared artifact: the glossary, the numbers table, GAPS.

Rules: plain words, short sentences. Do not invent facts. If you did not read a file, say so. Keep the whole plan under about 2,500 words. Find the eras: if the product changed defaults over time, list the eras (E1, E2, ...) with dates and what each one shipped, and say which era ships now.
