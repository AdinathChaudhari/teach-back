# Visual and interaction design for self-study HTML pages

Scope: the HTML-specific "how" for a guide that teaches an engineer their own tool. Retention basics (retrieval, spacing, chunking, dual coding) are in STYLE-GUIDE.md with published sources and are not repeated. Evidence ratings in this note are provisional.

**Source honesty.** "Opened" means I read the page or PDF text. "Snippet only" means I saw it in a search summary and did not open the paper. Effect sizes below come only from the Mayer 2023 chapter I opened, unless marked. All studies are mostly short lab lessons with students, not engineers reading a long technical guide. Treat the numbers as direction, not as promises.

## 1. Mayer's principles

Source for every number in this section: Mayer, R. E. (2023), "Research-Based Principles for Designing Multimedia Instruction", in *In Their Own Words*, APA Division 2. PDF: https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-research-based-principles-for-designing-multimedia-instruction-mayer.pdf (opened). He reports medians from his own 2021 review, so the author is also the main evaluator. That lowers my confidence a little. Mayer calls d above 0.40 "educationally important".

| Principle | Claim | Median d, tests | Strength | Fits a static page? |
|---|---|---|---|---|
| Coherence | Cut interesting but irrelevant material | 0.86, 18 of 19 | moderate-strong | Yes. Biggest lever. |
| Signaling | Headings, outlines, arrows, bold on key words | 0.70, 26 of 28 | moderate-strong | Yes. Use sparingly. |
| Spatial contiguity | Put labels on the diagram part, not in a legend | 0.82, 9 of 9 | moderate | Yes. |
| Segmenting | Learner-paced chunks with a "continue" | 0.67, 7 of 7 | moderate (few tests) | Yes. Natural for pages. |
| Pre-training | Teach the key terms before the process | 0.78, 10 of 10 | moderate (few tests) | Yes. A glossary-first card. |
| Personalization | Conversational "you/your" wording | 1.00, 13 of 15 | moderate | Yes. Cheapest to do. |

Boundary conditions that matter here: signaling and pre-training help novices more than experts; pre-training may not help if the learner already knows the terms. Our reader built the tool but may not hold the vocabulary, so pre-train terms and let them skip. Personalization may fade in long lessons. Most tests used short animations, so applying them to a text page is an extension, not a proven result.

**Patterns (one per principle):**
- Coherence: every element must answer "does this help explain or defend the tool?" The page has no mascot and no stock art.
- Signaling: in a code excerpt, bold only the one line that matters in that step. Never bold whole paragraphs.
- Spatial contiguity: put labels directly on the SVG pipeline boxes, with a thin leader line, not in a key below.
- Segmenting: each section ends with a "Next: section name" button. Body text stays short enough to finish in one sitting.
- Pre-training: a "Words you will meet" strip at the top of each section, three terms, one plain line each.
- Personalization: write "you" and "your tool", for example "Your tool reads the diff first." Not "the tool reads the diff."

## 2. Click-to-reveal and commit-then-reveal

**Claim A.** Trying to answer first, even wrongly, helps learning more than just reading the answer. Strength: strong for retrieval (covered in the standard); moderate for failed attempts.
- Mayer 2023 chapter lists self-testing at d = 0.57 over 76 tests (opened, same PDF).
- Overman, Stephens and Bernhardt (2021), *Memory* 29(8): after a wrong attempt, corrective feedback was remembered better than reading only. https://pmc.ncbi.nlm.nih.gov/articles/PMC8440464 (opened first 100,000 characters). It tested word-style materials, not code.
- Kornell, Hays and Bjork (2009), "Unsuccessful retrieval attempts enhance subsequent learning", and Richland, Kornell and Kao (2009): snippet only. A PubMed fetch failed. Findings there: pretest guesses beat extra study time, though the effect is smaller for unrelated pairs.

**Pattern: Predict-then-reveal card.** A question, a text box (or 3 choice buttons), and a disabled "Show answer" button. The button unlocks once the reader types at least a few characters or picks an option. Then it shows the answer next to the reader's own words, with a "Got it / Missed it" tap.

**Claim B.** Typing beats clicking, because typing forces production. Strength: practitioner opinion plus the generation effect (Slamecka and Graf 1978, in the standard). I found no study comparing type-in to click-choose on a web page. Do not claim one.

**Tension with a common rule.** A common retrieval-practice rule says answers should live only in an end answer key. A same-page reveal puts the answer near the question. It is still safe if the reader must commit first, so the answer is not visible during thinking. The course keeps both: the same-page reveal after commit, and a full key at the end. Keep a final mixed quiz with answers hidden until typed.

**Pattern: Commit-lock.** Store the reader's typed text in localStorage (wrapped in try/catch). On revisit tomorrow, show their old answer beside the model answer. This supports spacing too.

## 3. Diagrams that teach

**Claim.** A diagram that builds up in steps, with one new thing per step, beats a full diagram shown at once for novices. Strength: moderate. This is segmenting (d = 0.67) plus signaling (visual signaling d = 0.71, 11 of 12 tests), both from the Mayer chapter. For code-review tools, nobody has tested it. That part is my inference.

