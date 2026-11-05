/* Lesson player behaviour shared by reading, interactive and video lessons.
 * - Renders maths with KaTeX ($...$ inline, [data-latex] display blocks)
 * - Tracks reading position, scroll % and active time; reports to the server
 * - Remembers the chosen text size on this device
 */
(function () {
  // KaTeX (~80 KB) is only downloaded when the page has maths. Layouts pass its URLs as
  // data-katex-* attributes on this script tag; pages that load KaTeX themselves still work.
  var self = document.currentScript;
  var katexUrls = self && self.dataset.katexJs
    ? { js: self.dataset.katexJs, auto: self.dataset.katexAuto, css: self.dataset.katexCss } : null;
  var katexLoading = null;

  function hasMaths(root) {
    if (root.querySelector("[data-latex]")) return true;
    var scope = root === document.body ? (document.querySelector("main") || root) : root;
    return /\$|\\\(|\\\[/.test(scope.textContent || "");
  }

  function loadKatex() {
    if (window.katex || !katexUrls) return Promise.resolve();
    if (katexLoading) return katexLoading;
    katexLoading = new Promise(function (resolve) {
      var css = document.createElement("link");
      css.rel = "stylesheet";
      css.href = katexUrls.css;
      document.head.appendChild(css);
      function add(src, done) {
        var s = document.createElement("script");
        s.src = src;
        s.onload = done;
        s.onerror = done;
        document.head.appendChild(s);
      }
      add(katexUrls.js, function () { add(katexUrls.auto, resolve); });
    });
    return katexLoading;
  }

  function renderMaths(root) {
    if (window.katex) return renderNow(root);
    if (!hasMaths(root)) return;
    loadKatex().then(function () { renderNow(root); });
  }

  function renderNow(root) {
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

  function isTyping(e) {
    var t = e.target;
    return t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName));
  }

  window.lessonPlayer = function (opts) {
    return {
      percent: opts.percent || 0,
      position: "",
      activeSince: Date.now(),
      pending: 0,
      moved: false,          // only report a position once the student has actually scrolled
      resume: opts.resume || null,
      notesOpen: false,
      helpOpen: false,
      textSize: (function () { try { return localStorage.getItem("lessonTextSize") || "md"; } catch (e) { return "md"; } })(),
      init: function () {
        var self = this;
        this.onScroll();
        window.addEventListener("scroll", function () { self.moved = true; self.onScroll(); }, { passive: true });
        document.addEventListener("visibilitychange", function () {
          if (document.hidden) { self.flush(true); } else { self.activeSince = Date.now(); }
        });
        window.addEventListener("pagehide", function () { self.flush(true); });
        window.addEventListener("keydown", function (e) { self.onKey(e); });
        setInterval(function () { if (!document.hidden) self.flush(false); }, 30000);
        if (this.resume && opts.autoResume) {
          // After load so KaTeX and fonts have settled before we measure
          if (document.readyState === "complete") { this.continueReading(); }
          else { window.addEventListener("load", function () { self.continueReading(); }); }
        }
      },
      /* "Continue from <section>": jump to the saved section and dismiss the banner. */
      continueReading: function () {
        if (!this.resume) return;
        var el = document.getElementById(this.resume.anchor);
        this.resume = null;
        if (!el) return;
        el.scrollIntoView({ block: "start" });
        if (!el.hasAttribute("tabindex")) el.setAttribute("tabindex", "-1");
        el.focus({ preventScroll: true });
        this.moved = true;
      },
      dismissResume: function () { this.resume = null; },
      /* j / k: next / previous section */
      jumpSection: function (dir) {
        var list = Array.prototype.slice.call(document.querySelectorAll("#objectives, #lesson-body [data-toc][id]"));
        var i, target = null;
        if (dir > 0) {
          for (i = 0; i < list.length; i++) { if (list[i].getBoundingClientRect().top > 110) { target = list[i]; break; } }
        } else {
          for (i = list.length - 1; i >= 0; i--) { if (list[i].getBoundingClientRect().top < 70) { target = list[i]; break; } }
        }
        if (target) target.scrollIntoView({ block: "start" });
      },
      onKey: function (e) {
        if (e.key === "Escape") { this.notesOpen = false; this.helpOpen = false; return; }
        if (e.ctrlKey || e.metaKey || e.altKey || isTyping(e)) return;
        var go = function (url) { if (url) window.location.href = url; };
        var actions = {
          j: function () { this.jumpSection(1); },
          k: function () { this.jumpSection(-1); },
          n: function () { go(opts.nextUrl); },
          p: function () { go(opts.prevUrl); },
          c: function () { this.continueReading(); },
          w: function () { if (opts.hasNotesPanel) this.toggleNotes(); },
          "?": function () { this.helpOpen = !this.helpOpen; },
        };
        var action = actions[e.key];
        if (!action) return;
        e.preventDefault();
        action.call(this);
      },
      toggleNotes: function () {
        this.notesOpen = !this.notesOpen;
        var id = this.notesOpen ? "note-body" : "notes-toggle";
        setTimeout(function () { var el = document.getElementById(id); if (el) el.focus(); }, 60);
      },
      printLesson: function () { window.print(); },
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
        data.append("position", this.moved ? (this.position || "") : "");
        data.append("anchor", this.moved ? (this.activeAnchor || "") : "");
        if (opts.videoPosition) data.append("video_position", Math.round(opts.videoPosition()));
        if (useBeacon && navigator.sendBeacon) { navigator.sendBeacon(opts.heartbeatUrl, data); return; }
        fetch(opts.heartbeatUrl, { method: "POST", body: data, credentials: "same-origin" }).catch(function () {});
      },
    };
  };

  /* Live LaTeX preview for the content studio formula block. */
  window.latexPreview = function (src) {
    return {
      src: src,
      render: function () {
        if (window.katex && this.$refs.preview) {
          katex.render(this.src || "", this.$refs.preview, { displayMode: true, throwOnError: false });
        }
      },
      init: function () {
        var self = this;
        this.$watch("src", function () { self.render(); });
        if (window.katex) { this.render(); } else { window.addEventListener("load", function () { self.render(); }); }
      },
    };
  };

  /* Learning-objective checklist remembered on this device. */
  window.checklist = function (key) {
    var stored = [];
    try { stored = JSON.parse(localStorage.getItem(key) || "[]"); } catch (e) {}
    return {
      done: stored,
      save: function () { try { localStorage.setItem(key, JSON.stringify(this.done)); } catch (e) {} },
    };
  };

  /* Multiple-choice quick check inside a lesson (block type "quiz").
   * Optional hint, per-choice feedback for wrong answers, and "Show answer" after
   * two wrong tries so nobody gets stuck (Khan Academy / Brilliant pattern). */
  window.quickCheck = function (correct) {
    return {
      picked: null, checked: false, correct: correct, wrongTries: 0, hintShown: false, revealed: false,
      pick: function (i) { if (this.revealed) return; this.picked = i; this.checked = false; },
      check: function () {
        if (this.picked === null) return;
        if (!this.checked && this.picked !== this.correct) this.wrongTries += 1;
        this.checked = true;
      },
      get solved() { return this.checked && this.picked === this.correct; },
      get canReveal() { return this.wrongTries >= 2 && !this.solved; },
      reveal: function () { this.revealed = true; this.picked = this.correct; this.checked = true; },
      state: function (i) {
        if (this.picked !== i) return "idle";
        if (!this.checked) return "picked";
        return i === this.correct ? "right" : "wrong";
      },
    };
  };
})();
