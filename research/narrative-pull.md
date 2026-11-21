# Narrative pull and curiosity in technical self-study text

Research note, run-01. Scope: what keeps a reader reading, and how to use it in a guide that teaches a builder their own tool. Retrieval practice, spacing, chunking and dual coding are covered in STYLE-GUIDE.md (with published sources) and are not repeated here. Evidence ratings in this note are provisional: most sources were read as abstracts or summaries.

**Source honesty.** Web search returned abstracts and secondary summaries for most items. I fully read only the Mar et al. (2021) meta-analysis (PMC) and Nicky Case's design-patterns post. Everything else was read as search snippets or abstracts. Each finding says which. The "unopened" list is at the end.

Evidence labels: strong / moderate / weak / opinion.

---

## 1. Curiosity comes from a gap, and curiosity helps memory

**Claim.** Curiosity is the felt gap between what you know and what you want to know (Loewenstein 1994). Later work says the gap bites most when you already know a little. Curious people also remember more, including side facts met while curious (Kang et al. 2009; Gruber et al. 2014).

**Evidence.** Gap theory: moderate (influential, mostly lab trivia studies). Curiosity improves memory: moderate. Gruber reported better memory right away and one day later, for the target answers and for incidental items shown during high curiosity. Sample sizes are small (Kang is reported as 19 students, from a secondary source), the tasks are trivia questions, and I did not see a large replication. The "side facts also stick" result is the most useful and the least tested.

**Sources.**
- Loewenstein (1994), Psychological Bulletin 116(1), 75-98. Abstract and citing papers only: https://stafforini.com/works/loewenstein-1994-psychology-curiosity-review/
- Golman and Loewenstein, information-gap paper: https://www.cmu.edu/dietrich/sds/docs/golman/Information%20Gaps--Golman%20and%20Loewenstein.pdf (the PDF would not parse; not read).
- Kang et al. (2009), Psychological Science 20(8): https://pubmed.ncbi.nlm.nih.gov/19619181/
- Gruber, Gelman, Ranganath (2014), Neuron 84(2): https://pmc.ncbi.nlm.nih.gov/articles/PMC4252494 (page blocked; abstract read via search).

**Do this in a guide: ask the question, then make them want the answer.** Open a section with a specific puzzle the reader can almost answer.

> Your tool flagged a SQL injection in a file that has no SQL. Before you read on: what could it have been reading instead? Guess in one line. The answer is two paragraphs down, and it explains why your first rule engine was wrong.

Keep the gap small. A gap about something the reader knows nothing about makes no pull.

## 2. Stories are easier to understand and recall than essays

**Claim.** Narrative text is understood and remembered better than expository text on average.

**Evidence.** Moderate. Mar et al. (2021): 37 articles, 78 samples, 33,078 people. Overall g = .55; memory g = .72; comprehension g = .48. Caveats from the paper: very high heterogeneity (I-squared 98%), signs of publication bias in the memory studies, only 4 studies with delayed tests, and only about 28% controlled the content. So "stories help" is real on average but the size is uncertain, and the evidence for delay is thin. Graesser's work (narratives drive more knowledge-based inferences, via the Mar paper's introduction) supports a mechanism: events give causes, and causes give coherence. I found no source using the phrase "psychologically privileged" and did not verify it.

**Sources.**
- Mar, Li, Nguyen, Ta (2021), Psychonomic Bulletin & Review 28(3), 732-749: https://pmc.ncbi.nlm.nih.gov/articles/PMC8219577 (read)
- Clinton et al. (2020), inferential comprehension g = .36, via ERIC summary: https://files.eric.ed.gov/fulltext/ED618145.pdf (not read in full)

**Do this in a guide: tell the system's history as cause and effect.**

> Version 1 sent every diff to the model. It was slow. So you added a file filter. That filter dropped lockfiles, and the tool missed a bad dependency bump. So you added a second pass.

Each "so" is a cause the reader can recall later in an interview. Note the limit: these studies used stories about people, not stories about code. Whether a build story transfers the same way is untested.

## 3. Story shapes that teach

**Claim.** A usable teaching arc is: problem, stakes, attempts, failure, fix. The reader is the builder. Open loops carry the reader between sections.

**Evidence.** Arc and "reader as hero": practitioner opinion. It matches the cause-and-effect logic in section 2 but I found no study that tests this exact arc on technical text. Cliffhangers and the Zeigarnik effect: **weak**. The classic claim (unfinished tasks are remembered better) did not hold up in the 2025 meta-analysis by Ghibellini and Meier, reported in snippets as about no recall advantage for interrupted tasks, with a more robust Ovsiankina effect (a pull to resume). I could not open the paper (the Bern PDF returned 404) and the effect-size figures differ between secondary sources, so I give no numbers. Practical reading: do not promise that an open loop improves memory. It may still make people want to resume reading, which is all we need here.

**Sources.**
- Ghibellini and Meier (2025), Humanities and Social Sciences Communications (DOI prefix 10.1057/s41599-025-05000-w): https://ideas.repec.org/a/pal/palcom/v12y2025i1d10.1057_s41599-025-05000-w.html (listing only)

