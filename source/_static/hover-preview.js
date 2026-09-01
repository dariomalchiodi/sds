/*
 * SDS hover-preview
 * -----------------
 * Shows a floating preview of a cross-reference target (definition, theorem,
 * figure, table, …) when the reader hovers an internal link.
 *
 * Configuration (set in each conf.py via html_context, surfaced in
 * source/_templates/layout.html as window.sphinxConfig.hoverPreview):
 *   - enabled : master on/off switch (default: on)
 *   - types   : which target kinds get a preview, e.g.
 *               ["definition","theorem","lemma","corollary","proposition",
 *                "example","figure","table"]
 *
 * A reader can override the on/off state at runtime (persisted in
 * localStorage, key "sdsHoverPreview"):
 *   window.sdsHoverPreview.disable() / .enable() / .toggle()
 *
 * Design notes:
 *   - Pure client side, no build/Sphinx changes. Degrades to plain links.
 *   - Math is rendered in the browser (KaTeX auto-render), so injected
 *     preview content is re-rendered via the global renderMathInElement /
 *     katex_options (see source/_static/katex_autorenderer.js).
 *   - Cross-page targets are fetched same-origin (cached) and their relative
 *     asset URLs rewritten to absolute, so images/links resolve correctly.
 *   - Disabled on touch-only devices (no hover).
 */
