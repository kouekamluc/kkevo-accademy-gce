# Running KKEVO Academy in Docker

The image is the production build: gunicorn behind WhiteNoise, `DEBUG` off, hashed and compressed static files,
the Tailwind stylesheet and front-end libraries rebuilt from source. Development still uses `runserver`
(see the README); Docker is for trying the real build and for hosting.

## On your machine

```powershell
docker compose up --build -d
```

Open http://localhost:8000. The first start creates the database tables. The database is empty until you load
the curriculum, lessons and practice sets once (a few minutes; safe to repeat, nothing existing is overwritten):

```powershell
docker compose exec web sh -c "python manage.py load_gce_curriculum && python manage.py load_lessons && python manage.py load_practice"
```

(On a host you can instead set `LOAD_CONTENT=1` for one start; the container then loads the content before
it begins serving.)

Then create a staff account:

```powershell
docker compose exec web python manage.py createsuperuser
```

Useful commands:

| What | Command |
|---|---|
| Follow the app's logs | `docker compose logs -f web` |
| Is it healthy? | `docker compose ps` (the app reports `healthy` once `/healthz/` answers) |
| Any management command | `docker compose exec web python manage.py <command>` |
| Stop (keeps the data) | `docker compose down` |
| Stop and **delete** the database and uploads | `docker compose down -v` |
| Use another port | `$env:WEB_PORT = "8100"; docker compose up -d` |

`docker-compose.yml` is for local use only: it serves plain http, so it turns the HTTPS redirect and secure
cookies off, and it has a throwaway secret key and database password. Emails (password reset) are printed in
the logs instead of being sent.

## On a host

Build and run the image with the environment variables listed in `docs/DEPLOYMENT.md`, against the host's
PostgreSQL:

```sh
docker build -t kkevo-academy .
docker run -d -p 8000:8000 --env-file production.env -v kkevo-media:/app/media kkevo-academy
```

- **HTTPS** is ended by the host's proxy or load balancer, which must send `X-Forwarded-Proto`. Leave
  `DJANGO_SECURE_SSL_REDIRECT` and `DJANGO_SECURE_COOKIES` at their defaults (on).
- **On start** the container waits for the database (up to two minutes), runs `migrate` and creates the cache
  table. Set `MIGRATE_ON_START=0` to run migrations yourself instead, for example as a release step:
  `docker run --rm --env-file production.env kkevo-academy python manage.py migrate`.
- **Several workers**: gunicorn starts 3; set `CACHE_URL=dbcache://django_cache` (or Redis) so login rate
  limits are shared. Change the worker count by overriding the command:
  `... kkevo-academy gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 5`.
- **Health check**: the image checks `/healthz/` itself; point the host's check at the same path.
- **Uploaded files** live in `/app/media` and are not served by the app when `DEBUG` is off. See
  `docs/DEPLOYMENT.md` (object storage or a web server in front).
- **Study reminders**: schedule `python manage.py send_reminders` every hour, as a cron job that runs
  `docker exec <container> python manage.py send_reminders` or as the host's scheduled task.
