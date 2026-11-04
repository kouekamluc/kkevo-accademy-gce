# Benchmark: practice & assessment

What leading learning products do with practice, what we adopted for GCE Learning Academy, and
what we skipped. Our constraints: Form 5 to Upper Sixth students in Cameroon, mostly phones on slow
or expensive data, server-rendered pages that must work without JavaScript, and a "concepts first"
platform (not a past-paper bank). Notes are from public product behaviour, not internal data.

## What they do well

| Product | Strength | Why it works |
| --- | --- | --- |
| **Khan Academy** | Mastery levels per skill (Not started → Attempted → Familiar → Proficient → Mastered); levels go *down* when a later quiz shows a gap. Hints per question; using one means the item doesn't count toward mastery. | Students see a concrete next goal instead of a raw percentage. Hints keep a stuck learner moving. |
| **Anki / Quizlet** | Spaced repetition: a missed card comes back after a short gap, then longer gaps as you keep recalling it ("Learn" / "Review" modes). Anki asks how hard the recall felt. | Re-testing at growing intervals is one of the best-evidenced ways to make learning stick. |
| **Brilliant** | Every answer, right or wrong, opens a short explanation; wrong answers get an explanation of *that* misconception. | Feedback teaches the concept, not just the score. |
| **Duolingo** | Immediate, warm feedback ("Nice!", "Not quite"), a visible correct answer, mistakes collected into a "Practice mistakes" session. | Low-stakes tone keeps beginners trying; mistakes become the next lesson. |
| **WAEC / JAMB CBT practice apps, GCE past-question apps** | Timed mock exams with a countdown; feedback and score only at the end; offline question packs. | Builds pacing and exam stamina, matches the real paper's conditions. |

Common weaknesses we want to avoid: past-question apps that show only the letter of the right
answer (no reasoning), streak pressure that rewards guessing, heavy media and SPA bundles that are
slow on 3G, and content of unclear origin presented as official.

## What we adopted (built in this round)

1. **Topic mastery levels** (Khan). Not started / Attempted (<60%) / Familiar (60–79%) /
   Proficient (80%+ once) / Mastered (80%+ twice, latest included). Shown on the practice index (per
   card, plus a tally), the set page and the results page, each with the *next step* ("Score 80% or
   more again to reach Mastered"). Levels follow the latest score, so they can drop, like Khan. We
   reused the existing 60/80 marks and the progress page's "80% twice" rule so the numbers agree.
2. **Hints** (Khan). Optional per-question hint, written in the admin. The student opens it before
   answering; it's recorded on the answer (`used_hint`) and shown on the results page. Opening a
   hint is a POST, so it is recorded without JavaScript; HTMX just avoids the reload. Hints are off in
   timed exam mode. We *don't* lower the score for hints yet (see below).
3. **Review my mistakes** (Anki / Quizlet / Duolingo). Every wrong answer creates a review card
   due the next day. A correct review pushes it to 3 days, then 7 days; the next correct review
   retires it. A wrong review resets it to 1 day; a correct review with a hint repeats the same gap.
   Sessions take up to 10 due questions across all subjects and reuse the normal quiz screen with
   full worked solutions. Reachable from the practice index and the results page.
4. **Confidence rating** (Anki's "how hard was it", applied to MCQs). Optional "I'm sure /
   I'm guessing" before checking. A right answer marked as a guess still goes into Review my
   mistakes, because a lucky guess on a 4-option question isn't knowledge.
5. **Numeric-answer questions with tolerance** (Brilliant, and most of O/A Level Physics, Chemistry
   and Maths). Typed answers accept "3600", "3 600" and the decimal comma "3,6" used in
   Francophone Cameroon. Authors set the value, tolerance and unit; the worked solution follows.
6. **Timed exam mode** (WAEC/JAMB CBT apps). 90 seconds a question (5 minutes minimum), countdown
   in the header (plain text without JS), no hints or right/wrong until the student hands in or time
   runs out; answers sent within 15 s of the end still count (slow connections). Unanswered
   questions count as wrong. Afterwards every question shows its full solution.
7. **Feedback tone** (Duolingo/Brilliant): we kept the existing "Correct — nicely done." /
   "Not quite — here's how to get there." with misconception explanations, and added a
   "comes back tomorrow" note so a wrong answer has a clear next action.

## What we skipped, and why

- **Hints reducing mastery credit** (Khan). Fair, but our sets are short (5 questions), so one hint
  would swing a level. Revisit once sets are longer; `Answer.used_hint` already stores what's needed.
- **SM-2 / adaptive algorithms, ease factors** (Anki). A fixed 1/3/7-day ladder is easy to explain to
  a 16-year-old and to a teacher; tuning needs real usage data first.
- **Hearts, XP, leaderboards, streak freezes** (Duolingo). Gamification belongs to the motivation
  area; for assessment it encourages speed and guessing over understanding.
- **Large past-paper banks** (exam-prep apps). We are concepts-first and must not invent or copy
  official papers. Timed mode works on our own practice sets; licensed past papers would need a
  content agreement.
- **Offline question packs** (exam-prep apps). Valuable for our users but needs a service worker and
  sync design across the whole app; out of scope for this area.
- **Free-text / essay marking and AI grading.** Not reliable enough for exam feedback yet.

## Possible next steps

- Show "N reviews due" on the dashboard and in the planner (owned by other areas; data is ready via
  `apps.practice.reviews.review_summary`).
- Per-concept mastery using the existing `Question.concept` tags.
- Exam mode across several sets (a mock paper for a whole subject).
