"""Minimal Claude Messages API client (standard library only).

The model must answer through a tool call, so the reply is always JSON that matches the
tool's input schema. The document is sent as a cached block, so checking it in several
batches costs the document tokens once.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

API_URL = "https://api.anthropic.com/v1/messages"
API_VERSION = "2023-06-01"
DEFAULT_MODEL = "claude-sonnet-5-5"


class LLMError(RuntimeError):
    pass


def call_tool(*, system: str, cached_context: str, prompt: str, tool: dict, model: str = DEFAULT_MODEL,
              max_tokens: int = 8000, api_key: str | None = None, transport=None, retries: int = 4) -> dict:
    """Send one request that forces `tool` and return the tool input as a dict.

    `transport(payload: dict) -> dict` can replace the HTTP call (tests, mock runs).
    """
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "system": system,
        "tools": [tool],
        "tool_choice": {"type": "tool", "name": tool["name"]},
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": cached_context, "cache_control": {"type": "ephemeral"}},
                {"type": "text", "text": prompt},
            ],
        }],
    }
    response = transport(payload) if transport else _send(payload, api_key, retries)
    for block in response.get("content", []):
        if block.get("type") == "tool_use" and block.get("name") == tool["name"]:
            return block["input"]
    raise LLMError(f"no {tool['name']} call in response (stop_reason={response.get('stop_reason')})")


def _send(payload: dict, api_key: str | None, retries: int) -> dict:
    key = api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise LLMError("ANTHROPIC_API_KEY is not set")
    body = json.dumps(payload).encode("utf-8")
    for attempt in range(retries + 1):
        req = urllib.request.Request(API_URL, data=body, method="POST", headers={
            "x-api-key": key,
            "anthropic-version": API_VERSION,
            "content-type": "application/json",
        })
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:500]
            if e.code in (429, 500, 502, 503, 529) and attempt < retries:
                time.sleep(min(60, 2 ** attempt * 5))
                continue
            raise LLMError(f"HTTP {e.code}: {detail}") from None
        except urllib.error.URLError as e:
            if attempt < retries:
                time.sleep(2 ** attempt * 5)
                continue
            raise LLMError(f"network error: {e.reason}") from None
    raise LLMError("unreachable")