(function () {
  "use strict";

  var CFG = (window.sphinxConfig && window.sphinxConfig.hoverPreview) || {};
  var DEFAULT_TYPES = ["definition", "theorem", "lemma", "corollary",
                       "proposition", "example", "exercise", "figure", "table",
                       "section", "footnote", "equation"];

  // For section previews, how many direct content blocks (after the heading,
  // before the first nested subsection) to include.
  var SECTION_MAX_BLOCKS = 4;
  var TYPES = (Array.isArray(CFG.types) && CFG.types.length) ? CFG.types : DEFAULT_TYPES;

  var SHOW_DELAY = 350;   // ms of hover intent before a preview appears
  var HIDE_DELAY = 180;   // ms grace so the pointer can travel into the popover

  // Admonition kinds are identified by a class on the target <div>. Note the
  // sphinx-proof framework also adds a generic "proof" class to these blocks,
  // so we never treat bare "proof" as a kind here.
  var ADMONITION_KINDS = ["definition", "theorem", "lemma", "corollary",
                          "proposition", "example", "exercise", "remark",
                          "axiom", "property", "algorithm", "conjecture",
                          "observation"];

  // Touch-only devices: no hover, so do nothing.
  var TOUCH = !!(window.matchMedia && window.matchMedia("(hover: none)").matches);

  var pop = null;
  var showTimer = null;
  var hideTimer = null;
  var currentLink = null;
  var docCache = new Map();   // origin+pathname -> parsed Document

  // Build-time default, overridable by the reader via localStorage.
  function isEnabled() {
    var ls = null;
    try { ls = localStorage.getItem("sdsHoverPreview"); } catch (e) {}
    if (ls === "on") return true;
    if (ls === "off") return false;
    return CFG.enabled !== false;
  }

  function isHeading(el) {
    return el && el.tagName && /^h[1-6]$/.test(el.tagName.toLowerCase());
  }

  // Map a raw cross-reference target to the element to preview and its kind,
  // or null if it is not a previewable kind. Section references resolve to an
  // empty anchor <span> (or a heading) that labels a <section>; in that case we
  // preview the enclosing section, not the bare anchor.
  function classify(el) {
    if (!el) return null;
    var tag = el.tagName ? el.tagName.toLowerCase() : "";
    if (tag === "figure") return { el: el, kind: "figure" };
    if (tag === "table") return { el: el, kind: "table" };
    if (tag === "section") return { el: el, kind: "section" };
    if (tag === "aside" && el.classList && el.classList.contains("footnote")) {
      return { el: el, kind: "footnote" };
    }
    if (el.classList) {
      if (el.classList.contains("sds-proof")) return { el: el, kind: "proof" };
      // Numbered display equation: <div class="math" id="equation-…">. Inline
      // math is a <span class="math"> and is never a reference target, so
      // restricting to <div> keeps this to the numbered block form.
      if (el.classList.contains("math") && tag === "div") {
        return { el: el, kind: "equation" };
      }
      for (var i = 0; i < ADMONITION_KINDS.length; i++) {
        if (el.classList.contains(ADMONITION_KINDS[i])) {
          return { el: el, kind: ADMONITION_KINDS[i] };
        }
      }
    }
    // Section label (anchor span before a heading) or a heading itself.
    if (isHeading(el) || isHeading(el.nextElementSibling)) {
      var sec = el.closest ? el.closest("section") : null;
      if (sec) return { el: sec, kind: "section" };
    }
    return null;
  }

  function tryDisplay(link, el, baseHref) {
    var c = classify(el);
    if (c && TYPES.indexOf(c.kind) !== -1) display(link, c.el, c.kind, baseHref);
  }

  function ensurePopover() {
    if (pop) return pop;
    pop = document.createElement("div");
    pop.className = "sds-preview";
    pop.setAttribute("role", "tooltip");
    pop.addEventListener("mouseenter", function () { clearTimeout(hideTimer); });
    pop.addEventListener("mouseleave", scheduleHide);
    document.body.appendChild(pop);
    return pop;
  }

  // Try each URL in turn; resolve with the first successful body, or null.
  // A target on another page can only be previewed if it can be fetched, which
  // fails silently when the book is opened from disk (file:// blocks fetch) or
  // served without clean-URL resolution. Warn once, so the cause is visible:
  // same-page previews keep working, which makes the failure look selective —
  // cross-page references, such as those to other sections, are the ones lost.
  var fetchWarned = false;
  function fetchFirst(urls) {
    var i = 0;
    function attempt() {
      if (i >= urls.length) {
        if (!fetchWarned) {
          fetchWarned = true;
          console.warn(
            "[sds hover-preview] impossibile recuperare " + urls[0] +
            ": le anteprime dei riferimenti a un'altra pagina richiedono che " +
            "il sito sia servito via http(s) (per esempio con `make serve`); " +
            "aprendo i file direttamente da disco (file://) il browser blocca " +
            "la richiesta. Le anteprime interne alla pagina continuano a " +
            "funzionare.");
        }
        return Promise.resolve(null);
      }
      return fetch(urls[i++], { credentials: "same-origin" })
        .then(function (res) { return res.ok ? res.text() : attempt(); })
        .catch(function () { return attempt(); });
    }
    return attempt();
  }

  function renderMath(node) {
    try {
      if (window.renderMathInElement && window.katex_options) {
        window.renderMathInElement(node, window.katex_options);
      }
    } catch (e) { /* never let math break the preview */ }
  }

  // Rewrite relative URLs so assets resolve against the *target* page, not the
  // page the popover currently lives on.
  function absolutize(node, baseHref) {
    var fix = function (sel, attr) {
      node.querySelectorAll(sel).forEach(function (n) {
        var v = n.getAttribute(attr);
        if (v && !/^(#|[a-z][a-z0-9+.-]*:|\/\/)/i.test(v)) {
          try { n.setAttribute(attr, new URL(v, baseHref).href); } catch (e) {}
        }
      });
    };
    fix("img[src]", "src");
    fix("source[src]", "src");
    fix("a[href]", "href");
  }

  function finalize(node, baseHref) {
    if (node.removeAttribute) node.removeAttribute("id");
    node.querySelectorAll("[id]").forEach(function (n) { n.removeAttribute("id"); });
    node.querySelectorAll("a.headerlink").forEach(function (n) { n.remove(); });
    absolutize(node, baseHref);
    return node;
  }

  // A section can be long and contains nested subsections, so preview only its
  // heading plus a few intro blocks up to the first child <section>.
  function sectionClone(sectionEl) {
    var kids = sectionEl.children, i, heading = null;
    for (i = 0; i < kids.length; i++) {
      if (/^h[1-6]$/.test(kids[i].tagName.toLowerCase())) { heading = kids[i]; break; }
    }
    if (!heading) return sectionEl.cloneNode(true);   // fallback: whole section
    var box = document.createElement("div");
    box.appendChild(heading.cloneNode(true));
    var count = 0, truncated = false;
    for (var j = i + 1; j < kids.length; j++) {
      if (kids[j].tagName.toLowerCase() === "section") { break; }
      if (count >= SECTION_MAX_BLOCKS) { truncated = true; break; }
      box.appendChild(kids[j].cloneNode(true));
      count++;
    }
    if (truncated) {
      var more = document.createElement("p");
      more.className = "sds-preview-more";
      more.textContent = "…";
      box.appendChild(more);
    }
    return box;
  }

  function buildContent(targetEl, kind, baseHref) {
    var inner = (kind === "section") ? sectionClone(targetEl) : targetEl.cloneNode(true);
    if (kind === "footnote") {
      // Keep the "[1]" label on the left, but de-link the back-reference
      // (a jump-to-reference link is pointless inside a preview).
      inner.querySelectorAll("a[role='doc-backlink']").forEach(function (a) {
        a.replaceWith(document.createTextNode(a.textContent));
      });
    }
    finalize(inner, baseHref);
    var wrap = document.createElement("div");
    wrap.className = "sds-preview-inner sds-preview-" + kind;
    wrap.appendChild(inner);
    return wrap;
  }

  function position(link) {
    var r = link.getBoundingClientRect();
    var sx = window.pageXOffset, sy = window.pageYOffset;
    pop.style.maxWidth = Math.min(440, window.innerWidth - 24) + "px";
    pop.style.left = "-9999px";
    pop.style.top = "0px";
    pop.style.display = "block";
    var pw = pop.offsetWidth, ph = pop.offsetHeight;
    var left = sx + r.left;
    left = Math.max(sx + 8, Math.min(left, sx + window.innerWidth - pw - 8));
    var fitsBelow = (r.bottom + ph + 12) <= window.innerHeight;
    var top = (fitsBelow || (r.top - ph - 8) < 0) ? (sy + r.bottom + 8)
                                                  : (sy + r.top - ph - 8);
    pop.style.left = left + "px";
    pop.style.top = top + "px";
  }

  function display(link, targetEl, kind, baseHref) {
    if (link !== currentLink) return;     // hover already moved elsewhere
    ensurePopover();
    pop.innerHTML = "";
    pop.appendChild(buildContent(targetEl, kind, baseHref));
    renderMath(pop);
    position(link);
    // force reflow so the entrance transition runs
    void pop.offsetWidth;
    pop.classList.add("sds-preview--visible");
  }

  function showFor(link) {
    var url;
    try { url = new URL(link.href); } catch (e) { return; }
    var frag = decodeURIComponent(url.hash.replace(/^#/, ""));
    if (!frag) return;

    var samePage = url.origin === location.origin && url.pathname === location.pathname;

    if (samePage) {
      var here = document.getElementById(frag);
      if (here) tryDisplay(link, here, location.href);
      return;
    }

    var base = url.origin + url.pathname;
    var use = function (doc) {
      var el = doc.getElementById(frag);
      if (el) tryDisplay(link, el, url.href);
    };
    if (docCache.has(base)) { use(docCache.get(base)); return; }

    // The site uses clean URLs (html_link_suffix=''); GitHub Pages and the dev
    // server both resolve /page -> page.html. Fall back to an explicit .html
    // suffix for plainer static servers.
    var candidates = [base];
    if (!/\.html$/.test(url.pathname) && !/\/$/.test(url.pathname)) {
      candidates.push(base + ".html");
    }
    fetchFirst(candidates).then(function (html) {
      if (html == null) return;
      var doc = new DOMParser().parseFromString(html, "text/html");
      docCache.set(base, doc);
      use(doc);
    });
  }

  function scheduleShow(link) {
    clearTimeout(showTimer);
    showTimer = setTimeout(function () { showFor(link); }, SHOW_DELAY);
  }
  function hideNow() {
    if (pop) {
      pop.classList.remove("sds-preview--visible");
      pop.style.display = "none";
    }
    currentLink = null;
  }
  function scheduleHide() {
    clearTimeout(hideTimer);
    hideTimer = setTimeout(hideNow, HIDE_DELAY);
  }

  function onEnter(e) {
    if (!isEnabled()) return;
    currentLink = e.currentTarget;
    clearTimeout(hideTimer);
    scheduleShow(currentLink);
  }
  function onLeave() {
    clearTimeout(showTimer);
    scheduleHide();
  }

  function bind() {
    if (TOUCH) return;
    // Only cross-references in the article body — not sidebar / on-page TOC nav.
    var root = document.querySelector(".bd-article") || document;
    root.querySelectorAll(
      'a.reference.internal[href*="#"], a.footnote-reference[href*="#"]'
    ).forEach(function (a) {
      a.addEventListener("mouseenter", onEnter);
      a.addEventListener("mouseleave", onLeave);
      a.addEventListener("focus", onEnter);
      a.addEventListener("blur", onLeave);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") hideNow();
    });
    window.addEventListener("scroll", function () {
      if (currentLink) scheduleHide();
    }, { passive: true });
  }

  // Minimal runtime API for readers (and for a future UI toggle).
  window.sdsHoverPreview = {
    enable: function () { try { localStorage.setItem("sdsHoverPreview", "on"); } catch (e) {} },
    disable: function () { try { localStorage.setItem("sdsHoverPreview", "off"); } catch (e) {} hideNow(); },
    toggle: function () { if (isEnabled()) { this.disable(); } else { this.enable(); } },
    isEnabled: isEnabled
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bind);
  } else {
    bind();
  }
})();
