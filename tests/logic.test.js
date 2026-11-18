// Run: node --test tests/logic.test.js
const test = require("node:test");
const assert = require("node:assert");
const L = require("../addin/logic.js");

test("buildParagraphs skips empty paragraphs and keeps Word indexes", () => {
  const p = L.buildParagraphs([{ text: "Title", heading: true }, { text: "  " }, { text: "1.1  Some\ttext" }]);
  assert.deepStrictEqual(p.map((x) => [x.pid, x.index, x.text, x.heading]), [
    ["P1", 0, "Title", true],
    ["P2", 2, "1.1 Some text", false],
  ]);
});

test("heading styles in several languages", () => {
  for (const s of ["Heading 1", "Title", "Überschrift 2", "Başlık 1"]) assert.ok(L.isHeadingStyle(s), s);
  assert.ok(!L.isHeadingStyle("Normal"));
});

const F = (o) => Object.assign({ primary: true, paragraphs: [], item_id: "X", item_title: "t", check_text: "c", legal_basis: [] }, o);

test("groupFindings sorts findings like the report", () => {
  const g = L.groupFindings([
    F({ check: "a", basis: "law", status: "contradicts" }),
    F({ check: "b", basis: "law", status: "missing" }),
    F({ check: "c", basis: "law", status: "partial" }),
    F({ check: "d", basis: "guidance", status: "missing" }),
    F({ check: "e", basis: "good_practice", status: "partial" }),
    F({ check: "f", basis: "law", status: "covered" }),
    F({ check: "g", basis: "law", status: "missing", primary: false }),
    F({ check: "h", basis: "law", status: "upcoming", item_id: "REP-04", explanation: "applies from 2027-01-01" }),
    F({ check: "i", basis: "law", status: "upcoming", item_id: "REP-04" }),
    F({ check: "j", basis: "law", status: "not_applicable" }),
  ]);
  assert.deepStrictEqual(g.counts, { conflicts: 1, gaps: 1, weak: 1, acer: 1, recs: 1, covered: 1 });
  assert.deepStrictEqual(g.elsewhere.map((f) => f.check), ["g"]);
  assert.strictEqual(g.upcoming.length, 1);
});

test("paragraphColours: worst status wins, recommendations do not colour", () => {
  const paras = [{ pid: "P1", index: 0 }, { pid: "P2", index: 3 }];
  const c = L.paragraphColours([
    F({ basis: "law", status: "missing", paragraphs: ["P2"] }),
    F({ basis: "law", status: "contradicts", paragraphs: ["P2"] }),
    F({ basis: "good_practice", status: "missing", paragraphs: ["P1"] }),
    F({ basis: "law", status: "covered", paragraphs: ["P1"] }),
    F({ basis: "law", status: "partial", paragraphs: ["P9"] }),
  ], paras);
  assert.deepStrictEqual(c, [{ pid: "P2", index: 3, colour: "Pink", status: "contradicts" }]);
});

test("escapeHtml and hash", () => {
  assert.strictEqual(L.escapeHtml('<a href="x">&</a>'), "&lt;a href=&quot;x&quot;&gt;&amp;&lt;/a&gt;");
  assert.strictEqual(L.hash("abc"), L.hash("abc"));
  assert.notStrictEqual(L.hash("abc"), L.hash("abd"));
});

test("commentText", () => {
  const t = L.commentText(F({ basis: "law", status: "contradicts", check_text: "Publish without delay.", explanation: "24h is too slow.", legal_basis: ["Article 4(1) REMIT"] }));
  assert.ok(t.startsWith("Compliance Lens · Conflict · Law"));
  assert.ok(t.includes("Article 4(1) REMIT"));
});
