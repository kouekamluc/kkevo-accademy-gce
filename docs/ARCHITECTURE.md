# KKEVO Academy — Architecture (Phase 2)

## Design reference

The visual source of truth is the Claude Design export in this folder:

| Mockup | Used for |
|---|---|
| `01-landing*.html` | Public landing page (`core`) |
| `02-dashboard*.html` | Student dashboard (`dashboard`) |
| `03-subject-overview*.html` | Course overview (`courses`) |
| `04/05/06-*.html` | Lesson player — later phase |
| `../design-system/tailwind.config.js`, `tokens.css` | Tailwind theme (copied into `tailwind.config.js`) |

Not yet designed (built in the same visual language, kept minimal): onboarding,
subject catalog, auth pages, profile.

## Stack

Django 5.2 · PostgreSQL (via `DATABASE_URL`) · Django templates · Tailwind CSS 3 +
Flowbite (built with the Tailwind CLI, output committed to `static/css/app.css`) ·
HTMX + Alpine.js served locally from `static/vendor/` (no CDN — low-connectivity users).

No REST API, no SPA framework.

## Project layout

```
code/
├── config/              settings, urls, wsgi/asgi
├── apps/
│   ├── core/            abstract base models, landing page, shared template tags
│   ├── accounts/        custom User, StudentProfile, auth + profile views
│   ├── academics/       levels, pathways, subjects, offerings, syllabi, curriculum refs
│   ├── courses/         course → module → topic → lesson → content block
│   └── dashboard/       student dashboard, enrolments
├── templates/           base layouts + shared partials (components/)
├── static/src/          Tailwind input CSS
├── static/css/app.css   built CSS (committed)
├── static/vendor/       htmx, alpine, katex, self-hosted fonts (committed)
└── tests live in each app's tests/ package (pytest-django)
```

## Database schema

```
accounts.User (AbstractUser, email = login)
  └─1:1─ accounts.StudentProfile  level → AcademicLevel · pathway → AcademicPathway
                                  low_data_mode · onboarded_at   (auto-created by post_save signal)

academics.AcademicLevel      code(F5/L6/U6) unique · name · slug unique · exam_level(O/A) · order
academics.AcademicPathway    name unique (Arts, Science) · slug unique · order
academics.Subject            name unique · slug unique · icon_text · accent · order
academics.SubjectOffering    subject → Subject · level → AcademicLevel · pathways ⟷ AcademicPathway
                             UNIQUE(subject, level)
academics.Syllabus           offering → SubjectOffering · title · version · year · is_official
                             effective_from/to · source_url · status   UNIQUE(offering, version)
academics.CurriculumReference syllabus → Syllabus · parent → self · code · title · order
                             UNIQUE(syllabus, code)

courses.Course               offering → SubjectOffering · title · slug unique · summary
                             description · learning_outcomes · status(draft/published/archived)
courses.Module               course → Course · title · summary · order     UNIQUE(course, title)
courses.Topic                module → Module · title · order · curriculum_refs ⟷ CurriculumReference
                             UNIQUE(module, title)
courses.Lesson               topic → Topic · title · slug · lesson_type · estimated_minutes
                             status · order · curriculum_refs ⟷ CurriculumReference
                             UNIQUE(topic, slug)
courses.LessonBlock          lesson → Lesson · block_type · title · body · media_url
                             data(JSON) · order
```

Every ordered model inherits `core.OrderedModel` (`order` PositiveIntegerField,
`Meta.ordering = ["order", "pk"]`). Order is deliberately **not** unique so that
reordering in the admin never fails on a temporary collision; ties fall back to pk.

### Why this stays generic

All pages resolve content by slug/pk (`/subjects/`, `/courses/<slug>/`,
later `/courses/<slug>/lessons/<pk>/`). A new subject, course or lesson is a new
row, never a new route or template. Lesson bodies are a list of typed
`LessonBlock`s rendered by one block-type → partial mapping.

### Syllabus mapping and versioning

`Syllabus` holds a versioned syllabus per subject offering (e.g. "2024 revision").
`CurriculumReference` holds the hierarchical items of that syllabus (codes as
written by the exam board). Topics and lessons link to references many-to-many,
so content can be re-mapped when a new syllabus version is published without
touching the content. **No official syllabus content is seeded** — references
are entered by staff from official documents (`is_official` flags the source).
`manage.py load_gce_curriculum` loads KKEVO's own curriculum summary
(`apps/academics/gce_curriculum.py`) as unofficial draft syllabi plus empty draft course
outlines whose topics link to the matching references. It validates the data first, against
model field lengths and choices, duplicates, and unknown levels or pathways.

## Milestones

1. ✅ Foundation — project, custom user, academic + course models, admin, landing (01)
2. ✅ Accounts — register, login, logout, profile, password change
3. ✅ Onboarding wizard (07) and enrolments
4. ✅ Explore subjects (08), course overview (03), my subjects, learning data model
5. ✅ Lesson player: reading (04), interactive (05), video (06)
6. ✅ Dashboard (02)
7. ✅ Practice quiz (09)
8. ✅ My progress (10), study planner (11), saved lessons
9. ✅ Content studio (12) with review workflow

## Apps added after phase 2 planning

- `learning` — Enrollment, LessonProgress, DailyActivity, SavedLesson, LessonNote, StudySession;
  `services.py` (progress maths), `analytics.py` (progress page / planner)
- `practice` — PracticeSet, Question, Choice, Attempt, Answer; MistakeCard, ReviewSession, ReviewAnswer
  (spaced "Review my mistakes"), `mastery.py` (topic levels). See docs/benchmarks/practice-assessment.md
- `studio` — staff lesson list, block editor, overview, media library. Models: `LessonDraft` (unpublished
  working copy of a published lesson's blocks), `LessonRevision` (block snapshots for history/restore),
  `LessonEvent` (audit log + review comments), `MediaAsset` (validated image uploads). See
  `apps/studio/revisions.py` and `docs/benchmarks/content-studio.md`.

## Known gaps

- Offline downloads, phone-number sign-up, Google sign-in and push notifications are shown in the mockups
  but not built. Studio image uploads exist (media library); production must serve `MEDIA_ROOT` itself.
- Lesson *settings* (title, objectives…) of a published lesson still change immediately; only blocks are
  staged as draft changes. Django admin edits to blocks of published lessons are locked except for superusers.
- Login rate limiting is per process unless `CACHE_URL` points to a shared cache.
- Benchmarks behind the five improvement branches: `docs/benchmarks/`.
