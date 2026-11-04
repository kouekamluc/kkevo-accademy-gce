# Lesson experience — benchmark

How five well-known learning products structure a lesson, and what KKEVO adopts for
Cameroon GCE students (Form 5 – Upper Sixth) who mostly learn on phones with slow,
expensive data. Based on the public product experience of each platform (late 2026);
it describes patterns, not internal details.

## What they do well

| Product | Lesson shape | In-lesson checks & hints | Resume / progress | Low-data / offline | Notes & accessibility |
|---|---|---|---|---|---|
| **Khan Academy** | Short video or article, then an exercise set ("practice to mastery") | Every exercise has step-by-step **hints** you reveal one at a time; using a hint costs mastery credit but never blocks you. Wrong answers get a short explanation | Remembers video position; course map shows mastery levels | Text articles are light; videos stream adaptively; downloadable on the mobile app | Captions and transcripts on every video, keyboard-navigable exercises, screen-reader friendly maths |
| **Brilliant** | Many tiny interactive steps, one idea per screen | Each step is a question; wrong answers show **targeted feedback for that specific choice**, then an explanation; "Why?" expanders | Saves progress per step; reopening drops you on the step you left | Mostly vector/interactive, no heavy video | Little long-form notes; strong visual explanations |
| **BBC Bitesize** | Revision guide split into short pages + a test | End-of-guide quiz with answers explained | Not really session-based | Pages are lightweight HTML; works on poor connections; **print-friendly** revision pages | Excellent plain language, clear headings, accessible markup |
| **Coursera** | Week → module → video/reading/quiz items | Ungraded in-video quiz pop-ups, graded quizzes | "Resume" button goes to the exact item; video resumes at timestamp | Download videos and readings in the app; low-quality video setting | **Notes** taken on video/transcript, saved highlights, **keyboard shortcuts** in the player, transcripts |
| **uLesson** (Africa, WAEC/NECO) | Animated video lessons per syllabus topic, then quizzes and past questions | Quizzes after lessons with solutions | Tracks watched lessons per subject | Built for low connectivity: content shipped on **SD card / tablet** or downloaded once, then fully offline | Simple navigation designed for secondary students on Android phones |

## What we adopt

1. **Resume where you stopped** (Coursera, Brilliant). The player already reports the
   section in view; it now also stores the section's anchor (`LessonProgress.position_anchor`).
   Reopening an unfinished lesson shows *"Continue from &lt;section&gt;"*; one tap scrolls
   there. The sidebar "Continue learning" link scrolls automatically (`?resume=1`).
   Video lessons say where playback resumes and offer "Start over".
2. **Low-data mode that really saves data** (uLesson, Coursera low quality). With low-data
   mode on, images, videos and embeds are not requested at all: each is a small placeholder
   showing the caption/alt text and a "Load" button. The real element lives inside a
   `<template>`, so the browser fetches nothing until the student asks. A lighter
   `low_data_url` video is used when the author provides one.
3. **Notes on every lesson type** (Coursera). Reading and interactive lessons get a notes
   panel (slide-over drawer, works on phones). Each note remembers the section the student
   was reading, so it shows "Completing the square" and links back to it. Notes can be deleted.
4. **Hints and per-choice feedback on quick checks** (Khan Academy, Brilliant). A quiz block
   can carry `data.hint` and `data.feedback` (one line per choice). "Get a hint" is optional;
   after a wrong answer the student sees why *that* choice is wrong; after two wrong tries
   "Show answer" appears so nobody is stuck.
5. **Print / save-as-PDF view** (BBC Bitesize). Print styles drop navigation, sidebars and
   buttons, and expand hidden practice answers. Students can print at a cyber café or save a
   PDF once and revise offline for free.
6. **Keyboard shortcuts** (Coursera, Khan Academy) for students on shared laptops: `j`/`k`
   next/previous section, `n`/`p` next/previous lesson, `c` continue, `w` notes, `?` help.
   Ignored while typing.

## What we skip (for now) and why

- **Full offline downloads / service-worker caching** (uLesson, Coursera app). The highest
  value for our users, but it needs a caching strategy, storage limits and sync of progress
  and notes. Print-to-PDF covers part of the need cheaply; offline is a separate project.
- **Adaptive mastery scoring** (Khan Academy). Needs a large question bank per topic; the
  practice area owns scoring.
- **Brilliant-style one-step-per-screen lessons.** Each step is a round trip or a heavy
  client app; long scrolling pages with inline checks load once and work better on 3G.
- **Transcript-synced highlights and social notes** (Coursera). Notes stay private and
  plain text — cheap to store and to sync later.
- **Mastery cost for hints.** Quick checks are formative and unscored; hints are free.
