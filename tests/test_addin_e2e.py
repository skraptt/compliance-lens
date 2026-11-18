"""End-to-end test of the task pane in headless Chrome, with a fake Office.js standing in for Word.

The local server runs with a replayed model (examples/nordwind-blind-run/responses.json), the
fake Word document holds the Nordwind inside information policy, and the test clicks through
Setup, Selection and Document. Skipped when Playwright or Chrome is not installed.
Screenshots go to $LENS_SCREENSHOTS if set.
"""
import json
import os
import shutil
import sys
import threading
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from lens import documents, server  # noqa: E402
from lens.__main__ import replay_transport  # noqa: E402

try:
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover
    sync_playwright = None

CHROME = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")

FAKE_OFFICE = r"""
(function () {
  var doc = window.__fakeDoc;
  function paragraphItems() {
    return doc.paragraphs.map(function (p, i) {
      return {
        text: p.text, style: p.style,
        getRange: function () {
          return {
            font: { set highlightColor(v) { doc.highlights[i] = v; } },
            insertComment: function (t) { doc.comments.push([i, t]); }
          };
        },
        select: function () { doc.selected = i; }
      };
    });
  }
  window.Office = {
    HostType: { Word: "Word" },
    EventType: { DocumentSelectionChanged: "documentSelectionChanged" },
    onReady: function (cb) { setTimeout(function () { cb({ host: "Word" }); }, 0); },
    context: {
      requirements: { isSetSupported: function () { return true; } },
      document: {
        settings: { _d: {}, get: function (k) { return this._d[k]; }, set: function (k, v) { this._d[k] = v; }, saveAsync: function (cb) { cb && cb(); } },
        addHandlerAsync: function (t, h) { window.__selectionChanged = h; }
      }
    }
  };
  window.Word = {
    run: function (fn) {
      var ctx = {
        document: {
          getSelection: function () { return { load: function () {}, get text() { return doc.selection; } }; },
          body: { paragraphs: { load: function () {}, items: paragraphItems() } }
        },
        sync: function () { return Promise.resolve(); }
      };
      return Promise.resolve(fn(ctx));
    }
  };
})();
"""


def selection_model(payload):
    msg = payload["messages"][0]["content"]
    keys = [l.split("key: ", 1)[1] for l in msg[0]["text"].splitlines() if l.startswith("- key: ")]
    pick = {"REMIT-DIS-02.c1": "contradicts", "REMIT-DIS-02.c3": "contradicts"} if "24 hours" in msg[1]["text"] else {}
    return {"content": [{"type": "tool_use", "name": "record_findings", "input": {"findings": [
        {"check": k, "status": s, "paragraphs": [], "evidence": "Publication takes place within 24 hours",
         "explanation": "24 hours is not disclosure without delay; ACER expects one hour."}
        for k, s in pick.items() if k in keys]}}]}


