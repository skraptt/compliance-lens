/* Compliance Lens task pane: pure functions (no Office.js), so they can be tested in Node. */
(function (root) {
  "use strict";

  var BASIS_LABEL = { law: "Law", guidance: "ACER", good_practice: "Good practice" };
  var STATUS_LABEL = { covered: "Covered", partial: "Partial", missing: "Missing", contradicts: "Conflict" };

  // Same order and rules as lens/report.py.
  var GROUPS = [
    { id: "conflicts", title: "Conflicts with REMIT", test: function (f) { return f.basis === "law" && f.status === "contradicts"; } },
    { id: "gaps", title: "Gaps (required by law)", test: function (f) { return f.basis === "law" && f.status === "missing"; } },
    { id: "weak", title: "Weak points", test: function (f) { return f.basis === "law" && f.status === "partial"; } },
    { id: "acer", title: "ACER expects", test: function (f) { return f.basis === "guidance" && isProblem(f.status); } },
    { id: "recs", title: "Recommendations", test: function (f) { return f.basis === "good_practice" && isProblem(f.status); } }
  ];

  function isProblem(status) {
    return status === "contradicts" || status === "missing" || status === "partial";
  }

  /* Word paragraphs -> what the server needs. Empty paragraphs are skipped, exactly as
     lens/documents.py does, and `index` remembers the Word paragraph each pid came from. */
  function buildParagraphs(raw) {
    var out = [];
    for (var i = 0; i < raw.length; i++) {
      var text = String(raw[i].text || "").replace(/\s+/g, " ").trim();
      if (!text) continue;
      out.push({ pid: "P" + (out.length + 1), index: i, text: text, heading: !!raw[i].heading });
    }
    return out;
  }

  function isHeadingStyle(style) {
    return /^(heading|title|überschrift|titel|başlık)/i.test(String(style || ""));
  }

  /* Scan findings -> groups for the pane. Only the document's primary checks count;
     others are "may be covered elsewhere". */
  function groupFindings(findings) {
    var groups = GROUPS.map(function (g) { return { id: g.id, title: g.title, items: [] }; });
    var elsewhere = [], upcoming = {}, covered = [];
    var order = { contradicts: 0, missing: 1, partial: 2 };
    findings.forEach(function (f) {
      if (f.status === "upcoming") { upcoming[f.item_id] = { item_id: f.item_id, title: f.item_title, why: f.explanation }; return; }
      if (f.status === "not_applicable") return;
      if (!f.primary) { if (isProblem(f.status)) elsewhere.push(f); return; }
      if (f.status === "covered") { covered.push(f); return; }
      for (var i = 0; i < GROUPS.length; i++) {
        if (GROUPS[i].test(f)) { groups[i].items.push(f); return; }
      }
    });
    groups.forEach(function (g) { g.items.sort(function (a, b) { return order[a.status] - order[b.status]; }); });
    return {
      groups: groups,
      elsewhere: elsewhere,
      upcoming: Object.keys(upcoming).sort().map(function (k) { return upcoming[k]; }),
      covered: covered,
      counts: {
        conflicts: groups[0].items.length, gaps: groups[1].items.length, weak: groups[2].items.length,
        acer: groups[3].items.length, recs: groups[4].items.length, covered: covered.length
      }
    };
  }

  /* Highlight colour for a paragraph: the most serious finding pointing at it wins.
     Only law and ACER findings colour the document; recommendations do not. */
  function paragraphColours(findings, paragraphs) {
    var rank = { contradicts: 3, partial: 2, missing: 1 };
    var best = {};
    findings.forEach(function (f) {
      if (!f.primary || f.basis === "good_practice" || !rank[f.status]) return;
      (f.paragraphs || []).forEach(function (pid) {
        if (!best[pid] || rank[f.status] > rank[best[pid]]) best[pid] = f.status;
      });
    });
    var byPid = {};
    paragraphs.forEach(function (p) { byPid[p.pid] = p; });
    return Object.keys(best).filter(function (pid) { return byPid[pid]; }).map(function (pid) {
      return { pid: pid, index: byPid[pid].index, colour: best[pid] === "contradicts" ? "Pink" : "Yellow", status: best[pid] };
    });
  }

  function commentText(f) {
    var parts = ["Compliance Lens · " + STATUS_LABEL[f.status] + " · " + BASIS_LABEL[f.basis], f.check_text];
    if (f.explanation) parts.push(f.explanation);
    if (f.legal_basis && f.legal_basis.length) parts.push(f.legal_basis.join(", "));
    return parts.join("\n");
  }

  /* Small stable hash for caching selection results. */
  function hash(s) {
    var h = 2166136261;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return (h >>> 0).toString(36);
  }

  function escapeHtml(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  var api = {
    BASIS_LABEL: BASIS_LABEL, STATUS_LABEL: STATUS_LABEL, isProblem: isProblem,
    buildParagraphs: buildParagraphs, isHeadingStyle: isHeadingStyle, groupFindings: groupFindings,
    paragraphColours: paragraphColours, commentText: commentText, hash: hash, escapeHtml: escapeHtml
  };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.CLLogic = api;
})(this);
