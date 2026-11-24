/*
 * matheusneder.com: progressive enhancements only.
 * Everything here is optional: content and navigation work without JavaScript.
 *   1. Theme toggle (light/dark, persisted)
 *   2. Language preference (persisted when the visitor switches language)
 *   3. Current section highlight in the navigation
 *   4. Click-to-load video (no third-party request until the visitor asks)
 */
(function () {
  "use strict";

  var root = document.documentElement;
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) { /* storage unavailable */ } }
  };

  /* 1. Theme ------------------------------------------------------------- */
  var darkQuery = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;
  var toggle = document.querySelector(".theme-toggle");

  function activeTheme() {
    return root.dataset.theme || (darkQuery && darkQuery.matches ? "dark" : "light");
  }

  function syncTheme() {
    var theme = activeTheme();
    root.dataset.activeTheme = theme;
    if (toggle) {
      var next = theme === "dark" ? "light" : "dark";
      toggle.setAttribute("aria-label", toggle.getAttribute("data-label-" + next));
      toggle.setAttribute("title", toggle.getAttribute("data-label-" + next));
    }
  }

  if (toggle) {
    toggle.hidden = false;
    toggle.addEventListener("click", function () {
      var next = activeTheme() === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      store.set("theme", next);
      syncTheme();
    });
  }
  if (darkQuery && darkQuery.addEventListener) darkQuery.addEventListener("change", syncTheme);
  syncTheme();

  /* 2. Language preference ----------------------------------------------- */
  document.querySelectorAll("[data-set-lang]").forEach(function (link) {
    link.addEventListener("click", function () {
      store.set("lang", link.getAttribute("data-set-lang"));
    });
  });

  /* 3. Current section in navigation ------------------------------------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".site-nav a[href^='#']"));
  if ("IntersectionObserver" in window && navLinks.length) {
    var byId = {};
    navLinks.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var visible = {};
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { visible[e.target.id] = e.isIntersecting; });
      var current = null;
      for (var i = 0; i < navLinks.length; i++) {
        var id = navLinks[i].getAttribute("href").slice(1);
        if (visible[id]) { current = id; break; }
      }
      navLinks.forEach(function (a) {
        if (a.getAttribute("href").slice(1) === current) a.setAttribute("aria-current", "true");
        else a.removeAttribute("aria-current");
      });
    }, { rootMargin: "-35% 0px -55% 0px" });
    Object.keys(byId).forEach(function (id) {
      var section = document.getElementById(id);
      if (section) observer.observe(section);
    });
  }

  /* 4. Click-to-load video ----------------------------------------------- */
  document.querySelectorAll("[data-video-id]").forEach(function (link) {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      var id = link.getAttribute("data-video-id");
      var iframe = document.createElement("iframe");
      iframe.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id) + "?autoplay=1&rel=0";
      iframe.title = link.getAttribute("data-video-title") || "YouTube";
      iframe.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
      iframe.allowFullscreen = true;
      iframe.referrerPolicy = "strict-origin-when-cross-origin";
      var container = link.parentNode;
      container.replaceChildren(iframe);
      iframe.focus();
    });
  });
})();
