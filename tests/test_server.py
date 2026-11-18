"""Local server tests with a fake model (no API key, no network)."""
import json
import shutil
import ssl
import subprocess
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from lens import documents, server  # noqa: E402

PROFILE = {"market_participant": True, "registered_mp": True, "mp_disclosing": True, "has_group_facilities": True}


def fake_model(payload):
    """Answers every check it is asked about; for passages, only checks that mention 'publish'."""
    msg = payload["messages"][0]["content"]
    selection = "Selected passage" in msg[1]["text"]
    listing = msg[0]["text"] if selection else msg[1]["text"]
    keys = [l.split("key: ", 1)[1] for l in listing.splitlines() if l.startswith("- key: ")]
    if selection:
        keys = [k for k in keys if k.startswith("REMIT-DIS-02")]
        findings = [{"check": k, "status": "contradicts", "paragraphs": [], "evidence": "within 24 hours",
                     "explanation": "too slow"} for k in keys]
        findings.append({"check": "NOT-A-KEY.c1", "status": "covered", "paragraphs": [], "evidence": "", "explanation": ""})
        findings.append({"check": keys[0], "status": "missing", "paragraphs": [], "evidence": "", "explanation": ""})
    else:
        findings = [{"check": k, "status": "missing", "paragraphs": ["P2"], "evidence": "", "explanation": ""} for k in keys]
    return {"content": [{"type": "tool_use", "name": "record_findings", "input": {"findings": findings}}]}


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = server.App(ROOT / "obligations/remit.yaml", transport=fake_model, log=lambda m: None)
        cls.httpd = server.serve(app, port=0)
        cls.base = f"http://127.0.0.1:{cls.httpd.server_address[1]}"
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def get(self, path):
        with urllib.request.urlopen(self.base + path) as r:
            return r.status, r.headers.get("Content-Type"), r.read()

    def post(self, path, body):
        req = urllib.request.Request(self.base + path, data=json.dumps(body).encode(), method="POST",
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req) as r:
                return r.status, json.loads(r.read())
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read())

    def test_meta(self):
        code, ctype, body = self.get("/api/meta")
        meta = json.loads(body)
        self.assertEqual(code, 200)
        self.assertIn("IIP", meta["document_types"])
        self.assertTrue(meta["profile_questions"])

    def test_static_files_and_blocked_paths(self):
        code, ctype, body = self.get("/taskpane.html")
        self.assertEqual(code, 200)
        self.assertIn("text/html", ctype)
        self.assertIn(b"taskpane.js", body)
        self.assertEqual(self.get("/assets/icon-32.png")[1], "image/png")
        for bad in ("/manifest.xml", "/../lens/server.py", "/%2e%2e/lens/server.py", "/nope.js"):
            with self.assertRaises(urllib.error.HTTPError, msg=bad):
                self.get(bad)

    def test_selection_returns_only_touched_checks(self):
        code, data = self.post("/api/selection", {
            "text": "4.2 Publication takes place within 24 hours of the information becoming known.",
            "doc_types": ["IIP"], "profile": PROFILE, "as_of": "2026-11-18"})
        self.assertEqual(code, 200)
        keys = [f["check"] for f in data["findings"]]
        self.assertTrue(keys and all(k.startswith("REMIT-DIS-02") for k in keys))
        self.assertEqual(len(keys), len(set(keys)))                     # duplicate dropped
        self.assertTrue(all(f["status"] != "missing" for f in data["findings"]))

    def test_short_selection_and_validation(self):
        self.assertEqual(self.post("/api/selection", {"text": "too short", "doc_types": ["IIP"], "profile": PROFILE})[1]["findings"], [])
        code, data = self.post("/api/selection", {"text": "x" * 50, "doc_types": [], "profile": PROFILE})
        self.assertEqual(code, 400)
        self.assertIn("document type", data["error"])

    def test_scan_uses_the_add_in_paragraph_ids(self):
        md = documents.load(ROOT / "demo/nordwind/src/inside-information-policy.md")
        paras = [{"text": p.text, "heading": p.heading} for p in md]
        paras.insert(3, {"text": "   ", "heading": False})               # empty paragraphs are skipped
        code, data = self.post("/api/scan", {"paragraphs": paras, "doc_types": ["IIP"], "profile": PROFILE,
                                             "as_of": "2026-11-18"})
        self.assertEqual(code, 200)
        self.assertEqual(data["paragraph_count"], len(md))
        ran = [f for f in data["findings"] if f["status"] == "missing"]
        self.assertTrue(ran and all(f["paragraphs"] == ["P2"] for f in ran))

    def test_unknown_route(self):
        self.assertEqual(self.post("/api/nope", {})[0], 404)


@unittest.skipUnless(shutil.which("openssl"), "openssl not available")
class TlsTest(unittest.TestCase):
    def test_https(self):
        with tempfile.TemporaryDirectory() as d:
            cert, key = Path(d, "c.pem"), Path(d, "k.pem")
            subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-subj", "/CN=localhost",
                            "-keyout", str(key), "-out", str(cert), "-days", "1"], check=True, capture_output=True)
            app = server.App(ROOT / "obligations/remit.yaml", transport=fake_model, log=lambda m: None)
            httpd = server.serve(app, port=0, cert=cert, key=key)
            threading.Thread(target=httpd.serve_forever, daemon=True).start()
            try:
                ctx = ssl.create_default_context(cafile=str(cert))
                ctx.check_hostname = False
                with urllib.request.urlopen(f"https://127.0.0.1:{httpd.server_address[1]}/api/meta", context=ctx) as r:
                    self.assertEqual(r.status, 200)
            finally:
                httpd.shutdown()


if __name__ == "__main__":
    unittest.main()
