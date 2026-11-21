#!/bin/sh
# Runs before the app starts: wait for PostgreSQL, apply migrations, make sure the shared cache table exists.
# LOAD_CONTENT=1 also loads the GCE curriculum, lessons and practice sets (safe to repeat: existing ones are kept).
set -e

python - <<'EOF'
import os, sys, time
import psycopg
url = os.environ.get("DATABASE_URL", "")
for attempt in range(60):
    try:
        psycopg.connect(url, connect_timeout=3).close()
        sys.exit(0)
    except Exception as error:
        if attempt == 0:
            print(f"Waiting for the database ({error.__class__.__name__})...", flush=True)
        time.sleep(2)
print("The database did not answer within two minutes.", file=sys.stderr)
sys.exit(1)
EOF

if [ "${MIGRATE_ON_START:-1}" = "1" ]; then
    python manage.py migrate --noinput
    python manage.py createcachetable
fi

if [ "${LOAD_CONTENT:-0}" = "1" ]; then
    python manage.py load_gce_curriculum
    python manage.py load_lessons
    python manage.py load_practice
fi

exec "$@"
