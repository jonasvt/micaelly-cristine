/* Micaelly Cristine — portfolio. ~2 KB, no dependencies.
   1. Header border on scroll
   2. Reveal-on-scroll (skipped when the user prefers reduced motion)
   3. Video players: nothing downloads until needed; one video plays at a time. */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var saveData = navigator.connection && navigator.connection.saveData;

  /* 1. Header ----------------------------------------------------------- */
  var header = document.querySelector("[data-header]");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* 2. Reveal ----------------------------------------------------------- */
  var revealEls = document.querySelectorAll(".reveal");
  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("is-visible"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* 2b. Animated poster fan (AI page header) ------------------------------
     Deals the cards in, then every few seconds shifts them one place to the
     left; the card that lands in the centre plays a tiny muted preview.
     Pauses on hover/focus, when off screen and when the tab is hidden. */
  (function initFan() {
    var fan = document.querySelector("[data-fan]");
    if (!fan) return;
    var cards = Array.prototype.slice.call(fan.querySelectorAll("[data-fan-card]"));
    var n = cards.length;
    var mid = (n - 1) / 2;
    var pos = cards.map(function (_, i) { return i; });
    var INTERVAL = 3200;
    var timer = null;
    var hovering = false;
    var visible = true;

    function layout() {
      cards.forEach(function (card, i) {
        var o = pos[i] - mid;
        var a = Math.abs(o);
        card.style.setProperty("--o", o);
        card.style.setProperty("--a", a);
        card.style.zIndex = String(10 - a * 3);
        var active = a === 0;
        card.classList.toggle("is-active", active);
        var v = card.querySelector("video");
        if (!v) return;
        if (active && !reduceMotion && !saveData) {
          if (!v.getAttribute("src")) {
            v.setAttribute("src", v.getAttribute("data-src"));
            v.addEventListener("playing", function () { v.classList.add("is-ready"); });
          }
          try { v.currentTime = 0; } catch (e) {}
          var pr = v.play();
          if (pr && pr.catch) pr.catch(function () {});
        } else {
          v.pause();
          v.classList.remove("is-ready");
        }
      });
    }

    function step() {
      pos = pos.map(function (p) { return (p - 1 + n) % n; });
      layout();
    }
    function start() {
      if (timer || reduceMotion || hovering || !visible || document.hidden) return;
      timer = window.setInterval(step, INTERVAL);
    }
    function stop() {
      if (timer) { window.clearInterval(timer); timer = null; }
    }

    layout();

    if (reduceMotion) {
      fan.classList.add("is-dealt");
      return;
    }

    // Deal-in, then start rotating.
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        fan.classList.add("is-dealing", "is-dealt");
        window.setTimeout(function () { fan.classList.remove("is-dealing"); start(); }, 1600);
      });
    });

    fan.addEventListener("mouseenter", function () { hovering = true; stop(); });
    fan.addEventListener("mouseleave", function () { hovering = false; start(); });
    document.addEventListener("visibilitychange", function () { document.hidden ? stop() : start(); });
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        visible ? start() : stop();
      }, { threshold: 0.2 }).observe(fan);
    }
  })();

  /* 3. Players ---------------------------------------------------------- */
  var players = Array.prototype.slice.call(document.querySelectorAll("[data-player]"));

  function load(video) {
    if (!video.getAttribute("src")) {
      video.setAttribute("src", video.getAttribute("data-src"));
    }
  }

  function stopOthers(current) {
    players.forEach(function (p) {
      if (p === current) return;
      var v = p.querySelector("video");
      if (!v.paused && !p.classList.contains("is-ambient")) v.pause();
      if (p.classList.contains("is-ambient")) v.muted = true;
    });
  }

  function playWithSound(player) {
    var video = player.querySelector("video");
    load(video);
    stopOthers(player);
    player.classList.remove("is-ambient");
    player.classList.add("is-playing");
    video.muted = false;
    video.loop = false;
    video.controls = true;
    if (player.hasAttribute("data-autoplay")) video.currentTime = 0;
    var pr = video.play();
    if (pr && pr.catch) pr.catch(function () {});
    video.focus({ preventScroll: true });
  }

  players.forEach(function (player) {
    var video = player.querySelector("video");
    var btn = player.querySelector("[data-play]");
    video.setAttribute("tabindex", "-1");

    btn.addEventListener("click", function () { playWithSound(player); });

    video.addEventListener("play", function () {
      if (!player.classList.contains("is-ambient")) stopOthers(player);
    });
    video.addEventListener("ended", function () {
      player.classList.remove("is-playing");
      video.controls = false;
    });

    /* Ambient autoplay (muted loop) only for the featured video, only when
       the user hasn't asked for less motion or less data, and only on screen. */
    if (player.hasAttribute("data-autoplay") && !reduceMotion && !saveData && "IntersectionObserver" in window) {
      var ambient = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!player.classList.contains("is-ambient") && player.classList.contains("is-playing")) return;
          if (e.isIntersecting) {
            load(video);
            video.muted = true;
            video.loop = true;
            player.classList.add("is-playing", "is-ambient");
            var pr = video.play();
            if (pr && pr.catch) pr.catch(function () { player.classList.remove("is-playing", "is-ambient"); });
          } else if (player.classList.contains("is-ambient")) {
            video.pause();
          }
        });
      }, { threshold: 0.25 });
      ambient.observe(player);
    }
  });
})();