**Do this in a guide: end each section on a live question that the next section answers.**

> The tool now catches the bug. But it also flags 40 harmless lines per PR, and your reviewers have started ignoring it. Section 4 is about the one number that quietly decides whether anyone trusts it.

Close the loop in the very next section. A loop left open for ten pages reads as a trick.

## 4. What the best explainers repeat

I could verify only some of this. Labels are practitioner opinion unless stated.

- **Make the reader predict or act.** Nicky Case lists four patterns: "Puzzle it out", "Place your bets" (predict before the reveal), "Role play", and "Sandbox mode" (start small; save the full sandbox for the end). Case also warns that tasks far above the reader's level make them quit. Read in full. Source: https://blog.ncase.me/explorable-explanations-4-more-design-patterns/
- **Active reader.** Bret Victor's 2011 essay frames the reader as someone who explores a model, with attention guided to one phenomenon. Source: https://worrydream.com/ExplorableExplanations/ (snippet only)
- **Interactive articles help modestly.** Hohman et al. (Distill 2020) synthesise design theory; Hohman says in an interview that interactive articles give "a moderate boost in information retention". Evidence: weak to moderate, and one author's own description. https://distill.pub/2020/communicating-with-interactive-articles/ (snippet only)
- **Characters and voice.** Why's (Poignant) Guide uses cartoon foxes and a comic voice to teach Ruby; Head First books say they use stories, informal language and varied formats, citing cognitive science. The Head First claim comes from publisher text and Wikipedia, so treat it as marketing. I found no outcome data for either. https://en.wikipedia.org/wiki/Why%27s_(poignant)_Guide_to_Ruby ; https://www.wikipedia.org/wiki/Head_First_(book_series)
- **Not verified.** Julia Evans: I found her zine-making posts (e.g. https://jvns.ca/blog/2016/08/29/how-i-made-a-zine/) but no post on her explaining method, so I make no claim about her patterns. Ciechanowski: I confirmed only that his essays use many sliders; I found nothing on his method. I did not search Stripe or Increment essays or engineering postmortems at all.

**Patterns that repeat across the sources I did read:** a concrete thing first; the reader does something early; one idea per screen; complexity added in steps.

**Do this in a guide: "Place your bets" before every reveal.**

> Bet first. Your reviewer runs on a 300-line diff. Does it send the whole file, the diff only, or the diff plus 20 lines around it? Write your pick. Check it against the key.

(This also fits the generation effect (Slamecka and Graf, 1978). Put the answer in the key at the end of the page.)

## 5. Introducing jargon

**Claim.** Two approaches conflict, and the evidence supports a mix. Mayer's pre-training principle says learners do better on transfer tests when they first learn the names and parts of the key components (5 of 5 tests, in multimedia lessons). Segmenting (10 of 10 tests, median effect around 0.79) says break lessons into learner-paced pieces. Just-in-time terms are practitioner opinion, with no direct test I found.

**Evidence.** Pre-training and segmenting: moderate (Mayer's own program, mostly animations, not text guides). "Earn the word": opinion.

**Sources.** Mayer chapters, via search summaries only: https://www.cambridge.org/core/books/abs/multimedia-learning/pretraining-principle/01791D57F5D4164251269E6DF56A8BF1 ; https://static.raspberrypi.org/files/curriculum/quickreads/QR33_Mayers_Principles_2_21_05_2026.pdf

**Do this in a guide: name the few core parts early, earn every other word.** A short "meet the cast" box of 4-5 core terms (diff, rule, finding, severity, reviewer) at the start, each with one line. Every other term appears the first time it solves a problem in the story.

> Your tool kept reporting the same issue twice. You needed a way to say "these two are the same finding." That is **deduplication**. The word just names what you built.

**Analogy failure modes.** Analogies help but are "double-edged" (Duit and colleagues, via review summaries): readers carry over features that do not match, and textbooks rarely state where the analogy breaks. Glynn's Teaching-With-Analogies model adds an explicit step: map the parts, then say where it fails. Evidence: moderate and mixed; the learning effect of text analogies is inconsistent. Source: https://chemed.chem.purdue.edu/chemed/bodnergroup/PDF_2008/88%20Orgill%20JRST.pdf (snippet only).

> Think of the severity filter as a bouncer. Where it breaks: a bouncer judges the person at the door, but your filter judges the finding, not the author. Do not say "the tool judges developers" in an interview.

## 6. ADHD readers

**Claim.** Readers with ADHD may find low-stimulation text harder, and may respond more to reward and choice.

**Evidence.** Weak for our purpose. I found no study of narrative or novelty in technical self-study for adults with ADHD. What exists: delay-aversion and reward-circuit theories (theory, not tests of reading); a review of 22 studies (ages 5-14) where external reinforcers affected children with ADHD more than others (task performance, not reading); and two small studies on children, one with 92 children where text choice raised comprehension (not enjoyment) for children with and without inattention, and a 24-child study that was inconclusive. These are children's studies. Applying them to an adult reading a technical guide is my inference.

**Sources.**
- Choice and reading comprehension, 2021: https://link.springer.com/article/10.1007/s10802-021-00835-8 (snippet only)
- Related UCL thesis summary: https://discovery-pp.ucl.ac.uk/10129270/7/Kakoulidou_The%20effects%20of%20choice%20on%20the%20reading%20comprehension%20and%20enjoyment%20of%20children%20with%20severe%20inattention%20and%20no%20attentional%20difficulties_VoR.pdf (snippet only)

**Opinion, clearly marked:** short loops (a win every 2-3 minutes of reading), a visible progress marker, and a choice of next section are sensible bets. They are cheap to try and fit the chunking rule in STYLE-GUIDE.md. Do not claim they are proven for ADHD.

**Do this in a guide: give a progress line and a choice.**

> Part 2 of 6 done: you can explain how a diff becomes a prompt. Next, pick one: (a) why findings get ranked, or (b) how the tool decides it is wrong. About 6 minutes each.

## 7. Where story hurts: seductive details

**Claim.** Interesting but off-topic material lowers learning. Harp and Mayer (1998) proposed it works by diverting readers to the wrong prior knowledge (lightning lesson with an aircraft-strike story). Hurt was larger when the detail came early, per a later summary.

**Evidence.** Moderate to strong that the effect exists and is small to medium. Rey (2012): 39 effects, small-to-medium harm for retention, medium for transfer. Sundararajan and Adesope (2020): reported g about -0.33 over 68 effects from 58 studies (figure from a press summary, not the paper). Reported moderators: worse when the detail sits next to relevant diagrams, worse with limited study time. The meta-analyses measured only cognitive outcomes, not motivation or enjoyment. That gap matters for us: our reader's problem is not finishing at all.

**Sources.**
- Harp and Mayer (1998), J. Educational Psychology 90(3), 414-434, DOI 10.1037/0022-0663.90.3.414 (original not opened; secondary summaries only): https://en.wikipedia.org/wiki/Seductive_details
- Rey (2012), Educational Research Review 7(3), 216-237, DOI 10.1016/j.edurev.2012.05.003 (abstract only): https://www.fachportal-paedagogik.de/literatur/vollanzeige.html?FId=eric_ej986386
- Sundararajan and Adesope (2020), Educational Psychology Review 32(3), 707-734: https://www.e-teaching.org/materialien/literatur/sundararajan-adesope-2020 (summary only)

**Do this in a guide: the story is the facts' delivery vehicle.** Test every story beat: if you delete it, does the reader lose a fact or a reason? If not, cut it or move it after the lesson. Keep jokes and asides off the diagrams and out of the early lines of a section.

> Keep: "The first rule engine failed because it matched text, not meaning." (carries the reason.) Cut: "You built this at 2 a.m. fuelled by cold chai." (no fact.)

---

## Ranked: the 8 most useful patterns

1. **Every story beat must carry a fact or a reason** (cut the rest; section 7).
2. **Cause-and-effect history with "so"** instead of a feature list (section 2).
3. **Bet before the reveal**, answer in the end key (sections 1 and 4).
4. **Open each section with a small, specific puzzle** the reader can nearly solve (section 1).
5. **Close every loop in the next section**; end sections on a live question (section 3).
6. **Pre-teach 4-5 core terms; earn every other word** when it first solves a problem (section 5).
7. **State where each analogy breaks**, in one line (section 5).
8. **Progress line plus a choice of next section**, labelled as a bet, not a proven ADHD fix (section 6).

## Anti-patterns

1. **Decorative stories**: jokes, personal colour or trivia that carry no fact (seductive details).
2. **Cliffhangers that stay open** or that promise payoffs the next page does not deliver. Zeigarnik is weak, and trust is lost fast.
3. **An up-front glossary of 20+ terms.** Too much before any story gives nothing to attach the words to.
4. **Unbounded analogies** with no stated break point; the reader repeats them wrongly in interviews.
5. **Claiming the science is settled.** The guide should not tell the reader that stories, cliffhangers or ADHD tricks are proven. They are bets.

## Sources I could not open

- Loewenstein (1994), full text: abstract and citing papers only.
- Golman and Loewenstein PDF: fetched but unreadable.
- Gruber et al. (2014): PMC page blocked by a browser check; abstract via search.
- Ghibellini and Meier (2025): Bern PDF 404; listing and snippets only. No effect sizes given.
- Harp and Mayer (1998), Rey (2012), Sundararajan and Adesope (2020): abstracts and secondary summaries only; the g = -0.33 figure is from a press summary.
- Springer page for the 2021 ADHD-choice study and the 2023 seductive-details paper: redirect or snippet only.
- Graesser's own papers: not searched directly.
- Julia Evans on explaining, Ciechanowski's method, Stripe/Increment essays, engineering postmortems, Head First outcome data: no usable source found or not searched.
