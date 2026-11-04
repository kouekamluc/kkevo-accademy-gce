# Benchmark: motivation, progress and study planning

Scope: dashboard, My Progress, Study Planner, streaks and goals. Our students are Form 5 to Upper Sixth
(about 15 to 19 years old), mostly on phones with slow or expensive data, and many will never see a push
notification. We copy what builds a steady study habit and leave out anything that works by guilt, fear of
loss or endless engagement.

## What the products do well

| Product | Strong ideas | Weak or risky ideas for us |
|---|---|---|
| **Duolingo** | A streak counted in days, with a small daily goal. Streak freeze protects the streak on a missed day. A weekly progress email. The goal is easy to change. | Streak loss is framed as a threat, with guilt-trip notifications. Freezes and repairs cost gems you can buy. Leagues and leaderboards push compulsive use. Hearts and lives punish mistakes. |
| **Khan Academy** | Mastery goals tied to course content. Assignments with due dates. A parent or teacher view of the student's real activity (minutes, skills, completions). Energy points stay a minor feature. | Parent accounts mean another sign-up flow. Many reports are made for teachers and are dense. |
| **Google Calendar / Notion** | Recurring events ("Mon/Wed/Fri 17:00"). Editing "this event" or "this and following events". Reminders on the phone that work offline once synced. Subscribe by URL (iCal). | Generic: no idea of syllabus or pace. Notion's planning templates take setup time. |
| **MyStudyLife** | Timetables built around school weeks. Exam entries with a countdown. Tasks tied to subjects. | Separate app, so students type the same data twice. Exams are just events, with no link to how much content is left. |
| **Forest** | One focused session gives one visible reward. Skipping a day costs nothing. Calm visuals. | The "tree dies" if you leave the app: loss-framing again. |
| **Habitica** | Rewards come from real habits you set yourself. Rest is built in ("Rest in the Inn" pauses damage). | Damage, HP and RPG punishment loops. Heavy gamification that can crowd out the real work. |

## What we adopted

1. **Exam countdown with a pace you need** (MyStudyLife's exam countdown plus Khan's content-based goals).
   The student enters the date of their first GCE paper, copied from their official timetable. We never
   ship exam dates ourselves. Dashboard and planner show the days left, the lessons left in their own plan,
   and the weekly and daily pace to finish **two weeks before the exam, leaving time for revision**. We
   compare that pace with the last 14 days and give a calm "on track" or "a few short extra sessions will
   close the gap".
2. **Recurring sessions and editing** (Google Calendar). "Repeat on Mon/Wed/Fri for N weeks" creates a
   series. A session can be edited on its own or together with all later sessions in its series; later
   sessions keep their own days. "Delete this and later sessions" works the same way.
3. **Private calendar feed (.ics)** (Google Calendar / iCal subscriptions). This is our answer to "no push
   notifications": the student subscribes once in Google Calendar or their phone calendar, and every session
   comes with a 15-minute reminder that the phone's own calendar shows, even offline. The exam date is
   included as an all-day event. The URL holds a secret token: the student can rotate it (the old URL stops
   working) or switch it off.
4. **Rest days instead of streak freezes** (Duolingo freeze, Habitica's inn, Forest's no-penalty skip).
   One planned rest day per week, for today or a later date, never backdated. A rest day neither adds to
   nor breaks the streak. It is free and needs no tokens to earn. The copy says "Tired? Take one rest day a
   week", not "Don't lose your streak!".
5. **Weekly summary shareable with a parent or guardian** (Duolingo's weekly report plus Khan's parent
   view, without a parent account). "Your week" shows minutes per day, days active, days the goal was
   reached, lessons completed, practice, and planned sessions done, with up to 8 weeks of history. The
   student can create a private, revocable read-only link and send it on WhatsApp. The page shows the
   first name only (no email), sends no-index and no-referrer headers, and tells the parent the student can
   switch it off.
6. **Goal-adjust suggestions** (Duolingo's easy goal change). Based on the last 14 days: if the goal was
   reached on 12 or more days, we suggest +10 min, never nudging above 2 h a day. If the student studied
   often but rarely reached the goal, we suggest -10 min, because "a goal you can keep builds the habit".
   The student applies it with one tap. The server works out the new value itself and ignores any value
   sent from the page.

## What we skipped and why

- **Leaderboards, leagues, XP or coins.** They compare teenagers with each other and reward time spent in
  the app rather than learning. Our progress numbers measure the syllabus covered.
- **Paid or earned streak freezes and streak repair.** Monetising anxiety is a dark pattern. Rest days are
  free and limited to keep the habit honest, not to sell anything.
- **Loss-framed copy and guilt notifications** ("Your streak is about to die!"). We never message the
  student about a broken streak. The streak chip simply shows the current number.
- **Hearts/lives and HP damage** (Duolingo, Habitica). Penalties for mistakes discourage practice before
  exams.
- **Achievement badges for now.** Badges are only healthy when they come from real milestones (module
  finished, topic mastered). The practice and analytics agent owns mastery, so badges should be built on
  top of that once it lands. It is a good next step.
- **Parent accounts.** A link is lighter for families on shared phones and needs no sign-up. It can be
  revoked, and it shows nothing beyond what the student already sees.
- **Push or email reminders.** Many students don't get them reliably, and the calendar feed gives
  reminders through the phone's own calendar at no extra data cost.
