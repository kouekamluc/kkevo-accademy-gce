# KKEVO Academy: production image (Django + gunicorn). See docs/DOCKER.md.
#
#   docker compose up --build          # app on http://localhost:8000 with its own PostgreSQL
#   docker build -t kkevo-academy .    # image only, for a host that provides PostgreSQL

# ---- 1. Front-end: KaTeX, fonts, htmx, Alpine and the Tailwind stylesheet ----------------------------
FROM node:22-alpine AS assets
WORKDIR /build
COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund
# Tailwind scans the templates and the apps' Python files for class names.
COPY tailwind.config.js ./
COPY scripts ./scripts
COPY static ./static
COPY templates ./templates
COPY apps ./apps
RUN npm run build

# ---- 2. Python app --------------------------------------------------------------------------------------
FROM python:3.13-slim AS app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
# Built front-end files from stage 1 replace the copies in the repository.
COPY --from=assets /build/static/css ./static/css
COPY --from=assets /build/static/vendor ./static/vendor

# Hashed, compressed static files for WhiteNoise. Settings need a database URL and a key to load;
# collectstatic never connects, so placeholders are enough here.
RUN DJANGO_DEBUG=False DJANGO_SECRET_KEY=build-only DATABASE_URL=postgres://build:build@localhost:5432/build \
    python manage.py collectstatic --noinput \
 && useradd --create-home --uid 10001 kkevo \
 && mkdir -p /app/media \
 && chown -R kkevo:kkevo /app/media \
 && chmod +x docker/entrypoint.sh
USER kkevo

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/healthz/', timeout=4).status == 200 else 1)"
ENTRYPOINT ["docker/entrypoint.sh"]
CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "60", \
     "--access-logfile", "-", "--forwarded-allow-ips", "*"]