**Pattern: Step-through pipeline.** An inline SVG of the tool's stages (diff in, rules, model, findings, output). Buttons "Back / Next". Each press lights one stage and dims the rest, and swaps a one-sentence caption beneath. A "Show all" toggle for review. Pure CSS classes, no animation library.

**Explorable explanations (opened sources).**
- Bret Victor, "Explorable Explanations": https://worrydream.com/ExplorableExplanations/. Idea: a document where the reader changes assumptions and sees results. His 2024 note says the term now often means any article with interactive graphics, which is not what he meant. His claim is opinion and design vision, not a tested result.
- Nicky Case, "Explorable explanations": https://blog.ncase.me/explorable-explanations/. Practitioner advice: use interactivity only where it works best; build up one mechanic at a time; gate later content; embed practice; playtest with real people because explorers skim and get lost. Opinion, but from playtesting.
- Ciechanowski (ciechanow.ski, "Mechanical Watch") and Case's "How to Remember Anything Forever-ish" (ncase.me/remember): snippet only. I saw reviews describing 100+ interactive images and a 20-minute interactive comic. I did not open them, so I cannot say what the interactions are.

**Worth it vs gimmick, for a 5-line-excerpt guide:**
- Worth it: step-through of the real pipeline; a "change the input, watch the verdict" toy only if the tool has a deterministic part to show; predict-then-reveal.
- Gimmick: scroll-hijacking "scrollytelling", 3D, free-play sliders with nothing to learn from. I found no controlled evidence that scrollytelling beats a plain stepper, so the cost (build time, phone bugs) is not justified.

## 4. Reading pace and layout for ADHD readers

The honest finding: I found almost no ADHD-specific layout experiments. Most "ADHD design" advice is practitioner opinion. Label accordingly.

- **Line length.** Evidence, moderate and mixed. Dyson and Haselgrove (2001) and Dyson and Kipping (1998) on screens: longer lines (about 100 characters) read faster, but readers prefer 45 to 72 (snippet only; a secondary summary). WCAG 1.4.8 (opened): width no more than 80 characters, line spacing at least 1.5, paragraph spacing at least 1.5 times line spacing (Level AAA). https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html. Butterick (opened): 45 to 90 characters, explicitly rule-of-thumb opinion. https://practicaltypography.com/line-length.html. **Pattern:** `max-width: 66ch; line-height: 1.6;` for body text, code blocks may be wider.
- **Spacing and ADHD.** Weak. Stern et al. (2013), via a secondhand summary only: double spacing and screen text helped teens who already had good sustained attention, not those with poor attention. I did not open the paper. Moussaoui et al. (2025), snippet only: adults with ADHD did better with one-word-at-a-time (RSVP) reading. Small and early. Do not build around it.
- **Chunk size, progress bars, time estimates, "you are here" maps.** Practitioner opinion. I found no study that tests them for ADHD. They are cheap and low risk, and segmenting (strong-ish) supports the chunking part. **Pattern: Sticky section rail.** A thin left (desktop) or top (phone) rail listing the sections, current one highlighted, each with "~4 min". Clicking jumps.
- **Callout boxes.** Opinion. Signaling works only when sparing ("visual and verbal signals used sparingly", Mayer 2023). **Pattern:** at most 2 callouts per screen, 3 kinds only: "Say this in the interview", "Watch out", "Try it".
- **Section chunk size.** Opinion, my default: one idea per section, under about 250 words, then an interaction. Not from a study.
- **Bionic-style bolding of word starts.** Weak. I saw only a consumer article and could not find the original study. Skip it.

## 5. Typography, colour, and code on screen

No strong experiments found for long technical reading beyond line length. Treat these as practitioner opinion with accessibility standards behind them.
- System font stack for body, one monospace stack for code, two weights. Body about 17 to 19 px, 16 px minimum on phones.
- Contrast: aim for WCAG AA (4.5:1) in both modes. Never pure black on pure white; use a soft off-white/off-black pair. Define colours as CSS variables, with `prefers-color-scheme` for dark mode.
- One accent colour for "interactive", one for "danger/watch out", the rest neutral. Colour must never be the only signal (add an icon or word).

**Pattern: Code excerpt with file:line chip.** A `<figure>` with a small chip above the block, for example `review/rules.py:42-46`, and a "copy path" tap. Five lines, monospace, horizontal scroll rather than wrap. One line highlighted with a background band, and a numbered gutter that matches the real file line numbers (so the reader can open the file and find it). A one-line caption below states what to notice. Use only real excerpts, never invented code. Do syntax highlighting with at most 3 token colours, or none; the band does the signaling.

## 6. Visible progress and small rewards

