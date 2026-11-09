/* KKEVO Academy service worker (rendered by apps/core/pwa.py; version changes when precached assets change).
   - Precaches the app shell and the offline page.
   - Lesson pages the signed-in student opens are cached (stale-while-revalidate), keyed to that user.
   - /static/ files are cache-first.
   - Never touched: non-GET requests, login/accounts, practice, staff studio and admin. Logout clears lesson caches. */
const VERSION = "{{ version }}";
const SHELL = "kkevo-shell-" + VERSION;
const STATIC = "{{ static_cache }}";
const LESSONS = "kkevo-lessons-v1";
const META = "kkevo-meta-v1";
const KEEP = [SHELL, STATIC, LESSONS, META];
const OFFLINE_URL = "{{ offline_url }}";
const PRECACHE = {{ precache_json|safe }};
const STATIC_PREFIX = "{{ static_prefix }}";
const NEVER = {{ never_cache_json|safe }};
const USER_HEADER = "{{ user_header }}";
const LESSON_RE = /^\/courses\/[^/]+\/lessons\/\d+\/$/;
const MAX_STATIC_ENTRIES = 400;

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const shell = await caches.open(SHELL);
    await shell.add(new Request(OFFLINE_URL, { cache: "reload" }));
    const stat = await caches.open(STATIC);
    // One missing file must not block installation of the worker.
    await Promise.allSettled(PRECACHE.map((url) => stat.add(url)));
    await self.skipWaiting();
  })());
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    for (const name of await caches.keys()) {
      if (name.startsWith("kkevo-") && !KEEP.includes(name)) await caches.delete(name);
    }
    const stat = await caches.open(STATIC);
    const keys = await stat.keys();
    for (const req of keys.slice(0, Math.max(0, keys.length - MAX_STATIC_ENTRIES))) await stat.delete(req);
    await self.clients.claim();
  })());
});

async function getUser() {
  const r = await (await caches.open(META)).match("/__user");
  return r ? r.text() : "";
}
async function setUser(key) {
  await (await caches.open(META)).put("/__user", new Response(key));
}
async function purge() {
  await caches.delete(LESSONS);
  await setUser("");
}
/* Every HTML navigation response says who is signed in. If that changed (logout, other student), drop cached lessons. */
async function noteUser(response) {
  const key = response.headers.get(USER_HEADER) || "";
  if (key !== (await getUser())) {
    await caches.delete(LESSONS);
    await setUser(key);
  }
  return key;
}
async function tellClients(path) {
  for (const client of await self.clients.matchAll({ type: "window" })) client.postMessage({ type: "lesson-cached", path });
}

async function offlinePage() {
  return (await (await caches.open(SHELL)).match(OFFLINE_URL)) ||
    new Response("You are offline.", { status: 503, headers: { "Content-Type": "text/plain" } });
}

async function lessonNavigation(event, url) {
  const cache = await caches.open(LESSONS);
  const key = url.pathname;
  const user = await getUser();
  const cached = await cache.match(key, { ignoreVary: true });
  const usable = cached && user && cached.headers.get(USER_HEADER) === user;

  const store = async (response) => {
    const who = await noteUser(response);
    const lessons = await caches.open(LESSONS);
    if (response.ok && !response.redirected && who && response.type !== "opaqueredirect") {
      await lessons.put(key, response.clone());
      await tellClients(key);
    } else {
      await lessons.delete(key, { ignoreVary: true }); // e.g. session expired or lesson unpublished
    }
  };

  if (usable) {
    // Stale-while-revalidate: show what we have now, refresh for next time.
    event.waitUntil(
      fetch(url.href, { credentials: "same-origin", headers: { Accept: "text/html" } }).then(store).catch(() => {})
    );
    return cached;
  }
  try {
    const response = await fetch(event.request);
    event.waitUntil(store(response.clone()).catch(() => {}));
    return response;
  } catch (err) {
    return offlinePage();
  }
}

async function otherNavigation(event) {
  try {
    const response = await fetch(event.request);
    event.waitUntil(noteUser(response.clone()).catch(() => {}));
    return response;
  } catch (err) {
    return offlinePage();
  }
}

async function staticAsset(request) {
  const cache = await caches.open(STATIC);
  const hit = await cache.match(request);
  if (hit) return hit;
  const response = await fetch(request);
  if (response.ok && response.type === "basic") await cache.put(request, response.clone());
  return response;
}

self.addEventListener("fetch", (event) => {
  const request = event.request;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  if (request.method !== "GET") {
    // Pass through untouched (CSRF, practice submissions...). Logging out also clears this device's cached lessons.
    if (request.method === "POST" && url.pathname === "/accounts/logout/") {
      event.respondWith(purge().catch(() => {}).then(() => fetch(request)));
    }
    return;
  }
  if (url.pathname.startsWith(STATIC_PREFIX)) {
    event.respondWith(staticAsset(request));
    return;
  }
  if (request.mode !== "navigate") return;
  if (NEVER.some((prefix) => url.pathname.startsWith(prefix))) {
    event.respondWith(fetch(request).catch(offlinePage)); // never cached, only a friendly failure page
    return;
  }
  event.respondWith(LESSON_RE.test(url.pathname) ? lessonNavigation(event, url) : otherNavigation(event));
});

self.addEventListener("message", (event) => {
  if (event.data && event.data.type === "purge") event.waitUntil(purge());
});
