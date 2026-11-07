/* Registers the service worker and shows the small "Available offline" hint on cached lessons. */
(function () {
  if (!("serviceWorker" in navigator)) return;

  function showHint() {
    document.querySelectorAll("[data-offline-hint]").forEach(function (el) { el.hidden = false; });
  }
  function checkCached() {
    if (!window.caches || !document.querySelector("[data-offline-hint]")) return;
    caches.open("kkevo-lessons-v1").then(function (c) { return c.match(location.pathname, { ignoreVary: true }); })
      .then(function (hit) { if (hit) showHint(); }).catch(function () {});
  }

  window.addEventListener("load", function () {
    navigator.serviceWorker.register("/sw.js", { scope: "/" }).catch(function () {});
    checkCached();
  });
  navigator.serviceWorker.addEventListener("message", function (event) {
    if (event.data && event.data.type === "lesson-cached" && event.data.path === location.pathname) showHint();
  });
  // Log out: clear this device's cached lessons straight away (also works if the request later fails).
  document.addEventListener("submit", function (event) {
    var form = event.target;
    if (form && form.getAttribute && /\/accounts\/logout\/$/.test(form.getAttribute("action") || "") && navigator.serviceWorker.controller) {
      navigator.serviceWorker.controller.postMessage({ type: "purge" });
    }
  });
})();
