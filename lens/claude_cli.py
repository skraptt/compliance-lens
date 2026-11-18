"""Run the model through the Claude Code CLI (`claude -p`) instead of the API.

This uses the Claude subscription you are logged in with in Claude Code (Pro, Max, ...),
so no API key or API credit is needed. Usage counts against the same limits as your
normal Claude and Claude Code use.

The call is made as a plain model call:
- every built-in and MCP tool is switched off and the system prompt is replaced, so
  Claude only reads the text it is given;
- it runs in an empty temporary folder, so no project CLAUDE.md or settings apply;
- ANTHROPIC_API_KEY is removed from the environment, because Claude Code would
  otherwise bill the API key instead of the subscription;
- the answer must match the tool's JSON schema (--json-schema).

The transport returns the same shape as the Messages API tool call, so the rest of the
engine does not change.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile

from .llm import LLMError

MODEL_ALIASES = {"claude-sonnet-5-5": "sonnet", "claude-opus-5-5": "opus", "claude-haiku-5-5": "haiku"}


def find_cli() -> str:
    exe = shutil.which("claude")
    if not exe:
        raise LLMError("Claude Code CLI ('claude') not found. Install Claude Code and log in with your Claude account.")
    return exe


def auth_status(exe: str | None = None) -> dict:
    exe = exe or find_cli()
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
    r = subprocess.run([exe, "auth", "status"], capture_output=True, text=True, env=env, timeout=60)
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return {"loggedIn": False, "authMethod": "unknown", "raw": r.stdout[-300:]}


def build_command(exe: str, system: str, schema: dict, model: str) -> list[str]:
    return [
        exe, "-p",
        "--output-format", "json",
        "--json-schema", json.dumps(schema),
        "--system-prompt", system,
        "--tools", "",
        "--disallowedTools", "mcp__*",
        "--strict-mcp-config",
        "--no-session-persistence",
        "--max-turns", "3",
        "--model", MODEL_ALIASES.get(model, model),
    ]


def _parse(stdout: str) -> dict:
    try:
        out = json.loads(stdout)
    except json.JSONDecodeError:
        raise LLMError(f"unexpected output from claude: {stdout[-300:]}") from None
    if out.get("is_error"):
        raise LLMError(f"claude reported an error: {str(out.get('result'))[:300]}")
    if isinstance(out.get("structured_output"), dict):
        return out["structured_output"]
    # Fallback: a JSON object in the text result.
    text = str(out.get("result") or "")
    m = re.search(r"\{.*\}", text, re.S)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass
    raise LLMError("claude returned no structured output")


def make_transport(model: str = "sonnet", timeout: int = 600, exe: str | None = None):
    exe = exe or find_cli()

    def transport(payload: dict) -> dict:
        tool = payload["tools"][0]
        text = "\n\n".join(block["text"] for block in payload["messages"][0]["content"])
        cmd = build_command(exe, payload["system"], tool["input_schema"], model)
        env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
        with tempfile.TemporaryDirectory(prefix="lens-") as cwd:
            try:
                r = subprocess.run(cmd, input=text, capture_output=True, text=True, env=env, cwd=cwd, timeout=timeout)
            except subprocess.TimeoutExpired:
                raise LLMError(f"claude did not answer within {timeout} s") from None
        if r.returncode != 0 and not r.stdout.strip():
            raise LLMError(f"claude exited with {r.returncode}: {r.stderr.strip()[-300:]}")
        return {"content": [{"type": "tool_use", "name": tool["name"], "input": _parse(r.stdout)}]}

    return transport
