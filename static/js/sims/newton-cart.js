/* Newton's second law cart simulation (mockup 05), as an Alpine component.
 * Usage: <div x-data="newtonCart()"> … </div>
 */
window.newtonCart = function (options) {
  var opts = Object.assign({ force: 20, mass: 5, track: 20, maxForce: 50, minMass: 1, maxMass: 20 }, options || {});
  return {
    force: opts.force, mass: opts.mass, t: 0, running: false, raf: null,
    get a() { return this.force / this.mass; },
    get distance() { return Math.min(0.5 * this.a * this.t * this.t, opts.track); },
    get velocity() { return this.a * this.t; },
    get done() { return this.distance >= opts.track - 0.001; },
    get position() { return (this.distance / opts.track) * 100; },
    get forceWidth() { return Math.max(8, this.force * 3); },
    get accWidth() { return Math.max(0, Math.min(110, this.a * 12)); },
    get cartHeight() { return 56 + this.mass * 2.5; },
    get status() { return this.running ? "Running…" : this.done ? "Reached " + opts.track + " m" : "Ready — press Run"; },
    get statusColor() { return this.running ? "bg-success" : this.done ? "bg-primary" : "bg-slate-400"; },
    get runLabel() { return this.running ? "Running" : this.done ? "Run again" : "Run"; },
    get insight() {
      if (this.force === 0) return "With no resultant force the cart stays at rest. Acceleration is zero.";
      return "Each newton of force on this " + this.mass + " kg cart adds " + (1 / this.mass).toFixed(2) + " m/s² of acceleration.";
    },
    fill: function (val, min, max, colour) {
      var p = ((val - min) / (max - min)) * 100;
      return "background: linear-gradient(to right," + colour + " 0 " + p + "%,#E2E8F0 " + p + "% 100%)";
    },
    stop: function (changes) {
      if (this.raf) cancelAnimationFrame(this.raf);
      this.raf = null; this.running = false; this.t = 0;
      Object.assign(this, changes || {});
      this.force = Math.max(0, Math.min(opts.maxForce, Number(this.force)));
      this.mass = Math.max(opts.minMass, Math.min(opts.maxMass, Number(this.mass)));
    },
    run: function () {
      var self = this, a = this.a;
      if (this.running || a <= 0) return;
      var tEnd = Math.sqrt((2 * opts.track) / a);
      var t0 = this.t >= tEnd - 0.001 ? 0 : this.t;
      var start = performance.now() - t0 * 1000;
      this.running = true; this.t = t0;
      var step = function (now) {
        var t = (now - start) / 1000;
        if (t >= tEnd) { self.t = tEnd; self.running = false; self.raf = null; return; }
        self.t = t;
        self.raf = requestAnimationFrame(step);
      };
      this.raf = requestAnimationFrame(step);
    },
  };
};
