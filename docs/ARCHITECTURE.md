# GCE Learning Academy — Architecture (Phase 2)

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
├── static/vendor/       htmx, alpine, flowbite (committed)
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

## Milestones

1. ✅ **Foundation** — project, settings, custom user, academic + course models,
   admin, Tailwind build, base layouts, landing page (DB-driven), tests.
2. ✅ **Accounts & onboarding** — register / login / logout / profile, StudentProfile,
   level + pathway selection.
3. **Catalog & course overview** — subject catalog with HTMX filters, course page
   with ordered modules/topics/lessons.
4. **Dashboard** — enrolments, enrolled subjects, continue-learning, empty states.
5. **Polish** — mobile bottom bar, accessibility pass, PostgreSQL verification.
