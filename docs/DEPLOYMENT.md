# Going live: checklist

What the code already provides, and what a person still has to do. Work through it in order.
Deployment is planned close to the pilot (see `NEXT_PHASE.md`), so hosting is not paid for early.

## Already in the code

- **Production switch:** `DJANGO_DEBUG=False` turns on the HTTPS redirect, secure cookies, WhiteNoise hashed and
  compressed static files, gzip for pages and the SMTP email backend (`config/settings.py`).
- **Legal pages:** `/terms/`, `/privacy/` and `/contact/`, linked from the footer. Sign-up has a required box
  "I accept the Terms of use and the Privacy policy"; the date is saved in `StudentProfile.terms_accepted_at`.
- **Report a mistake:** a form under every lesson and practice question. Staff work through the reports in the
  studio under *Workspace → Student feedback* (mark them fixed, or not a problem).
- **Who checked it:** each lesson shows "Checked by …" when it has a reviewer, and "A teacher has not checked
  this lesson yet" when it has none. Publishing in the studio records the reviewer.
- **Usage:** *Workspace → Usage* in the studio shows active students, sign-ups, lessons finished, practice and
  where students stop, for the last 7 or 30 days.
- **Health check:** `GET /healthz/` answers `ok` only when the database responds (503 otherwise). It is exempt
  from the HTTPS redirect. Point the host's health check and an uptime monitor (for example UptimeRobot) at it.
- **Search engines:** `/robots.txt` hides the admin, studio, account and student pages; `/sitemap.xml` lists
  the public ones.
- **Logs and errors:** logs go to stdout. Set `SENTRY_DSN` and errors are sent to Sentry, without personal data.
- **Login protection:** failed logins and password-reset requests are rate limited.

## Environment variables (set them on the host, never commit them)

| Variable | Value |
|---|---|
| `DJANGO_SECRET_KEY` | A new long random string (50+ characters). |
| `DJANGO_DEBUG` | `False` |
| `DJANGO_ALLOWED_HOSTS` | Your domain(s), comma separated. |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | `https://your-domain` |
| `DATABASE_URL` | The production PostgreSQL URL. |
| `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL` | An SMTP provider, so password-reset and reminder emails arrive. Set up SPF and DKIM for the sender domain so they do not land in spam. |
| `SITE_BASE_URL` | `https://your-domain` (used for links inside emails). |
| `CONTACT_EMAIL`, `CONTACT_WHATSAPP` | Real contact details for `/contact/`. WhatsApp in international format, digits only (e.g. `2376XXXXXXXX`). Leave empty until they exist. |
| `SENTRY_DSN` | From sentry.io (optional, recommended). |
| `DJANGO_HSTS_SECONDS` | Start with `3600`; raise to `31536000` once everything works over HTTPS. |
| `DJANGO_TRUSTED_PROXY_COUNT` | `1` when the host puts one proxy in front of the app (needed for correct rate limiting). |
| `CACHE_URL` | A shared cache (`dbcache://django_cache` after `createcachetable`, or Redis) when running more than one worker. |

## Deploy steps

With Docker, the image does steps 1, 2, 3 and 4 itself (see `docs/DOCKER.md`); do steps 5 to 9 as written.
Without Docker:

1. `pip install -r requirements.txt` and `npm ci && npm run build` (vendor files and CSS).
2. `python manage.py collectstatic --noinput`
3. `python manage.py migrate`
4. Start with `gunicorn config.wsgi` (gunicorn does not run on Windows; use a Linux host).
5. `python manage.py createsuperuser`, then give staff the roles they need.
6. Load the curriculum, lessons and practice (`load_gce_curriculum`, `load_lessons`, `load_practice`). The
   loaders refresh the database statistics themselves.
7. Schedule `python manage.py send_reminders` to run every hour (the host's cron or scheduler).
8. Run `python manage.py check --deploy`. It should report nothing except HSTS while you are still on `3600`.
9. Open `/healthz/` and the site on a phone over mobile data.

## Not covered by the code: do these as well

- **Uploaded files.** `MEDIA_URL` is served only when `DEBUG` is on. If staff upload images or PDFs in
  production, use object storage (S3, Cloudflare R2, Backblaze) or a host volume served by the web server,
  or those files will not load.
- **Backups.** Turn on automatic PostgreSQL backups at the host, keep at least 7 days, and **practise
  restoring one** into a test database.
- **Domain and HTTPS.** Buy the domain, point it at the host, and confirm the certificate renews by itself.
- **Legal review.** Have a lawyer in Cameroon read `templates/core/terms.html` and `privacy.html` (plain-language
  drafts that describe what the app does). Update `LEGAL_UPDATED` in `apps/core/views.py` when the wording changes.
- **Content review.** Work through `docs/curriculum/REVIEW_CHECKLIST.md` (see `docs/CONTENT_REVIEW.md`). Lessons
  show "not checked yet" until a teacher has reviewed and published them.
- **Real-device test** on cheap Android phones with slow data: sign-up, a lesson, a practice set, installing
  the app, offline lessons.
- **Someone reads the reports.** A named person checks *Student feedback* every few days, or students stop
  sending them.
