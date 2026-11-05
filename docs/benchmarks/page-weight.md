# Student page weight

Measured with `python manage.py measure_pages` as the demo student, first visit (empty cache), static files gzip-compressed as WhiteNoise serves them. Third-party files (e.g. Google Fonts) are not in the byte totals but cost an extra connection each. Estimated load time assumes slow 3G (400 kbit/s, 400 ms round trip).

| Page | HTML (gzip) | Inline JS | Static files (gzip) | **Total (gzip)** | Requests | Third-party hosts | DB queries | Server ms | **Est. slow 3G** |
|---|---:|---:|---:|---:|---:|---|---:|---:|---:|
| Landing | 5.9 KB | 0.0 KB | 93.1 KB | **99 KB** | 5 | none | 8 | 64 | **2.8 s** |
| Explore subjects | 6.4 KB | 0.0 KB | 93.1 KB | **99 KB** | 5 | none | 16 | 44 | **2.8 s** |
| Dashboard | 6.7 KB | 0.0 KB | 93.1 KB | **100 KB** | 5 | none | 37 | 102 | **2.8 s** |
| Course overview (Form 5 Mathematics) | 7.6 KB | 0.9 KB | 93.1 KB | **101 KB** | 5 | none | 22 | 51 | **2.9 s** |
| Lesson, reading (Solving Quadratic Equations by Factorization) | 10.3 KB | 0.0 KB | 175.0 KB | **185 KB** | 9 | none | 37 | 72 | **4.6 s** |
| Lesson, interactive (Newton’s Second Law of Motion) | 6.6 KB | 0.0 KB | 176.1 KB | **183 KB** | 10 | none | 22 | 33 | **4.5 s** |
| Lesson, video (Understanding River Erosion) | 5.1 KB | 0.2 KB | 96.5 KB | **102 KB** | 6 | none | 25 | 35 | **2.9 s** |
| Practice | 3.6 KB | 0.0 KB | 93.1 KB | **97 KB** | 5 | none | 15 | 27 | **2.8 s** |
| Practice set start | 3.5 KB | 0.0 KB | 93.1 KB | **97 KB** | 5 | none | 16 | 28 | **2.8 s** |
| My progress | 5.3 KB | 0.0 KB | 93.1 KB | **98 KB** | 5 | none | 39 | 75 | **2.8 s** |
| Study planner | 8.4 KB | 0.0 KB | 93.1 KB | **101 KB** | 5 | none | 20 | 79 | **2.9 s** |

## Before and after (2026-11-05)

Before, every page also loaded Flowbite's JavaScript (29.5 KB gzip, used by no template) and Google
Fonts from two third-party hosts (`fonts.googleapis.com` for a render-blocking stylesheet, then
`fonts.gstatic.com` for the font files). Every lesson and practice-question page loaded KaTeX
(79 KB gzip) whether or not it had maths. The "before" totals below leave out the Google font bytes,
which were not measurable from the server, so the real difference is larger than shown.

| Page | Before (bytes we serve) | Before est. slow 3G | After (now incl. fonts) | After est. slow 3G |
|---|---:|---:|---:|---:|
| Landing, Explore, Dashboard, Course, Practice, Progress, Planner | 78–83 KB + Google Fonts | 4.8–4.9 s | 97–101 KB | 2.8–2.9 s |
| Lesson with maths (reading, interactive) | 164–166 KB + Google Fonts | 6.6 s | 183–185 KB | 4.5–4.6 s |
| Lesson without maths (video) | 161 KB + Google Fonts | 6.5 s | 102 KB | 2.9 s |

What changed:

1. **Flowbite JS removed** from `base.html` (and from `scripts/copy-vendor.js`). Its Tailwind plugin
   still provides the CSS; no template used its JavaScript.
2. **Fonts self-hosted** in `static/vendor/fonts/` (from `@fontsource-variable`, copied by
   `npm run vendor`): one 47 KB variable Inter file covers every weight and is preloaded; STIX Two
   Text (maths glyphs) is only fetched by pages that use the `font-math` class. No page contacts a
   third-party host any more.
3. **KaTeX loaded on demand**: `static/js/lesson.js` downloads KaTeX only when the page contains maths
   (`[data-latex]`, `$`, `\(` or `\[`). The studio still loads it up front for its live previews.

## Still to do

- **Compress HTML in production.** Django does not gzip HTML; WhiteNoise only compresses static files.
  The table assumes gzip, so the web server or CDN in front of Django must compress `text/html`
  (decide in Feature 18, deployment). Without it, lesson HTML is 3–5 times bigger.
- **KaTeX remains the biggest file** on maths pages (79 KB plus 2–4 maths fonts of 5–26 KB each).
  Rendering maths to HTML when a lesson is published would remove it from student pages entirely.
- **Database queries**: the dashboard (37), reading lesson (37) and My progress (39) pages run the most.
  Server time is under 110 ms locally, so this matters less than download size on 3G, but should be
  checked on PostgreSQL with realistic data.
- Repeat visits are cheap: in production WhiteNoise serves static files with hashed names and
  long cache lifetimes, so after the first visit only the HTML is downloaded.
