# GCE Learning Academy — Django platform

Learning platform for the Cameroon GCE curriculum (Form 5, Lower Sixth, Upper Sixth).
Architecture, schema and milestones: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

The `0x-*.html` files in this folder are the approved design mockups (visual reference only).

## Setup (Windows, Git Bash)

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
cp .env.example .env          # then edit: DJANGO_SECRET_KEY, DATABASE_URL
```

### PostgreSQL

```sql
CREATE USER gce_user WITH PASSWORD 'choose-a-password';
CREATE DATABASE gce_academy OWNER gce_user;
```

Set `DATABASE_URL=postgres://gce_user:choose-a-password@localhost:5432/gce_academy` in `.env`.
If `DATABASE_URL` is not set, a local SQLite file is used (handy for a first look, not for real data).

```bash
.venv/Scripts/python manage.py migrate
.venv/Scripts/python manage.py createsuperuser
.venv/Scripts/python manage.py runserver
```

Landing page: http://127.0.0.1:8000/ · Admin: http://127.0.0.1:8000/admin/

## Sample content (optional)

The mockups' sample data (Form 5 Mathematics outline, three full demo lessons, a physics
practice set) can be loaded to review every screen. It is **not** official GCE syllabus content.

```bash
.venv/Scripts/python manage.py seed_demo --with-student   # prints a one-time demo password
.venv/Scripts/python manage.py seed_demo --remove
```

## GCE curriculum outline

`load_gce_curriculum` loads every GCE subject and level from
`apps/academics/gce_curriculum.py` (KKEVO's summary in `docs/curriculum/GCE_CURRICULUM_GUIDE.md`).
Syllabi are saved as **unofficial drafts** (`is_official=False`). Each one also gets a draft course
outline with modules and topics but no lessons. The data is validated first: if anything is
wrong, every problem is listed and nothing is written. The command is safe to run twice, and it
never overwrites existing subjects, offerings or courses.

```bash
.venv/Scripts/python manage.py load_gce_curriculum --dry-run   # validate and report, save nothing
.venv/Scripts/python manage.py load_gce_curriculum
.venv/Scripts/python manage.py load_gce_curriculum --remove    # keeps outlines that already have lessons
```

Check each syllabus against the official GCE Board text before publishing anything built on it.

## Draft lessons

`load_lessons` loads KKEVO's draft lessons (one per syllabus topic, in
`apps/courses/lesson_content/`) into the GCE outline courses. They are created as **drafts**:
staff check each one against the official syllabus and publish it in the studio. How to write
lessons: [docs/curriculum/LESSON_AUTHORING.md](docs/curriculum/LESSON_AUTHORING.md).

```bash
.venv/Scripts/python manage.py check_lessons            # validate the content files, no database
.venv/Scripts/python manage.py load_lessons             # create the missing drafts
.venv/Scripts/python manage.py load_lessons --refresh   # rewrite drafts nobody has edited in the studio
.venv/Scripts/python manage.py check_practice           # validate the practice-set files
.venv/Scripts/python manage.py load_practice            # create the missing draft practice sets
```

## Main URLs

| Page | URL | Mockup |
|---|---|---|
| Landing | `/` | 01 |
| Register → onboarding wizard | `/accounts/register/` | 07 |
| Dashboard | `/dashboard/` | 02 |
| Explore subjects | `/subjects/` | 08 |
| Course overview | `/courses/<slug>/` | 03 |
| Lesson (reading / interactive / video) | `/courses/<slug>/lessons/<id>/` | 04 / 05 / 06 |
| Practice | `/practice/` | 09 |
| My progress | `/learn/progress/` | 10 |
| Study planner | `/learn/planner/` | 11 |
| Content studio (staff) | `/studio/` | 12 |
| Django admin (staff) | `/admin/` | — |

Studio permissions: staff need `courses.change_lesson` to edit; publishing/archiving also
needs `courses.publish_lesson` (give it to reviewers). Superusers have both.

## Front-end assets

Built CSS and vendored JS are committed, so Node is only needed when templates change:

```bash
npm install
npm run build        # copies htmx/alpine/katex/fonts to static/vendor and builds static/css/app.css
npm run watch:css    # rebuild CSS while editing templates
```

## Tests

```bash
.venv/Scripts/python -m pytest
```
