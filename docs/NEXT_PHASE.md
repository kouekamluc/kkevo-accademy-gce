# Next phase: finish MVP 1 ("The Digital Classroom") and get pilot-ready

Written 2026-11-05 after checking the whole `kkevo accademy` folder against the 18-feature roadmap.

## What the folders contain

| Folder | What it is | Needed for the build? |
|---|---|---|
| `claude designs/code/` | The real Django platform (this repo) | Yes, this is the product |
| `claude designs/code/0x-*.html`, `design-system/`, `screenshots/` | Approved mockups and tokens | Visual reference |
| `claude designs/design-source/` | Claude Design canvas sources | Only to edit mockups |
| `claude designs/code/docs/curriculum/GCE_CURRICULUM_GUIDE.md` | KKEVO's curriculum summary | Loaded by `load_gce_curriculum` (unofficial drafts) |
| `antigravity design/` | An earlier, smaller Django build (Phase 2 only) | No, superseded by this repo |
| `gpt designs/` | Alternative mockup PNGs | No |

## Roadmap status

Features 1–8, 10–14 and 16 are built. Feature 15 (curriculum import) was committed in `e7d19da`.
What is left for MVP 1 and the pilot, in order:

| # | Work | Why now | Status |
|---|---|---|---|
| 1 | **Feature 9: video & resource library** | Roadmap acceptance test: an approved video appears in its lesson, an unapproved one stays hidden. Before this, a video block was just a URL with no source, rights or review. | Done |
| 2 | **Run the suite on PostgreSQL** | SQLite ignored column lengths and some constraints. PostgreSQL is now the only database: the SQLite fallback was removed and `DATABASE_URL` is required. | Done: 288 tests pass on PostgreSQL 17.5 at `db71d37` (run with `DATABASE_URL` set to PostgreSQL and `--create-db`) |
| 3 | **Feature 17: measure the lesson pages** | Page weight and request count of dashboard, course and lesson pages on a throttled 3G profile; fix the heaviest. | Done (`fe72357`; `manage.py measure_pages`, `docs/benchmarks/page-weight.md`) |
| 4 | **First real module: Form 5 General Mathematics** | One excellent, reviewed module (e.g. Quadratic functions & equations) is the first thing worth showing students. Since `9c39360` / `db71d37` there are 115 draft lessons and 115 draft practice sets (AI-assisted, loaded by `load_lessons` / `load_practice`) across the 13 outline courses, all hidden from students. They must be checked against the official GCE syllabus, corrected and published by a reviewer, one module at a time; nothing is published automatically. | Drafts exist; needs your review (start with one Form 5 Maths module) |
| 5 | **Feature 18: deployment** | Production settings, hosting, backups, error monitoring. Start close to the pilot (after April 2027) so hosting is not paid for early. | Later |

## Feature 9 design

- `courses.VideoResource`: title, kind (NotebookLM, original, YouTube, other), URL, source, creator,
  rights status and licence note, duration, topics, captions, low-data copy, transcript, and a review
  status (pending / approved / rejected) with reviewer and date.
- A video block points to a library video by id in `data["resource"]` (not a foreign key), so the
  studio's JSON drafts and revisions keep working unchanged.
- Students only see a library video when it is **approved** and its rights are known. Otherwise the
  block is hidden. Staff previews show it with a "hidden from students" notice.
- Approving needs the existing `courses.publish_lesson` permission (the same people who publish lessons).
- YouTube links play through `youtube-nocookie.com` embeds. Other links play in the normal video player.
