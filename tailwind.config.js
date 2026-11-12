/**
 * KKEVO Academy — Tailwind theme ("Playful Ndop": bright, rounded, game-like, phone first).
 * Source: ../design-system/tailwind.config.js (keep the two in sync).
 */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./apps/**/templates/**/*.html",
    "./apps/**/*.py",
    "./static/js/**/*.js",
    "./node_modules/flowbite/**/*.js",
  ],
  // Classes assembled in templates from model values (e.g. accent-{{ subject.accent }}).
  safelist: ["accent-blue", "accent-emerald", "accent-amber", "accent-slate",
    "tile-blue", "tile-emerald", "tile-amber", "tile-slate",
    "session-blue", "session-emerald", "session-slate", "session-violet", "session-rose", "session-cyan", "session-amber", "session-plan"],
  theme: {
    extend: {
      colors: {
        navy: { DEFAULT: "#2A1F6B", 700: "#3B2E8C", 600: "#574BA8" },
        primary: { DEFAULT: "#5B3FE4", 700: "#4527C9", 100: "#E6E0FF", 50: "#F4F1FF", 300: "#B3A3FA" },
        success: { DEFAULT: "#1FBF75", text: "#0B7A47", 50: "#E8FBF1", 200: "#A8EDCB", 300: "#6FE0A8" },
        warning: { DEFAULT: "#FFB020", text: "#8F5200", 50: "#FFF6DC", 200: "#FFE08A" },
        danger: { DEFAULT: "#FF4D6A", text: "#BE1E3A", 50: "#FFEDF0", 200: "#FFC2CD" },
        surface: { bg: "#F6F0E2", card: "#FFFFFF", border: "#E2D8C4" },
        slate: { 50: "#F6F4FD", 100: "#EEEBF9", 200: "#E3DDF7", 300: "#CFC8EA", 400: "#9A93BC", 500: "#706A94",
          600: "#565078", 700: "#3F3A60", 800: "#2D2658", 900: "#1B1340" },
        ink: { heading: "#1B1340", body: "#2D2658", muted: "#665F8C" },
      },
      fontFamily: {
        sans: ["Nunito", "system-ui", "sans-serif"],
        math: ['"STIX Two Text"', "Georgia", "serif"],
      },
      fontSize: {
        display: ["48px", { lineHeight: "56px", letterSpacing: "-0.025em", fontWeight: "700" }],
        h1: ["36px", { lineHeight: "44px", letterSpacing: "-0.02em", fontWeight: "700" }],
        h2: ["24px", { lineHeight: "32px", letterSpacing: "-0.01em", fontWeight: "600" }],
        h3: ["18px", { lineHeight: "28px", fontWeight: "600" }],
        lesson: ["18px", { lineHeight: "30px" }],
      },
      borderRadius: { input: "12px", btn: "14px", card: "20px", panel: "28px" },
      boxShadow: {
        card: "0 1px 2px rgba(15,23,42,.05)",
        raised: "0 8px 24px rgba(15,23,42,.08)",
        hero: "0 24px 60px rgba(16,42,67,.14)",
        float: "0 12px 32px rgba(16,42,67,.12)",
        cta: "0 6px 16px rgba(91,63,228,.28)",
      },
      spacing: { sidebar: "264px", rail: "256px", header: "64px" },
      maxWidth: { content: "1200px", reading: "720px" },
      minHeight: { touch: "44px" },
      screens: { nav: "900px" },
    },
  },
  plugins: [require("flowbite/plugin")],
};