@unittest.skipUnless(sync_playwright and CHROME, "playwright or chrome not available")
class AddinE2E(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        responses = json.loads((ROOT / "examples/nordwind-blind-run/responses.json").read_text(encoding="utf-8"))
        replay = replay_transport(responses, "inside-information-policy.docx")

        def transport(payload):
            if "Selected passage" in payload["messages"][0]["content"][1]["text"]:
                return selection_model(payload)
            return replay(payload)

        cls.app = server.App(ROOT / "obligations/remit.yaml", transport=transport, log=lambda m: None)
        cls.httpd = server.serve(cls.app, port=0)
        cls.base = f"http://127.0.0.1:{cls.httpd.server_address[1]}"
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()
        paras = documents.load(ROOT / "demo/nordwind/inside-information-policy.docx")
        cls.fake_doc = {"paragraphs": [{"text": p.text, "style": "Heading 1" if p.heading else "Normal"} for p in paras],
                        "selection": "", "highlights": {}, "comments": [], "selected": None}
        cls.shots = os.environ.get("LENS_SCREENSHOTS")

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def shot(self, page, name):
        if self.shots:
            Path(self.shots).mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(Path(self.shots, name)), full_page=True)

    def test_pane(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": 360, "height": 900})
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.route("https://appsforoffice.microsoft.com/**", lambda r: r.fulfill(
                body=f"window.__fakeDoc = {json.dumps(self.fake_doc)};" + FAKE_OFFICE, content_type="text/javascript"))
            page.goto(self.base + "/taskpane.html")

            # First start: no document type yet -> Setup tab
            page.wait_for_selector("#doc-types input")
            self.assertFalse(page.is_hidden("#tab-setup"))
            page.check('[data-doctype="IIP"]')
            self.assertEqual(page.inner_text("#status"), "Ready")           # warning clears once a type is ticked
            page.click("#demo")                                              # one-click demo profile
            self.assertTrue(page.is_checked('[data-flag="algo_trader"]'))
            self.assertFalse(page.is_checked('[data-flag="lng_market_participant"]'))
            self.assertEqual(page.input_value("#company"), "Nordwind Energy Trading GmbH")
            self.assertTrue(page.is_checked('[data-doctype="IIP"]'))
            page.check('[data-flag="dea_provider ppat"]')                   # one answer sets both flags
            self.assertTrue(page.is_checked('[data-flag="ppat"]'))
            page.uncheck('[data-flag="dea_provider ppat"]')                 # PPAT stays implied while DEA is ticked
            page.uncheck('[data-flag="ppat"]')
            self.assertFalse(page.is_checked('[data-flag="ppat"]'))
            for flag in ("market_participant", "registered_mp", "mp_disclosing", "has_group_facilities"):
                page.check(f'[data-flag="{flag}"]')
            page.fill("#company", "Nordwind Energy Trading GmbH")
            page.dispatch_event("#company", "change")
            page.fill("#as-of", "2026-11-18")
            self.shot(page, "1-setup.png")

            # Selection
            page.click('[data-tab="selection"]')
            page.evaluate("window.__fakeDoc.selection = '4.2 Publication takes place within 24 hours of the information becoming known to Nordwind Trading.'")
            page.click("#analyse-selection")
            page.wait_for_selector("#selection-results .card")
            cards = page.locator("#selection-results .card")
            self.assertEqual(cards.count(), 2)
            self.assertIn("conflict", cards.first.inner_text().lower())
            self.shot(page, "2-selection.png")

            # Auto mode: a new selection is analysed after the pause, a repeated one is not
            page.check("#auto")
            page.evaluate("window.__fakeDoc.selection = '3.2 Inside information may only be shared with colleagues who need it to perform their duties (need-to-know).'")
            page.evaluate("window.__selectionChanged()")
            page.wait_for_function("document.querySelector('#selection-results').innerText.includes('does not touch')", timeout=5000)

            # Document scan with highlights and comments
            page.click('[data-tab="document"]')
            page.check("#opt-comments")
            page.click("#scan")
            page.wait_for_selector("#summary .summary")
            summary = page.inner_text("#summary")
            self.assertIn("conflicts", summary)
            doc = page.evaluate("window.__fakeDoc")
            self.assertTrue(doc["highlights"], "no paragraphs highlighted")
            self.assertIn("Pink", doc["highlights"].values())
            self.assertTrue(doc["comments"])
            self.assertTrue(all(t.startswith("Compliance Lens") for _, t in doc["comments"]))
            # highlighted paragraph indexes point at the right text (§4.2 is a conflict)
            idx_42 = next(i for i, p in enumerate(self.fake_doc["paragraphs"]) if p["text"].startswith("4.2 "))
            self.assertEqual(doc["highlights"].get(str(idx_42)), "Pink")
            self.shot(page, "3-document.png")

            # Clicking a finding selects its paragraph
            page.locator("#document-results .card.clickable").first.click()
            self.assertIsNotNone(page.evaluate("window.__fakeDoc.selected"))

            # Clear removes our highlights
            page.click("#clear")
            page.wait_for_function("Object.values(window.__fakeDoc.highlights).every(v => v === null)")

            self.assertEqual(errors, [], errors)
            browser.close()


if __name__ == "__main__":
    unittest.main()
