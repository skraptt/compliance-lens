/* Compliance Lens task pane. Talks to the local server on the same origin (python -m lens serve). */
/* global Office, Word, CLLogic */
(function () {
  "use strict";
  var L = CLLogic;
  var $ = function (id) { return document.getElementById(id); };

  var state = {
    meta: null,
    lastSelectionHash: null,
    selectionCache: {},
    scan: null,            // { paragraphs, findings }
    highlighted: [],       // Word paragraph indexes coloured by us in this session
    commentsSupported: false,
    autoTimer: null,
    busy: false
  };

  // ---------------------------------------------------------------- storage
  function local(key, value) {
    try {
      if (value === undefined) return JSON.parse(window.localStorage.getItem(key) || "null");
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (e) { /* storage can be unavailable in some Office hosts */ }
    return null;
  }
  function docSetting(key, value) {
    var s = Office.context.document.settings;
    if (value === undefined) return s.get(key);
    s.set(key, value);
    s.saveAsync(function () {});
    return null;
  }

  // ---------------------------------------------------------------- ui helpers
  function setStatus(text, isError) {
    var el = $("status");
    el.textContent = text;
    el.className = "status" + (isError ? " error" : "");
  }
  function busy(on, label) {
    state.busy = on;
    ["analyse-selection", "scan", "clear"].forEach(function (id) { $(id).disabled = on; });
    setStatus(on ? label : "Ready");
    if (on) $("status").insertAdjacentHTML("afterbegin", '<span class="spinner"></span>');
  }
  function switchTab(name) {
    document.querySelectorAll(".tabs button").forEach(function (b) {
      b.setAttribute("aria-selected", String(b.dataset.tab === name));
    });
    ["selection", "document", "setup"].forEach(function (t) { $("tab-" + t).hidden = t !== name; });
  }

  function settings() {
    var docTypes = docSetting("cl.docTypes") || [];
    var profile = local("cl.profile") || {};
    return {
      doc_types: docTypes,
      profile: profile,
      company: local("cl.company") || "",
      as_of: $("as-of").value || undefined
    };
  }
  function ready() {
    var s = settings();
    if (!s.doc_types.length) {
      setStatus("Choose the document type in Setup first.", true);
      switchTab("setup");
      return null;
    }
    return s;
  }

  function api(path, body) {
    var opts = body ? { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) } : {};
    return fetch(path, opts).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (data) {
        if (!r.ok) throw new Error(data.error || ("HTTP " + r.status));
        return data;
      });
    });
  }

  // ---------------------------------------------------------------- cards
  function card(f, opts) {
    var esc = L.escapeHtml;
    var where = (f.paragraphs && f.paragraphs.length && state.scan) ? f.paragraphs.map(function (pid) {
      var p = state.scan.paragraphs.find(function (x) { return x.pid === pid; });
      var sec = p && /^(\d+(?:\.\d+)*)\s/.exec(p.text);
      return sec ? "§" + sec[1] : pid;
    }).join(", ") : "";
    return '<div class="card ' + esc(f.status) + (opts && opts.clickable && f.paragraphs && f.paragraphs.length ? " clickable" : "") +
      '" data-key="' + esc(f.check) + '">' +
      '<div class="head"><span class="badge ' + esc(f.status) + '">' + esc(L.STATUS_LABEL[f.status] || f.status) + "</span>" +
      '<span class="badge basis ' + esc(f.basis) + '">' + esc(L.BASIS_LABEL[f.basis] || f.basis) + "</span>" +
      (where ? '<span class="where">' + esc(where) + "</span>" : "") +
      '<span class="key">' + esc(f.check) + "</span></div>" +
      '<div class="check">' + esc(f.check_text) + "</div>" +
      (f.explanation ? '<div class="why">' + esc(f.explanation) + "</div>" : "") +
      (f.evidence ? '<div class="quote">' + esc(f.evidence) + "</div>" : "") +
      '<div class="src">' + esc(f.item_title) + (f.legal_basis && f.legal_basis.length ? " — " + esc(f.legal_basis.join(", ")) : "") + "</div>" +
      "</div>";
  }

  // ---------------------------------------------------------------- selection
  function readSelection() {
    return Word.run(function (ctx) {
      var r = ctx.document.getSelection();
      r.load("text");
      return ctx.sync().then(function () { return r.text || ""; });
    });
  }

  function analyseSelection(fromAuto) {
    var s = ready();
    if (!s || state.busy) return Promise.resolve();
    return readSelection().then(function (text) {
      text = text.replace(/\s+/g, " ").trim();
      if (text.length < 40) {
        if (!fromAuto) $("selection-results").innerHTML = '<p class="empty">Select at least a full sentence.</p>';
        return null;
      }
      var key = L.hash(text + "|" + JSON.stringify(s));
      if (fromAuto && key === state.lastSelectionHash) return null;
      state.lastSelectionHash = key;
      if (state.selectionCache[key]) return renderSelection(state.selectionCache[key]);
      busy(true, "Analysing selection…");
      return api("/api/selection", Object.assign({ text: text }, s)).then(function (data) {
        state.selectionCache[key] = data.findings;
        renderSelection(data.findings);
        busy(false);
      });
    }).catch(function (e) { busy(false); setStatus(e.message, true); });
  }

  function renderSelection(findings) {
    var el = $("selection-results");
    if (!findings.length) {
      el.innerHTML = '<p class="empty">This passage does not touch any REMIT check for the selected document type.</p>';
      return;
    }
    el.innerHTML = findings.map(function (f) { return card(f); }).join("");
  }

  function onSelectionChanged() {
    if (!$("auto").checked) return;
    clearTimeout(state.autoTimer);
    state.autoTimer = setTimeout(function () { analyseSelection(true); }, 1500);
  }

  // ---------------------------------------------------------------- document scan
  function readParagraphs() {
    return Word.run(function (ctx) {
      var ps = ctx.document.body.paragraphs;
      ps.load("items/text,items/style");
      return ctx.sync().then(function () {
        return ps.items.map(function (p) { return { text: p.text, heading: L.isHeadingStyle(p.style) }; });
      });
    });
  }

  function scanDocument() {
    var s = ready();
    if (!s || state.busy) return;
    busy(true, "Scanning document… this can take a minute");
    readParagraphs().then(function (raw) {
      var paragraphs = L.buildParagraphs(raw);
      return api("/api/scan", Object.assign({ paragraphs: paragraphs.map(function (p) { return { text: p.text, heading: p.heading }; }) }, s))
        .then(function (data) {
          state.scan = { paragraphs: paragraphs, findings: data.findings };
          renderScan();
          var tasks = [];
          if ($("opt-highlight").checked) tasks.push(highlight);
          if ($("opt-comments").checked && state.commentsSupported) tasks.push(addComments);
          return tasks.reduce(function (p, t) { return p.then(t); }, Promise.resolve());
        });
    }).then(function () { busy(false); }).catch(function (e) { busy(false); setStatus(e.message, true); });
  }

  function renderScan() {
    var g = L.groupFindings(state.scan.findings);
    var c = g.counts;
    $("summary").innerHTML = '<div class="summary">' +
      '<div class="c"><b>' + c.conflicts + "</b>conflicts</div>" +
      '<div class="g"><b>' + c.gaps + "</b>gaps</div>" +
      "<div><b>" + c.weak + "</b>weak</div>" +
      "<div><b>" + c.acer + "</b>ACER</div>" +
      "<div><b>" + c.recs + "</b>recomm.</div>" +
      "<div><b>" + c.covered + "</b>covered</div></div>";
    var html = "";
    g.groups.forEach(function (grp) {
      if (!grp.items.length) return;
      var cards = grp.items.map(function (f) { return card(f, { clickable: true }); }).join("");
      // Law findings open; ACER expectations and recommendations folded to keep the list short.
      html += (grp.id === "acer" || grp.id === "recs")
        ? "<details><summary>" + L.escapeHtml(grp.title) + " (" + grp.items.length + ")</summary>" + cards + "</details>"
        : '<div class="group-title">' + L.escapeHtml(grp.title) + " (" + grp.items.length + ")</div>" + cards;
    });
    if (g.elsewhere.length) {
      html += "<details><summary>May be covered in another document (" + g.elsewhere.length + ")</summary>" +
        g.elsewhere.map(function (f) { return card(f); }).join("") + "</details>";
    }
    if (g.upcoming.length) {
      html += "<details><summary>Not yet in force (" + g.upcoming.length + ")</summary>" +
        g.upcoming.map(function (u) { return '<p class="small">' + L.escapeHtml(u.item_id + " " + u.title + " — " + u.why) + "</p>"; }).join("") + "</details>";
    }
    if (g.covered.length) {
      html += "<details><summary>Covered (" + g.covered.length + ")</summary>" +
        g.covered.map(function (f) { return card(f, { clickable: true }); }).join("") + "</details>";
    }
    $("document-results").innerHTML = html || '<p class="empty">No findings.</p>';
  }

  /* Run fn(paragraphItems) on the current Word paragraphs, after checking that the
     paragraphs we scanned are still where they were (the user may have edited). */
  function withScannedParagraphs(fn) {
    return Word.run(function (ctx) {
      var ps = ctx.document.body.paragraphs;
      ps.load("items/text");
      return ctx.sync().then(function () {
        var same = function (p) {
          var item = ps.items[p.index];
          return item && item.text.replace(/\s+/g, " ").trim() === p.text;
        };
        return Promise.resolve(fn(ps.items, same)).then(function () { return ctx.sync(); });
      });
    });
  }

  function highlight() {
    var targets = L.paragraphColours(state.scan.findings, state.scan.paragraphs);
    var byPid = {};
    state.scan.paragraphs.forEach(function (p) { byPid[p.pid] = p; });
    return withScannedParagraphs(function (items, same) {
      var skipped = 0;
      targets.forEach(function (t) {
        if (!same(byPid[t.pid])) { skipped++; return; }
        items[t.index].getRange("Whole").font.highlightColor = t.colour;
        state.highlighted.push(t.index);
      });
      if (skipped) setStatus(skipped + " paragraphs changed since the scan and were not highlighted.");
    });
  }

  function addComments() {
    var byPid = {};
    state.scan.paragraphs.forEach(function (p) { byPid[p.pid] = p; });
    return withScannedParagraphs(function (items, same) {
      state.scan.findings.forEach(function (f) {
        if (!f.primary || f.basis === "good_practice" || !L.isProblem(f.status) || !f.paragraphs || !f.paragraphs.length) return;
        var p = byPid[f.paragraphs[0]];
        if (p && same(p)) items[p.index].getRange("Whole").insertComment(L.commentText(f));
      });
    });
  }

  function clearHighlights() {
    if (!state.highlighted.length) { setStatus("Nothing to clear."); return; }
    var idx = state.highlighted.slice();
    Word.run(function (ctx) {
      var ps = ctx.document.body.paragraphs;
      ps.load("items");
      return ctx.sync().then(function () {
        idx.forEach(function (i) { if (ps.items[i]) ps.items[i].getRange("Whole").font.highlightColor = null; });
        return ctx.sync();
      });
    }).then(function () { state.highlighted = []; setStatus("Highlights cleared."); })
      .catch(function (e) { setStatus(e.message, true); });
  }

  function goToFinding(key) {
    if (!state.scan) return;
    var f = state.scan.findings.find(function (x) { return x.check === key; });
    if (!f || !f.paragraphs || !f.paragraphs.length) return;
    var p = state.scan.paragraphs.find(function (x) { return x.pid === f.paragraphs[0]; });
    if (!p) return;
    Word.run(function (ctx) {
      var ps = ctx.document.body.paragraphs;
      ps.load("items");
      return ctx.sync().then(function () {
        if (ps.items[p.index]) ps.items[p.index].select();
        return ctx.sync();
      });
    }).catch(function (e) { setStatus(e.message, true); });
  }

  // ---------------------------------------------------------------- setup tab
  function renderSetup() {
    var m = state.meta;
    var docTypes = docSetting("cl.docTypes") || [];
    $("doc-types").innerHTML = Object.keys(m.document_types).map(function (k) {
      return '<label><input type="checkbox" data-doctype="' + L.escapeHtml(k) + '"' + (docTypes.indexOf(k) >= 0 ? " checked" : "") + "> " +
        L.escapeHtml(m.document_types[k]) + "</label>";
    }).join("");

    var profile = local("cl.profile") || {};
    var seen = {};
    $("profile").innerHTML = m.profile_questions.map(function (q) {
      var flags = q.sets || q.sets_any_of || q.sets_one_of || [];
      return flags.map(function (flag) {
        if (seen[flag]) return "";
        seen[flag] = true;
        var label = flags.length > 1 ? m.addressees[flag] : q.text;
        return '<label><input type="checkbox" data-flag="' + L.escapeHtml(flag) + '"' + (profile[flag] ? " checked" : "") + "> " +
          L.escapeHtml(label || flag) + "</label>";
      }).join("");
    }).join("");

    $("company").value = local("cl.company") || "";
    $("meta").textContent = "Checklist v" + m.checklist_version + " · model " + m.model;
  }

  function bindSetup() {
    $("doc-types").addEventListener("change", function () {
      var picked = Array.prototype.map.call(document.querySelectorAll("[data-doctype]:checked"), function (el) { return el.dataset.doctype; });
      docSetting("cl.docTypes", picked);
      state.selectionCache = {};
      if (picked.length && !state.busy) setStatus("Ready");
    });
    $("profile").addEventListener("change", function () {
      var p = {};
      document.querySelectorAll("[data-flag]").forEach(function (el) { p[el.dataset.flag] = el.checked; });
      local("cl.profile", p);
      state.selectionCache = {};
    });
    $("company").addEventListener("change", function () { local("cl.company", $("company").value.trim()); });
  }

  // ---------------------------------------------------------------- start
  function init() {
    document.querySelectorAll(".tabs button").forEach(function (b) {
      b.addEventListener("click", function () { switchTab(b.dataset.tab); });
    });
    $("as-of").value = new Date().toISOString().slice(0, 10);
    $("analyse-selection").addEventListener("click", function () { analyseSelection(false); });
    $("scan").addEventListener("click", scanDocument);
    $("clear").addEventListener("click", clearHighlights);
    $("document-results").addEventListener("click", function (e) {
      var el = e.target.closest(".card.clickable");
      if (el) goToFinding(el.dataset.key);
    });
    $("auto").checked = !!local("cl.auto");
    $("auto").addEventListener("change", function () { local("cl.auto", $("auto").checked); });

    state.commentsSupported = Office.context.requirements.isSetSupported("WordApi", "1.4");
    if (!state.commentsSupported) {
      $("opt-comments").disabled = true;
      $("opt-comments").parentNode.title = "Comments need a newer version of Word (WordApi 1.4).";
    }
    Office.context.document.addHandlerAsync(Office.EventType.DocumentSelectionChanged, onSelectionChanged);

    api("/api/meta").then(function (m) {
      state.meta = m;
      renderSetup();
      bindSetup();
      setStatus("Ready");
      if (!(docSetting("cl.docTypes") || []).length) switchTab("setup");
    }).catch(function (e) {
      setStatus("Cannot reach the local server (python -m lens serve): " + e.message, true);
    });
  }

  Office.onReady(function (info) {
    if (info.host === Office.HostType.Word) init();
    else setStatus("Compliance Lens runs in Word.", true);
  });
})();
