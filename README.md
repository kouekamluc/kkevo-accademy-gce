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

## Front-end assets

Built CSS and vendored JS are committed, so Node is only needed when templates change:

```bash
npm install
npm run build        # copies htmx/alpine/flowbite to static/vendor and builds static/css/app.css
npm run watch:css    # rebuild CSS while editing templates
```

## Tests

```bash
.venv/Scripts/python -m pytest
```
