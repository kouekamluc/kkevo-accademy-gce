/**
 * GCE Learning Academy — Tailwind theme ("Academic Clarity").
 * Source: ../design-system/tailwind.config.js (keep the two in sync).
 */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./apps/**/templates/**/*.html",
    "./apps/**/*.py",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        navy: { DEFAULT: "#102A43", 700: "#1E3A5F", 600: "#334E68" },
        primary: { DEFAULT: "#2563EB", 700: "#1D4ED8", 100: "#DBEAFE", 50: "#EFF6FF", 300: "#93C5FD" },
        success: { DEFAULT: "#10B981", text: "#047857", 50: "#ECFDF5", 200: "#A7F3D0", 300: "#6EE7B7" },
        warning: { DEFAULT: "#F59E0B", text: "#B45309", 50: "#FFFBEB", 200: "#FDE68A" },
        danger: { DEFAULT: "#EF4444", text: "#B91C1C", 50: "#FEF2F2", 200: "#FECACA" },
        surface: { bg: "#F8FAFC", card: "#FFFFFF", border: "#E2E8F0" },
        ink: { heading: "#0F172A", body: "#1E293B", muted: "#64748B" },
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
        math: ['"STIX Two Text"', "Georgia", "serif"],
      },
      fontSize: {
        display: ["48px", { lineHeight: "56px", letterSpacing: "-0.025em", fontWeight: "700" }],
        h1: ["36px", { lineHeight: "44px", letterSpacing: "-0.02em", fontWeight: "700" }],
        h2: ["24px", { lineHeight: "32px", letterSpacing: "-0.01em", fontWeight: "600" }],
        h3: ["18px", { lineHeight: "28px", fontWeight: "600" }],
        lesson: ["18px", { lineHeight: "30px" }],
      },
      borderRadius: { input: "8px", btn: "10px", card: "14px", panel: "20px" },
      boxShadow: {
        card: "0 1px 2px rgba(15,23,42,.05)",
        raised: "0 8px 24px rgba(15,23,42,.08)",
        hero: "0 24px 60px rgba(16,42,67,.14)",
        float: "0 12px 32px rgba(16,42,67,.12)",
        cta: "0 6px 16px rgba(37,99,235,.25)",
      },
      spacing: { sidebar: "264px", rail: "256px", header: "64px" },
      maxWidth: { content: "1200px", reading: "720px" },
      minHeight: { touch: "44px" },
      screens: { nav: "900px" },
    },
  },
  plugins: [require("flowbite/plugin")],
};
