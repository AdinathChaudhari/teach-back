export const meta = {
  name: 'teachback-course',
  description: 'teach-back full course: plan (strong model) -> 4 levels draft+verify -> GAPS -> HTML pages + fidelity checks (mid model), one course at a time',
  phases: [{ title: 'Plan' }, { title: 'L1-L2' }, { title: 'L3-L4' }, { title: 'GAPS' }, { title: 'HTML' }],
}
// Claude Code Workflow script: runs prompts/00-kickoff.md end to end with no human gates.
// Use it when you have already approved the method and want several courses built unattended.
// The briefs in prompts/ stay the source of truth; this script only fills their placeholders and
// chains the agents. Freeze each repo first (00-kickoff.md step 2) so `snap` exists.
//
// args = {
//   teachback: '/abs/path/to/teach-back',            // this repo (prompts/, scripts/, kit/)
//   scratch:   '/abs/path/to/scratch-dir',           // where test runs copy the snapshot (never run in snap)
//   strongModel: 'opus', midModel: 'sonnet',         // optional; planner once, everything else mid
//   courses: [{
//     product: 'name', sha: 'abc1234',
//     out:  '/abs/OUT_DIR',  snap: '/abs/SNAPSHOT_DIR',
//     buildLog: 'paths or notes the agents may read (code wins over docs)',
//     privacy:  'e.g. "public repo; tag anything only the private logs reveal [PRIVATE-ONLY]"',
//     startAt:  'plan' | 'L12' | 'L34' | 'gaps' | 'html',   // optional, to resume a course mid-way
//   }],
// }
const TB = args.teachback
const STRONG = args.strongModel || 'opus'
const MID = args.midModel || 'sonnet'
const FILES = { 1: 'level-1-basics', 2: 'level-2-deeper', 3: 'level-3-deep-dive', 4: 'level-4-interview' }
const ORDER = ['plan', 'L12', 'L34', 'gaps', 'html']
const out = []