- **Evidence for gamification.** Sailer and Homner (2020), *Educational Psychology Review*: meta-analysis, cognitive g = 0.49 (k = 19), motivational g = 0.36 (k = 16); the cognitive effect held in high-rigor studies, motivational and behavioural effects were less stable; authors warn of low power. https://link.springer.com/article/10.1007/s10648-019-09498-w (snippet only; fetch redirected). A 2023 meta-analysis found g = 0.257 for intrinsic motivation (snippet only: https://link.springer.com/article/10.1007/s11423-023-10337-7). So: small to moderate benefit, shaky on motivation.
- **Overjustification.** Deci, Koestner and Ryan (1999), 128 experiments: tangible rewards can undermine intrinsic motivation; verbal praise did not (snippet only; the exact d values I saw were on a blog and I could not verify them, so I give none). The debate is not closed (Cameron and Pierce 1994 disagreed). Link: https://journals.sagepub.com/doi/10.3102/00346543071001001 (snippet only).
- **Reading of the evidence for a single-reader guide.** The reader is the only user, so social leaderboards are irrelevant. Cheap informational feedback ("5 of 8 sections done") is low risk. Points, badges, and streak-loss penalties are the risky parts: a broken streak can turn a study habit into guilt, which is a real risk for any self-study habit. This last point is my judgement, not a finding.
- Nicky Case (opened) warns that gamification changes behaviour, while explanation should change knowledge.

**Pattern: Tick-and-count.** Each section header has a checkbox that fills when the reader completes its predict card (not when they scroll). A line at the top shows "3 of 8 sections done, about 22 min left". State in localStorage with try/catch. No points, no streaks, no loss states. When all are done, show a plain "Done. Come back tomorrow for the mixed quiz."

## 7. Anti-patterns

- **Decorative images (seductive details).** Strong enough to act on. Coherence d = 0.86 from Mayer 2023 (opened). Rey (2012) meta-analysis found a small effect on recall and medium on transfer, stronger under time limits (snippet only, secondary descriptions). A 2026 meta-analysis of 50 studies found a small negative effect (snippet only). Caveat: effect is smaller when study time is unlimited, which is our case, so the penalty is probably mild. Still not worth any benefit.
- **Animation for its own sake.** Moderate. Mayer's boundary notes say extra material hurts most when lessons are fast and system-paced. Keep motion learner-triggered (a button press), under 300 ms, and honour `prefers-reduced-motion`.
- **Walls of callouts.** Signaling backfires when overused. Mayer: signals work "when used sparingly".
- **Too many colours.** Opinion plus signaling logic. If everything is highlighted, nothing is.
- **Gate-free interactivity.** Case (opened): readers skim and skip prerequisites. If a reveal can be clicked with nothing typed, it is just a collapsed paragraph.

## Component kit, ranked by value

1. **Predict-then-reveal card.** Makes the reader commit an answer before seeing it. Behaviour: text box, Show-answer unlocks after input, then shows the model answer beside the reader's text with a Got-it / Missed-it tap.
2. **Code excerpt with file:line chip.** Anchors the guide to the real code. Behaviour: 5-line monospace block, one highlighted line, gutter with real line numbers, copy-path chip, one-line caption.
3. **Step-through pipeline diagram.** Shows the tool's flow one stage at a time. Behaviour: inline SVG, Next/Back lights one stage, caption swaps, Show-all toggle.
4. **Interview-answer card ("Say this").** Gives a 30-second spoken answer to defend a design choice. Behaviour: shows the question, hides the model answer until the reader types their own version, then reveals it.
5. **Sticky section rail with time and ticks.** The "you are here" map. Behaviour: lists sections with minutes, highlights the current one, ticks done ones, jumps on click.
6. **Words-you-will-meet strip (pre-training).** Teaches three terms before a section. Behaviour: three chips, tap to flip plain definition, skippable.
7. **Why-card.** Asks "why did we choose X?" before the reason. Behaviour: same commit-lock as card 1, with the real decision from the project log shown after.
8. **Mixed final quiz with next-day return.** Spaced, interleaved recall. Behaviour: shuffled questions from all sections, answers hidden until typed, stores answers and shows them again on the next visit.
9. **Callout trio ("Say this", "Watch out", "Try it").** Signals the three things worth attention. Behaviour: styled box with icon and label, capped at 2 per screen.
10. **Plain progress line.** Informational progress without gamification. Behaviour: "3 of 8 done, about 22 min left" text and thin bar, no streaks or points.

## Anti-patterns to ban

1. Decorative art, mascots, stock illustrations, emoji strips.
2. Reveal buttons that work with no input.
3. Streaks, points, badges, or any loss state.
4. Scroll-hijacking scrollytelling and autoplaying motion.
5. More than 2 callouts per screen, or more than 3 colours beyond neutrals.

## Sources I could not open

- Kornell, Hays and Bjork (2009) and Richland, Kornell and Kao (2009): PubMed fetch failed; search snippet only.
- Sailer and Homner (2020): Springer redirected to a login; snippet only.
- Rey (2012), Harp and Mayer (1998), Deci et al. (1999), Dyson and Haselgrove (2001), Dyson and Kipping (1998), Stern et al. (2013), Moussaoui et al. (2025), the 2023 gamification meta-analysis, the 2026 seductive-details meta-analysis, Ciechanowski, Case's remember explorable: snippet or secondary description only.
- Mayer's per-principle effect sizes are from his own 2023 chapter. I did not open the primary meta-analyses (Alpizar et al. 2020 reported signaling d = .38 pooled, snippet only, which is lower than Mayer's 0.70, so expect real-world effects smaller than the table).
