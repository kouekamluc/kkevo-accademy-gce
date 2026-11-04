// Copies front-end libraries into static/vendor so pages never depend on a CDN.
const fs = require("fs");
const path = require("path");

const files = {
  "node_modules/htmx.org/dist/htmx.min.js": "htmx.min.js",
  "node_modules/alpinejs/dist/cdn.min.js": "alpine.min.js",
  "node_modules/flowbite/dist/flowbite.min.js": "flowbite.min.js",
};
const out = path.join(__dirname, "..", "static", "vendor");
fs.mkdirSync(out, { recursive: true });
// KaTeX (maths): JS, auto-render, CSS and woff2 fonts only (smallest download).
const katexOut = path.join(out, "katex");
fs.mkdirSync(path.join(katexOut, "fonts"), { recursive: true });
const katexDist = path.join(__dirname, "..", "node_modules/katex/dist");
for (const f of ["katex.min.js", "katex.min.css", "contrib/auto-render.min.js"]) {
  fs.copyFileSync(path.join(katexDist, f), path.join(katexOut, path.basename(f)));
}
for (const f of fs.readdirSync(path.join(katexDist, "fonts")).filter((f) => f.endsWith(".woff2"))) {
  fs.copyFileSync(path.join(katexDist, "fonts", f), path.join(katexOut, "fonts", f));
}
console.log("copied katex");
for (const [src, dest] of Object.entries(files)) {
  fs.copyFileSync(path.join(__dirname, "..", src), path.join(out, dest));
  console.log(`copied ${dest}`);
}
