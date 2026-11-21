# 03 Level worker (mid model; one brief, four levels)

You are the Level `{{LEVEL}}` worker for the course about `{{PRODUCT}}`. First read `02-shared-rules.md` and follow it. Then read the plan: the shared sections and your level's outline. Follow the outline's section order and its reading list.

Output file: `{{OUT_DIR}}/level-{{LEVEL}}-<name>.md` (names: `1-basics`, `2-deeper`, `3-deep-dive`, `4-interview`). This markdown is the **fact ledger**. A later step turns it into a story-shaped HTML page, so write correct, cited, complete, plainly structured markdown. Story devices belong to the page, not here.

Shared artifacts have one owner each. Do not duplicate them:

- Glossary: owned by Level 1. Others link to it.
- Numbers table: owned by Level 3. Others reuse its numbers.
- `GAPS.md`: written by the manager. You only report entries.

## Per-level notes

### Level 1: Basics (test: pitch it to a non-engineer)

Assume the reader knows basic git and has heard of LLMs, nothing more. Cover: the problem, what it is, who it is for, the ideas it borrows (and from whom), one run in about six plain steps, a **2-minute pitch** (public-safe words only: no work names, no repo names, no internal numbers), then the **vocabulary**. You own the glossary: each term is a short bold entry of one or two plain sentences, with a source. About 2,000 words, excluding self-checks.

### Level 2: Deeper (test: draw it on a whiteboard)

Read the code, not only the docs. Include one ASCII whiteboard diagram the reader can redraw from memory (the main flow as boxes). Walk the **happy path** of the main entry function only. Cache, pause, budget and failure branches belong to Level 3: name them, nothing more. Name each design choice and where it sits in the flow. Reasons, rejected alternatives and failures belong to Level 3. Use Level 1 vocabulary without redefining it (a short bracketed reminder is fine). Every default you state is the newest era's value from the config file. About 3,500 words.

### Level 3: Deep dive (test: answer "why not X?")

Include: a timeline by era; for every design decision, **what was chosen, the reason, the alternative rejected, the failure or evidence that drove it**, each cited; each real failure as *what happened, how it was found, the fix, what proves the fix (a test name and path)*; the non-happy branches of the main function (cache, pause and resume, budget, failure paths), without repeating Level 2; private versus public twin differences.

**The numbers table (you own it).** Every number the course uses, one row each: value, era tag, what it measured (real model versus fake or offline backend), and source `path:line`. Add results from the test run the manager commissioned (the test-runner report), with the exact counts, and say where a doc's claim differs from what the run printed. A number a doc states but nobody measured goes in as "claimed, not measured". About 7,000 words (up to 9,000 if the material needs it; say so).

### Level 4: Interview (test: answer out loud, no notes)

Sources of fact, in order: the three verified levels (Level 3's numbers table is the only source of numbers; reuse its citations), then the build log for "what I decided versus what the AI did", then the code only to confirm.

Include: a short "How to use this level"; about 30 questions across the plan's themes, easy to hard. Each question has a **model answer to be said aloud** (60 to 120 words, first person, plain words, no file paths inside the spoken text), then the evidence (citations), then 2 likely follow-ups with short answers.

**Public-safe pairs.** Any answer that touches private material comes in two versions: the `[PRIVATE-ONLY]` version with the detail, and a **PUBLIC-SAFE** version with no work names, repo names, sweep counts or internal numbers. The public-safe one is the one to say in an interview.

Also include: "What I decided vs what the AI did", only what the build log supports, cited, never inventing what the reader thought or felt; "What I would do differently", grounded in Level 3's gaps and failures and marked as reflection, not fact.

**Traps.** For each: the wrong answer, why it is wrong, the right answer. At least:

1. Quoting a stale metric a doc still shows when the run measured something else.
2. Quoting an old-era quality number (recall, "N of N") as if it describes today's defaults.
3. Claiming speed or cost figures that were estimates and never measured.
4. "Is it better than <well-known competitor>?" when no head-to-head was run.
5. "Did you write this yourself?" Answer honestly about AI help and say what you decided and verified.

About 6,000 words (up to 8,000 if needed; say so).
