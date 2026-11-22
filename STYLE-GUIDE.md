# Teach-back style guide

Reusable for every course page, for any product. One page, ten rules, four settled decisions, one checklist. Rules rest on published learning science, listed under Sources below, and on two research notes: **NP** = `research/narrative-pull.md`, **VD** = `research/visual-design.md`. All evidence ratings are provisional (decision d).

## The ten rules

1. **Commit, then reveal.** The reader types an answer or picks an option before the answer can be shown. The reveal button stays disabled until they do. (Roediger and Karpicke 2006; Karpicke and Blunt 2011; Slamecka and Graf 1978; VD section 2)
2. **Open on a puzzle, close on a question.** Each section starts with a small problem the reader can almost solve, and ends on an open question that the next section answers. Close every loop in the very next section. (NP section 1 and 3)
3. **Every story beat carries a fact or a reason.** Delete the beat. If the reader loses nothing, cut it. No jokes or colour on the diagrams or in the first lines of a section. (NP section 7; VD coherence)
4. **Tell history as cause and effect.** Use "so" to link steps: this failed, so you added that. Each "so" is something the reader can say later. (NP section 2)
5. **Pre-teach few words, earn the rest.** Four or five core terms at the top. Every other term gets a short plain definition where it first appears. (NP section 5; VD pre-training)
6. **Write to "you" and "your tool".** The reader is the builder. Short sentences, plain words, no idioms. (Mayer, personalization principle; VD personalization)
7. **Chunk and step.** One idea per section, then an interaction. Show a process one step at a time, with every step also readable as a plain list. (Mayer, segmenting principle; Paivio, dual coding for the diagram plus its text list; VD segmenting)
8. **Signal sparingly.** At most two callouts per screen. Highlight one thing per step. No decorative images, no mascots, no emoji. (VD section 4 and 7)
9. **Progress is plain.** Ticks fire when a card is answered, not when the reader scrolls. A line says "3 of 8 sections done, about 9 min left". No points, no streaks, no loss states. (VD section 6)
10. **Quiet sources, clean voice.** Citations are small monospace chips with literal `path:line` text. No em dashes, no "not X but Y", no hedging words. Tag numbers with an era. (Mayer, coherence principle; era tags are a house rule so old numbers are never read as current)

## Settled decisions (do not reopen)

a. **Commit-first reveal on the page.** Type or pick, then click. The answer is hidden until committed. A full answer key also sits at the end of the page.

b. **Pre-teach only 4 or 5 core terms** in a "Words you will meet" strip. Every other technical term gets a short plain definition inline: a dotted-underline term whose bracketed definition shows on tap (works on phones without hover) and shows in full when JavaScript is off.

c. **Story spine.** The reader is the builder. Each section opens on a small puzzle or problem and ends on an open question the next section answers. No decorative story.

d. **Evidence ratings stay provisional.** The research notes read mostly abstracts and summaries. Treat every effect size as direction, not as a promise. Story, open loops and ADHD layout choices are bets, never proven.

## Pass/fail checklist

Tick each line. One fail means the page goes back.

- [ ] Every card hides its answer until the reader has typed or picked something.
- [ ] The reveal button is disabled while the input is empty.
- [ ] A full answer key sits at the end and covers every card.
- [ ] Only 4 or 5 words are pre-taught at the top. All other terms are defined inline.
- [ ] Every section opens on a puzzle and ends on a question the next section answers.
- [ ] Each story beat carries a fact or reason (delete test passed).
- [ ] Every fact has a chip citation that exists in the source ledger. The citation checker reports 0 bad.
- [ ] Every number carries an era tag. Private material stays tagged and visible.
- [ ] Spoken pitch text contains no work names, no teammate names, no third-party names.
- [ ] Zero em dashes, zero emoji, no "not X but Y", no hedging words.
- [ ] Callouts: at most two per screen. No decorative images.
- [ ] Layout: no horizontal page scroll at 400px, visible keyboard focus, reduced motion respected.
- [ ] Light and dark themes both work, from CSS tokens only, and `body` has an explicit background.
- [ ] The page works with JavaScript off (terms visible, step list visible, answers readable) and with localStorage blocked.
- [ ] A spacing instruction is present (redo the checks tomorrow, in three days, in a week; Cepeda et al. 2006). Reading time sits near 12 to 15 minutes including reveals.

## Design and kit decisions (from the first course, 2026-11-21)

- **Design:** warm paper background in light mode, warm charcoal in dark mode. Cards are one step lighter than the page. One teal accent for "your turn", amber for private, green for done. Open questions are plain lines, not callouts. Citation chips are quiet footnote text. The working example is `kit/template.html`.
- **Type:** Avenir Next for body and headings (a system font on macOS and iOS; no web fonts). Monospace only for code and file paths. Weights 400 and 600, with 700 for the page title only. Measure about 32em.
- **Size:** every font size is in rem, from the browser default (body 1rem). An A−/A/A+ control steps from 75% to 125% and is saved per browser. Text in SVG diagrams uses px (SVG user units), so diagrams scale as a whole and labels never overflow. Text boxes never go below 16px, so iOS does not zoom.
- **Layout (v2):** on screens wider than 860px the section index sits on the left edge of the window and the reading column is centred in the window, as in a browser's reader view. Text stays left-aligned at a fixed 17px base, about 65 to 70 characters per line (34rem). Wide tables and ASCII blocks bleed evenly on both sides of the column, never into the index. The A−/A/A+ control multiplies the base through `--tb-scale`. Phones keep the top-bar index at 16px. `scripts/patch_layout.py` upgrades older pages.
- **Kit:** copy the KIT START / KIT END blocks unchanged between pages. Add new components only after KIT END, built from existing tokens.

## Sources

- Dunlosky, J., Rawson, K., Marsh, E., Nathan, M., and Willingham, D. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest*, 14(1). Practice testing and spaced practice rate high; rereading and highlighting rate low.
- Roediger, H. L. and Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science*, 17(3). Testing yourself beats rereading for later recall.
- Karpicke, J. D. and Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science*, 331.
- Cepeda, N., Pashler, H., Vul, E., Wixted, J., and Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3). Spread repeats out in time.
- Bjork, E. L. and Bjork, R. A. (2011). Making things hard on yourself, but in a good way: creating desirable difficulties. In *Psychology and the Real World*. Effortful recall feels harder and lasts longer.
- Slamecka, N. J. and Graf, P. (1978). The generation effect. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6). Words you produce are remembered better than words you read.
- Paivio, A. Dual coding theory (1971 onward). Words and pictures are stored in two linked channels.
- Mayer, R. E. Multimedia learning (2001; 3rd ed. 2021) and the 2023 summary of principles: coherence, signaling, segmenting, pre-training, personalization.

Most of these were read as abstracts or secondary summaries for this project. Treat every effect as direction, not as a promise.