for (const c of args.courses) {
  const start = ORDER.indexOf(c.startAt || 'plan')
  const OUT = c.out, SNAP = c.snap
  const PH = `Placeholders: PRODUCT = ${c.product}. SNAPSHOT_DIR = ${SNAP} (frozen commit ${c.sha}; cite paths relative to it). OUT_DIR = ${OUT}. TEACHBACK = ${TB}. BUILD_LOG = ${c.buildLog} (read-only; code wins over docs). Privacy: ${c.privacy}`
  const rec = { product: c.product }
  log(`=== ${c.product} (from ${ORDER[start]}) ===`)

  if (start <= 0) {
    const [plan, tests] = await parallel([
      () => agent(`Read ${TB}/prompts/01-planner.md and follow it as the planner. ${PH}
You read code only. The single file you write is your plan, verbatim, to ${OUT}/run/02-plan.md. Return a 5-line summary.`, { label: `${c.product}: planner`, phase: 'Plan', model: STRONG }),
      () => agent(`Read ${TB}/prompts/07-test-runner.md and follow it in code mode. ${PH}
Never run anything inside SNAPSHOT_DIR: copy it to ${args.scratch}/${c.product}-scratch first and run there (git init + commit there if a tool needs git; local venv or npm install there). Run the test suite and offline checks that need no network or paid keys. Never call paid APIs.
Write the full report with exact output to ${OUT}/run/03-test-run-report.md. Wait for every background command. Return a 10-line summary.`, { label: `${c.product}: tests`, phase: 'Plan', model: MID }),
    ])
    rec.audit = await agent(`Audit the course plan at ${OUT}/run/02-plan.md against frozen code at ${SNAP}. 1) Check every cited path exists and every cited line is within the file length. 2) Verify 6 concrete claims (MATCH/WRONG + real line). 3) List source modules the plan skipped. Write the report to ${OUT}/run/04-plan-audit.md and return it (under 400 words).`, { label: `${c.product}: plan audit`, phase: 'Plan', model: MID })
    rec.plan = plan; rec.tests = tests
  }
  const CTX = `Approved plan: ${OUT}/run/02-plan.md (follow your level's outline). Plan audit corrections to apply: ${OUT}/run/04-plan-audit.md. Test facts: ${OUT}/run/03-test-run-report.md. Earlier verified levels (if present) in ${OUT}/ are the source of truth for shared facts; do not contradict them.`
  const level = (L) => agent(`You are the Level ${L} worker. Read ${TB}/prompts/02-shared-rules.md and ${TB}/prompts/03-level-worker.md; follow them with LEVEL = ${L}. ${PH}
${CTX}
Write only ${OUT}/${FILES[L]}.md. When final, cp it byte-for-byte to ${OUT}/run/controls/${FILES[L]}.md. Run python3 ${TB}/scripts/check_cites.py ${OUT}/${FILES[L]}.md --root ${SNAP} and fix bad cites (build-log files outside the snapshot: cite as "file name line N", no colon). Wait for every command. Return word count, checker last line, and your gap list.`, { label: `${c.product}: L${L} draft`, phase: L <= 2 ? 'L1-L2' : 'L3-L4', model: MID })
  const verify = (L, draft) => agent(`You are the ledger verifier. Read ${TB}/prompts/04-ledger-verifier.md and follow it. LEDGER = ${OUT}/${FILES[L]}.md. ${PH}
Untouched draft: ${OUT}/run/controls/${FILES[L]}.md (never edit it). Edit only the ledger. Then run python3 ${TB}/scripts/check_cites.py ${OUT}/${FILES[L]}.md --root ${SNAP}. Return every fix (old -> new with path:line), the checker's last line, and new GAPS. Worker report:
${draft}`, { label: `${c.product}: L${L} verify`, phase: L <= 2 ? 'L1-L2' : 'L3-L4', model: MID })
  const lv = async (L) => { const d = await level(L); const v = await verify(L, d); return `## L${L} worker\n${d}\n\n## L${L} verifier\n${v}` }

  if (start <= 1) rec.L12 = await parallel([1, 2].map(L => () => lv(L)))
  if (start <= 2) { rec.L3 = await lv(3); rec.L4 = await lv(4) }
  if (start <= 3) rec.gaps = await agent(`Write ${OUT}/GAPS.md for the ${c.product} course (you are the only GAPS writer). Sources: section 5 of ${OUT}/run/02-plan.md, the gap lists inside the four verified levels ${OUT}/level-*.md, the plan audit ${OUT}/run/04-plan-audit.md, and the test report ${OUT}/run/03-test-run-report.md. Group: (1) claims docs make that code does not prove, (2) things that need a run, (3) contradictions between docs and code, (4) open design questions. Each item: one plain line plus its path:line source. Dedupe. No em dashes. ${PH}
Then run python3 ${TB}/scripts/check_cites.py ${OUT}/GAPS.md --root ${SNAP} and fix bad cites. Return item count per group and the checker's last line.`, { label: `${c.product}: GAPS`, phase: 'GAPS', model: MID })
  if (start <= 4) rec.html = await parallel([1, 2, 3, 4].map(L => async () => {
    const PAGE = `${OUT}/${FILES[L]}.html`, LEDGER = `${OUT}/${FILES[L]}.md`
    const b = await agent(`Read ${TB}/prompts/05-html-builder.md and follow it. LEVEL = ${L}. LEDGER = ${LEDGER}. PAGE = ${PAGE}. ${PH}
Copy the kit CSS/JS, fonts, A-/A/A+ size control, layout v2 block and component markup from ${TB}/kit/template.html. Read ${TB}/STYLE-GUIDE.md. Write only PAGE. Run python3 ${TB}/scripts/check_cites.py ${PAGE} --ledger ${LEDGER} --root ${SNAP} and bash ${TB}/scripts/reveal_test.sh ${PAGE}; fix until 0 bad and stillHidden=0. Return both checker lines.`, { label: `${c.product}: L${L} html`, phase: 'HTML', model: MID })
    const f = await agent(`Run python3 ${TB}/scripts/check_drift.py ${PAGE} ${LEDGER}, then read ${TB}/prompts/06-html-fidelity-verifier.md and follow it with PAGE = ${PAGE}, LEDGER = ${LEDGER}, SNAPSHOT_DIR = ${SNAP}, TEACHBACK = ${TB}. Fix the page only. Then run python3 ${TB}/scripts/patch_layout.py ${PAGE} (no-op if the page already has layout v2). Finally run python3 ${TB}/scripts/check_cites.py ${PAGE} --ledger ${LEDGER} --root ${SNAP} and bash ${TB}/scripts/reveal_test.sh ${PAGE}. Return fixes made plus both final checker lines. Builder said:
${b}`, { label: `${c.product}: L${L} fidelity`, phase: 'HTML', model: MID })
    return `## L${L} html builder\n${b}\n\n## L${L} fidelity\n${f}`
  }))
  out.push(rec)
  log(`=== ${c.product} done ===`)
}
return out
