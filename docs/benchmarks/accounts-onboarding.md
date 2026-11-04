# Benchmark: sign-up, login, recovery and onboarding

Scope: how Duolingo, Khan Academy, Coursera and uLesson (plus a glance at other
African ed-tech) handle accounts for teenagers on phones, and what we take from them
for GCE students on slow, expensive mobile data. Based on the public web and app
flows as of late 2026. Details change often, so read this as patterns, not specs.

## What they do

| | Sign-up | Login | Recovery | Onboarding |
|---|---|---|---|---|
| **Duolingo** | Lets you try a lesson *before* you create an account. Profile creation comes later. Age is asked, and under-13s get restricted features. | Email/username + password, or Google/Apple/Facebook. Stays signed in by default. | "Forgot password" link next to the field. Email link that signs you straight in. | Short, one question per screen (language, reason, daily goal, level). Progress bar at the top. Every step is skippable or has a default. |
| **Khan Academy** | Learner / teacher / parent roles. Asks birth date; under-13s need a parent's email to finish (COPPA). | Email or username + password, Google, Apple, Clever. | Email reset. For child accounts the parent or teacher resets it. | Asks for grade and courses, then suggests a "course mastery" path. Parent and teacher dashboards are a separate product area. |
| **Coursera** | Email + password or SSO. Asks for very little at the start. | Rate-limited, sometimes with a CAPTCHA after failures. "Remember me" is implicit. | Email reset link. A generic "if an account exists" message so you can't tell which emails are registered. | Asks about goals and role. Easy to skip. |
| **uLesson** (Nigeria/Ghana) | Phone number + OTP is the main path, with email as a fallback. Asks for class (JSS/SSS) and exam (WAEC/NECO/JAMB) straight away. | Phone/OTP or email + password. Stays signed in. | OTP by SMS or a reset by email. | Class → subjects → content downloads (the app is built around offline packs and SD-card content). |
| Others (Eneza, M-Shule, Kytabu) | SMS/USSD sign-up for feature phones. | — | Codes by SMS | Very short. Class and subject only. |

### Patterns that work well
1. **Ask for the minimum first.** Name, email and password, or just a phone number. Everything else comes later and is saved step by step.
2. **One decision per screen, with a visible step counter.** Every product does this. Our 5-step wizard (mockup 07) already does it.
3. **Recovery is one tap from the password field** ("Forgot password?") and **never reveals whether an email is registered.**
4. **Stay signed in by default** on personal phones, with a way to sign out on shared devices.
5. **Brute-force protection is invisible until it matters.** After several failures you get a calm message with a way out (reset your password), not a dead end.
6. **Privacy controls in settings:** download your data and delete your account (GDPR/COPPA-driven at Khan Academy, Duolingo and Coursera; also needed under Cameroon's 2024 personal-data protection law).
7. **Show/hide password** on mobile keyboards, where typos are common.

## What we adopt (built in this round)

| Improvement | Why (pattern above) |
|---|---|
| **Password reset by email**: Django's built-in token views, styled with our auth layout. Includes a generic "check your email" page, tips about the spam folder and slow delivery, a one-day single-use link, signing you in after the reset, and a clear "this link has expired" state. | 3. A teenager who forgets a password on a borrowed phone must not lose months of progress. Signing in after a reset copies Duolingo and saves one more slow page load. |
| **Login brute-force protection**: cache-based, per email + IP, 5 tries per 15 minutes. Warns when 2 tries are left. The lock message links to the reset page. HTTP 429. Password-reset requests are also limited per IP so the form can't be used to flood inboxes. No new dependency. | 5. Coursera-style calm lockout. Limiting per email + IP (not per email alone) means an attacker can't lock a classmate out from another network. Not limiting per IP alone avoids blocking a whole school or cyber café behind one shared IP. |
| **"Keep me signed in"**: ticked by default (30-day session). Unticked, the session ends when the browser closes. The hint says to untick it on a shared phone or cyber café computer. | 4. Cameroonian students often share family phones or use cyber cafés, so the choice matters more here than for Duolingo's mostly personal-device users. |
| **Download my data / Delete my account**: one JSON file with every record linked to the student, built from the model graph so new features are included automatically. Deletion needs the password, has a "download first" link, and removes all learning data. Staff accounts are excluded. | 6. Trust for parents and schools, and legal hygiene. The JSON file is tiny, so it's cheap on data. |
| **Show/Hide password button** on login, reset and delete forms, with `autocomplete` hints so password managers and Android autofill work. | 7. Fewer failed logins, which means fewer rate-limit lockouts. |

## What we skip, and why

- **Phone number + SMS OTP sign-in (uLesson).** This is the best fit for our market, but it needs a paid SMS gateway (MTN/Orange aggregators), number verification and fraud controls. It's a product decision with running costs. Email stays the identifier for now. It's already listed under "Known gaps" in ARCHITECTURE.md.
- **Google/Apple sign-in.** Adds third-party JavaScript and redirects (heavy on 2G/3G), and many students don't have a Google account they control. Revisit with phone sign-in.
- **Try a lesson before sign-up (Duolingo).** Valuable, but it touches the lesson player (another lane). Recommended next step: let `/learn/` preview one lesson anonymously.
- **Parent/guardian email or accounts (Khan Academy).** GCE candidates are mostly 15–19, so the under-13 consent flows that drive Khan's design don't apply. A guardian dashboard is a separate feature, and collecting a second adult's email adds personal data we have no use for yet.
- **CAPTCHA after failures.** Third-party scripts, data cost and accessibility problems. The rate limit is enough at our scale.
- **Email verification at sign-up.** It would block onboarding on slow email delivery. The reset flow already proves ownership when it matters. Consider a soft "verify your email" prompt later.
- **Age gate.** Not needed for this age group. Our terms should state the minimum age.

## Operational notes
- In development (`DEBUG`), emails are printed to the console. In production, set `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS` and `DEFAULT_FROM_EMAIL`.
- The rate limit uses the default cache (memory, per process). With several workers, set `CACHE_URL` (for example `dbcache://django_cache` after `manage.py createcachetable`, or Redis). Behind a reverse proxy, set `DJANGO_TRUSTED_PROXY_COUNT` so the real client IP is used.
