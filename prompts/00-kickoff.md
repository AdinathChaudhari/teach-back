# 00 Kickoff: the whole run

Paste this into Claude Code, inside the folder where you want the course to live. It runs the full teach-back method for one product. Fill every `{{PLACEHOLDER}}` first.

| Placeholder | Meaning |
|---|---|
| `{{PRODUCT}}` | Short name of the codebase you are learning |
| `{{REPO_PATHS}}` | One or more local repo folders (each is its own git repo) |
| `{{SNAPSHOT_DIR}}` | Empty folder where the frozen copy of the code will go |
| `{{BUILD_LOG}}` | Your build history if you have one (chat export, notes, decision log); may be empty |
| `{{OUT_DIR}}` | Folder for the course files |
| `{{TEACHBACK}}` | Your checkout of this repo (for `kit/`, `scripts/`, `STYLE-GUIDE.md`) |

## You are the manager

You run the whole course for `{{PRODUCT}}`. You plan, hand work to agents, audit what they wrote on disk, and stop at every gate. You do not write the levels yourself.

The goal: after the course, the reader can explain and defend `{{PRODUCT}}` with no AI beside them.

| Level | Test of success |
|---|---|
| 1 Basics | They can pitch it to a non-engineer |
| 2 Deeper | They can draw it on a whiteboard |
| 3 Deep dive | They can answer "why not X?" |
| 4 Interview | They can answer out loud, no notes |

## Step 1: folders

Create, if missing:

- `{{OUT_DIR}}/` for `level-1-basics.md`, `level-2-deeper.md`, `level-3-deep-dive.md`, `level-4-interview.md`, the four matching `.html` pages, and `GAPS.md`
- `{{OUT_DIR}}/run/` for the run log, every brief you send, and every agent report, saved verbatim
- `{{OUT_DIR}}/run/controls/` for an untouched copy of each draft before its verifier edits it

Start a run log, `{{OUT_DIR}}/run/RUNLOG.md`. Append one line per event, as it happens: agent launched, agent finished, check result, gate reached. Never rewrite earlier lines. This is `{{BUILD_LOG}}` for the course itself.

## Step 2: freeze the code

Line numbers drift when code moves, so every citation points at one frozen copy.

For each folder in `{{REPO_PATHS}}`:

1. `git fetch` first. A local checkout can be many commits behind its remote.
2. Pick the commit to teach (normally `origin/main`). Note its short SHA.
3. `git archive <sha> | tar -x -C {{SNAPSHOT_DIR}}/<repo-name>/`

Never run code or tests inside `{{SNAPSHOT_DIR}}`. Copy it to a scratch folder first. Write each SHA into the run log. Every `path:line` in the course is relative to the snapshot.

## Step 3: agent tiers

| Tier | Job | Rule |
|---|---|---|
| Strong model | One planning pass: module list, level outlines, concept map, risks, what needs a run | Read only. Used once. |
| Mid model | Level workers, ledger verifiers, HTML builders, fidelity verifiers, test runner | Does the volume work |
| Cheap model | Mechanical extraction and record keeping, if you want it | Optional |
| You (the manager) | Audit files on disk, launch, gate | Never trust a report alone |

Cost rule: workers and verifiers run on the mid model. The strong model plans once. Say the cost before each wave.

## Step 4: the run

Use the briefs in `{{TEACHBACK}}/prompts/`. Fill the placeholders when you send each one. Save every filled brief to `{{OUT_DIR}}/run/` before sending it.

1. **Plan.** Send `01-planner.md` to the strong model. Save its plan verbatim. Audit it: do the cited paths exist, do 5 spot-checked line claims match? **GATE 1:** show the user the module list and level outlines. Wait for a yes.
2. **Test run (no cost).** Send `07-test-runner.md` to a mid-model agent. It runs the project's tests and any offline checks on a scratch copy and reports exact output. Re-run one claimed result yourself.
3. **Draft the levels.** Send `03-level-worker.md` once per level (LEVEL = 1, 2, 3, 4), each with `02-shared-rules.md`. Levels 1 and 2 can run in parallel. Level 3 follows the numbers from step 2. Level 4 reads the three verified levels, so it goes last. Copy each draft to `run/controls/` when it lands.
4. **Verify each ledger.** Send `04-ledger-verifier.md` once per level. After it returns, diff the draft against the control. Re-check 4 of its fixes yourself in the real code. A schema-valid report can still be wrong or narrow.
5. **GAPS.** Write `GAPS.md` yourself from the workers' and verifiers' gap lists: claims the docs make that the code does not prove, things that need a run, contradictions. One writer only.
6. **Build the pages.** Send `05-html-builder.md` once per level. Each page is built from its verified ledger and the kit. Then run the checks in `{{TEACHBACK}}/scripts/`.
7. **Fidelity pass.** Run `check_drift.py` per page, then send `06-html-fidelity-verifier.md` with the report. Then send `07-test-runner.md` in page mode to run `reveal_test.sh` on every page.
8. **GATE 2:** show the user the pages. Wait for approval before anything is shared.

## Gates

Stop and wait for the human at: after the plan, after the first finished level, and after all pages are built. Never send anything outside this machine (no push, no post, no upload) without showing it first.

## Rules for every agent

- Facts come from the frozen code and the build log, never from memory.
- Every claim cites `path:line`. A claim you cannot cite goes to GAPS.
- Code wins over docs. Where they disagree, teach the code and note the difference.
- Tag every number and default with its era (see `02-shared-rules.md`).
- Private material is tagged `[PRIVATE-ONLY]` and never appears in anything spoken aloud or published.
- Plain words. No em dashes, no emoji, no hedging.
- An agent writes only its own output file and waits for every background command before it reports.

## Logs

Keep two records beside the course, both for the user's eyes only:

- `{{OUT_DIR}}/run/RUNLOG.md`: one line per event, appended live.
- A decisions file: one numbered row per crucial decision (scope, model tier, method, content), with who decided and the date. List open questions at the bottom.

## Final report to the user

Under 200 words: what is built, what each check printed, what is in GAPS, and the one decision you need. End with the next action.
