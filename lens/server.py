"""Local server for the Word add-in.

Serves the task pane files from addin/ and three JSON endpoints on the same HTTPS
origin (Office add-ins must load over HTTPS, and same origin avoids CORS and mixed
content). The Anthropic API key stays in this process; the add-in never sees it.

  GET  /api/meta        checklist version, profile questions, document types
  POST /api/selection   {text, doc_types, profile, company?, as_of?}      -> findings the passage touches
  POST /api/scan        {paragraphs: [{text, heading?}], doc_types, profile, company?, as_of?}
                                                                         -> findings for the whole document

Binds to 127.0.0.1 only.
"""
from __future__ import annotations

import datetime as dt
import json
import mimetypes
import ssl
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from . import analyze, checklist, documents, llm

ROOT = Path(__file__).resolve().parent.parent
ADDIN = ROOT / "addin"
DEMO_PROFILE = ROOT / "demo" / "nordwind" / "profile.yaml"
MAX_BODY = 5_000_000


class App:
    def __init__(self, checklist_path: Path, model: str = llm.DEFAULT_MODEL, transport=None, log=print):
        self.checklist = checklist.load(checklist_path)
        self.model = model
        self.transport = transport
        self.log = log
        self.lock = threading.Lock()

    # -- endpoints -----------------------------------------------------------------------
    def meta(self) -> dict:
        cl = self.checklist
        return {
            "checklist_version": cl["meta"]["version"],
            "profile_questions": cl.get("profile_questions", []),
            "addressees": cl.get("addressees", {}),
            "document_types": cl.get("document_types", {}),
            "model": self.model if self.transport is None else f"{self.model} (Claude Code)",
            "demo": self._demo(),
        }

    @staticmethod
    def _demo() -> dict | None:
        """The fictional Nordwind profile, so a new user can try the demo with one click."""
        try:
            import yaml
            d = yaml.safe_load(DEMO_PROFILE.read_text(encoding="utf-8"))
            return {"company": d["company"], "profile": {k: bool(v) for k, v in d["profile"].items()}}
        except Exception:  # noqa: BLE001 - the demo is optional
            return None

    def _checks(self, body: dict):
        profile = {k: bool(v) for k, v in (body.get("profile") or {}).items()}
        doc_types = body.get("doc_types") or []
        if not doc_types:
            raise ValueError("choose at least one document type")
        as_of = dt.date.fromisoformat(body["as_of"]) if body.get("as_of") else dt.date.today()
        checks = checklist.select(self.checklist, profile, doc_types, today=as_of)
        if not any(c.state == "run" for c in checks):
            raise ValueError("no REMIT checks apply with these settings. In Setup, tick what is true "
                             "for the company (at least that it trades on EU wholesale energy markets).")
        return checks, as_of

    def selection(self, body: dict) -> dict:
        text = str(body.get("text") or "")
        if len(text.strip()) < 20:
            return {"findings": [], "note": "Select at least a sentence."}
        if len(text) > 20_000:
            raise ValueError("selection too long for passage analysis; use Scan document")
        checks, as_of = self._checks(body)
        found = analyze.analyse_selection(text, body.get("company") or "the company", checks,
                                          model=self.model, transport=self.transport)
        return {"as_of": str(as_of), "findings": analyze.to_json(found)}

    def scan(self, body: dict) -> dict:
        raw = body.get("paragraphs") or []
        paras = documents.from_texts([(str(p.get("text", "")), bool(p.get("heading"))) for p in raw])
        if not paras:
            raise ValueError("the document is empty")
        checks, as_of = self._checks(body)
        found = analyze.analyse("document", body.get("company") or "the company", paras, checks,
                                model=self.model, transport=self.transport, log=self.log)
        return {"as_of": str(as_of), "paragraph_count": len(paras), "findings": analyze.to_json(found)}


def make_handler(app: App):
    class Handler(BaseHTTPRequestHandler):
        server_version = "ComplianceLens"

        def log_message(self, fmt, *args):  # quieter log
            app.log("%s %s" % (self.command, self.path))

        def _send(self, code: int, body: bytes, ctype: str):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def _json(self, code: int, obj):
            self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

        def do_GET(self):
            path = self.path.split("?", 1)[0]
            if path == "/api/meta":
                return self._json(200, app.meta())
            if path == "/":
                path = "/taskpane.html"
            target = (ADDIN / path.lstrip("/")).resolve()
            if not str(target).startswith(str(ADDIN.resolve())) or not target.is_file() or target.suffix == ".xml":
                return self._json(404, {"error": "not found"})
            ctype = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
            if ctype.startswith("text/") or ctype.endswith("javascript"):
                ctype += "; charset=utf-8"
            self._send(200, target.read_bytes(), ctype)

        def do_POST(self):
            path = self.path.split("?", 1)[0]
            routes = {"/api/selection": app.selection, "/api/scan": app.scan}
            if path not in routes:
                return self._json(404, {"error": "not found"})
            try:
                n = int(self.headers.get("Content-Length") or 0)
                if n > MAX_BODY:
                    return self._json(413, {"error": "request too large"})
                body = json.loads(self.rfile.read(n) or b"{}")
                return self._json(200, routes[path](body))
            except ValueError as e:
                return self._json(400, {"error": str(e)})
            except llm.LLMError as e:
                return self._json(502, {"error": f"model call failed: {e}"})
            except Exception as e:  # noqa: BLE001
                app.log(f"error: {e!r}")
                return self._json(500, {"error": "internal error"})

    return Handler


def serve(app: App, port: int = 3000, cert: Path | None = None, key: Path | None = None) -> ThreadingHTTPServer:
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(app))
    if cert and key:
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ctx.load_cert_chain(str(cert), str(key))
        httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
    return httpd


def default_certs() -> tuple[Path, Path]:
    d = Path.home() / ".office-addin-dev-certs"
    return d / "localhost.crt", d / "localhost.key"


def main(a) -> int:
    from .__main__ import backend_transport

    transport = backend_transport(a.backend, a.model)
    app = App(Path(a.checklist), model=a.model, transport=transport, log=lambda m: print(m, file=sys.stderr))
    cert = key = None
    if not a.no_tls:
        cert, key = (Path(a.cert), Path(a.key)) if a.cert else default_certs()
        if not cert.exists() or not key.exists():
            print(f"certificate not found at {cert}.\nRun once:  npx office-addin-dev-certs install\n"
                  "or pass --cert/--key, or --no-tls for API tests only.", file=sys.stderr)
            return 1
    httpd = serve(app, a.port, cert, key)
    scheme = "http" if a.no_tls else "https"
    via = "Claude Code subscription" if a.backend == "claude-code" else "Anthropic API"
    print(f"Compliance Lens on {scheme}://localhost:{a.port}  (checklist v{app.checklist['meta']['version']}, model {a.model} via {via})", file=sys.stderr)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0
