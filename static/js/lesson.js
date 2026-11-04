/* Lesson player behaviour shared by reading, interactive and video lessons.
 * - Renders maths with KaTeX ($...$ inline, [data-latex] display blocks)
 * - Tracks reading position, scroll % and active time; reports to the server
 * - Remembers the chosen text size on this device
 */
(function () {
  function renderMaths(root) {
    if (!window.katex) return;
    root.querySelectorAll("[data-latex]").forEach(function (el) {
      if (el.dataset.rendered) return;
      try {
        katex.render(el.dataset.latex, el, { displayMode: el.dataset.display !== "inline", throwOnError: false });
        el.dataset.rendered = "1";
      } catch (e) { el.textContent = el.dataset.latex; }
    });
    if (window.renderMathInElement) {
      renderMathInElement(root, {
        delimiters: [{ left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }],
        ignoredClasses: ["no-math"], throwOnError: false,
      });
    }
  }
  window.renderLessonMaths = renderMaths;
  document.addEventListener("DOMContentLoaded", function () { renderMaths(document.body); });
  document.addEventListener("htmx:afterSwap", function (e) { renderMaths(e.target); });

  function csrfToken() {
    var el = document.querySelector("[name=csrfmiddlewaretoken]");
    return el ? el.value : "";
  }

  window.lessonPlayer = function (opts) {
    return {
      percent: opts.percent || 0,
      position: "",
      activeSince: Date.now(),
      pending: 0,
      textSize: (function () { try { return localStorage.getItem("lessonTextSize") || "md"; } catch (e) { return "md"; } })(),
      init: function () {
        var self = this;
        this.onScroll();
        window.addEventListener("scroll", function () { self.onScroll(); }, { passive: true });
        document.addEventListener("visibilitychange", function () {
          if (document.hidden) { self.flush(true); } else { self.activeSince = Date.now(); }
        });
        window.addEventListener("pagehide", function () { self.flush(true); });
        setInterval(function () { if (!document.hidden) self.flush(false); }, 30000);
        if (opts.resumeAnchor) {
          var el = document.getElementById(opts.resumeAnchor);
          if (el && opts.resumeOnLoad) el.scrollIntoView();
        }
      },
      cycleTextSize: function () {
        this.textSize = { sm: "md", md: "lg", lg: "sm" }[this.textSize];
        try { localStorage.setItem("lessonTextSize", this.textSize); } catch (e) {}
      },
      onScroll: function () {
        var article = document.getElementById("lesson-body");
        if (!article) return;
        var rect = article.getBoundingClientRect();
        var seen = Math.min(Math.max(window.innerHeight - rect.top, 0), rect.height);
        var pct = rect.height ? Math.round((seen / rect.height) * 100) : 0;
        if (pct > this.percent) this.percent = pct;
        var heads = article.querySelectorAll("[data-toc]");
        var current = "";
        heads.forEach(function (h) { if (h.getBoundingClientRect().top < 140) current = h; });
        if (current) {
          this.position = current.dataset.toc;
          this.activeAnchor = current.id;
        }
      },
      activeAnchor: "",
      flush: function (useBeacon) {
        var seconds = Math.round((Date.now() - this.activeSince) / 1000);
        this.activeSince = Date.now();
        if (seconds < 3 && !useBeacon) return;
        var data = new FormData();
        data.append("csrfmiddlewaretoken", csrfToken());
        data.append("seconds", Math.min(seconds, 120));
        data.append("percent", this.percent);
        data.append("position", this.position || "");
        if (opts.videoPosition) data.append("video_position", Math.round(opts.videoPosition()));
        if (useBeacon && navigator.sendBeacon) { navigator.sendBeacon(opts.heartbeatUrl, data); return; }
        fetch(opts.heartbeatUrl, { method: "POST", body: data, credentials: "same-origin" }).catch(function () {});
      },
    };
  };

  /* Multiple-choice quick check inside a lesson (block type "quiz"). */
  window.quickCheck = function (correct) {
    return {
      picked: null, checked: false, correct: correct,
      pick: function (i) { this.picked = i; this.checked = false; },
      check: function () { if (this.picked !== null) this.checked = true; },
      state: function (i) {
        if (this.picked !== i) return "idle";
        if (!this.checked) return "picked";
        return i === this.correct ? "right" : "wrong";
      },
    };
  };
})();
