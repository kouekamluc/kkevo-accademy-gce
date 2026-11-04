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
for (const [src, dest] of Object.entries(files)) {
  fs.copyFileSync(path.join(__dirname, "..", src), path.join(out, dest));
  console.log(`copied ${dest}`);
}
