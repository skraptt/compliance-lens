"""The Claude Code backend, tested with a fake `claude` executable (no login needed)."""
import json
import os
import stat
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from lens import claude_cli, llm  # noqa: E402
from lens.llm import LLMError  # noqa: E402

FAKE = textwrap.dedent(r'''
    #!/usr/bin/env python3
    import json, os, re, sys
    args = sys.argv[1:]
    log = os.environ["FAKE_LOG"]
    if args[:2] == ["auth", "status"]:
        print(json.dumps({"loggedIn": True, "authMethod": "claude.ai"})); sys.exit(0)
    stdin = sys.stdin.read()
    json.dump({"args": args, "cwd": os.getcwd(), "api_key_seen": "ANTHROPIC_API_KEY" in os.environ,
               "stdin": stdin}, open(log, "w"))
    if os.environ.get("FAKE_MODE") == "error":
        print(json.dumps({"type": "result", "is_error": True, "result": "Usage limit reached"})); sys.exit(1)
    keys = re.findall(r"^- key: (\S+)", stdin, re.M)
    out = {"findings": [{"check": k, "status": "missing", "paragraphs": [], "evidence": "", "explanation": "fake"} for k in keys]}
    if os.environ.get("FAKE_MODE") == "text":
        print(json.dumps({"type": "result", "is_error": False, "result": "Here you go: " + json.dumps(out)}))
    else:
        print(json.dumps({"type": "result", "is_error": False, "result": "", "structured_output": out}))
''').lstrip()

TOOL = {"name": "record_findings", "input_schema": {"type": "object", "properties": {"findings": {"type": "array"}}}}


class ClaudeCliTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.exe = Path(self.tmp.name, "claude")
        self.exe.write_text(FAKE)
        self.exe.chmod(self.exe.stat().st_mode | stat.S_IEXEC)
        self.log = Path(self.tmp.name, "log.json")
        self.env = {"FAKE_LOG": str(self.log), "ANTHROPIC_API_KEY": "sk-should-not-be-used"}
        self.old = {k: os.environ.get(k) for k in list(self.env) + ["FAKE_MODE"]}
        os.environ.update(self.env)

    def tearDown(self):
        for k, v in self.old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        self.tmp.cleanup()

    def call(self):
        t = claude_cli.make_transport("claude-sonnet-5-5", exe=str(self.exe))
        return llm.call_tool(system="SYS", cached_context="CONTEXT", prompt="- key: A.c1\n- key: B.c2",
                             tool=TOOL, transport=t)

    def test_structured_output_and_isolation(self):
        out = self.call()
        self.assertEqual([f["check"] for f in out["findings"]], ["A.c1", "B.c2"])
        seen = json.loads(self.log.read_text())
        a = seen["args"]
        self.assertFalse(seen["api_key_seen"], "API key must not reach claude")
        self.assertIn("lens-", seen["cwd"])                                  # empty temp folder
        self.assertEqual(a[a.index("--tools") + 1], "")                       # no built-in tools
        self.assertEqual(a[a.index("--system-prompt") + 1], "SYS")
        self.assertEqual(a[a.index("--model") + 1], "sonnet")
        self.assertIn("--strict-mcp-config", a)
        self.assertIn("--no-session-persistence", a)
        self.assertEqual(json.loads(a[a.index("--json-schema") + 1]), TOOL["input_schema"])
        self.assertTrue(seen["stdin"].startswith("CONTEXT"))

    def test_json_in_text_result(self):
        os.environ["FAKE_MODE"] = "text"
        self.assertEqual(len(self.call()["findings"]), 2)

    def test_error_is_reported(self):
        os.environ["FAKE_MODE"] = "error"
        with self.assertRaisesRegex(LLMError, "Usage limit reached"):
            self.call()

    def test_cli_end_to_end_with_fake_claude(self):
        env = dict(os.environ, PATH=f"{self.tmp.name}:{os.environ['PATH']}")
        with tempfile.TemporaryDirectory() as out:
            r = subprocess.run([sys.executable, "-m", "lens", "analyze", "demo/nordwind/profile.yaml", "--as-of",
                                "2026-11-18", "--backend", "claude-code", "--out", out],
                               cwd=ROOT, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            run = json.loads(Path(out, "findings.json").read_text())
            self.assertIn("via Claude Code", run["model"])
            self.assertTrue(all(f["status"] in ("missing", "upcoming", "not_applicable")
                                for d in run["documents"] for f in d["findings"]))


if __name__ == "__main__":
    unittest.main()
