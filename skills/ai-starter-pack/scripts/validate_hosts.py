#!/usr/bin/env python3
"""Validate AI Starter Pack host adapter metadata."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOSTS_PATH = ROOT / "references" / "hosts.json"
README_PATH = ROOT.parents[1] / "README.md"
INSTALL_PATH = ROOT.parents[1] / "INSTALL.md"
SKILL_PATH = ROOT / "SKILL.md"
DEDUP_PATH = ROOT / "references" / "dedup.md"
CURSOR_RULE_PATH = ROOT.parents[1] / ".cursor" / "rules" / "ai-starter-pack.mdc"

ALLOWED_TARGET_FORMATS = {
    "skill-folder",
    "cursor-rule",
    "windsurf-rule",
    "copilot-instruction",
    "read-only"
}
ALLOWED_STATUSES = {"verified", "needs-verification", "best-effort"}
FORBIDDEN_TEXT = [
    ".codex" + "/skills",
    "~/.codex" + "/skills",
    "global" + ".mdc",
    "~/.cursor" + "/rules",
    "PIN" + "_ME"
]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def fail(message: str) -> None:
    print(f"host-registry: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_list(value: object, field: str) -> list:
    if not isinstance(value, list):
        fail(f"{field} must be a list")
    return value


def main() -> None:
    data = json.loads(HOSTS_PATH.read_text())

    if data.get("schema_version") != 1:
        fail("schema_version must be 1")
    if not DATE_RE.match(str(data.get("last_verified", ""))):
        fail("last_verified must be YYYY-MM-DD")

    target_formats = data.get("target_formats", {})
    missing_formats = ALLOWED_TARGET_FORMATS - set(target_formats)
    if missing_formats:
        fail(f"target_formats missing: {', '.join(sorted(missing_formats))}")

    hosts = require_list(data.get("hosts"), "hosts")
    if not hosts:
        fail("hosts must not be empty")

    seen_ids: set[str] = set()
    seen_aliases: set[str] = set()
    for host in hosts:
        if not isinstance(host, dict):
            fail("each host must be an object")
        host_id = host.get("id")
        if not isinstance(host_id, str) or not host_id:
            fail("host.id must be a non-empty string")
        if host_id in seen_ids:
            fail(f"duplicate host id: {host_id}")
        seen_ids.add(host_id)

        aliases = require_list(host.get("aliases", []), f"{host_id}.aliases")
        for alias in aliases:
            if not isinstance(alias, str) or not alias:
                fail(f"{host_id}.aliases contains a non-string alias")
            if alias in seen_ids or alias in seen_aliases:
                fail(f"duplicate host alias: {alias}")
            seen_aliases.add(alias)

        for field in ("display_name", "target_format", "rails_target"):
            if not isinstance(host.get(field), str) or not host[field]:
                fail(f"{host_id}.{field} must be a non-empty string")

        status = host.get("status")
        if status not in ALLOWED_STATUSES:
            fail(f"{host_id}.status must be one of {sorted(ALLOWED_STATUSES)}")
        if host["target_format"] not in ALLOWED_TARGET_FORMATS:
            fail(f"{host_id}.target_format is unknown: {host['target_format']}")

        last_verified = host.get("last_verified")
        if status == "verified":
            if not DATE_RE.match(str(last_verified)):
                fail(f"{host_id}.last_verified must be YYYY-MM-DD for verified hosts")
            if not require_list(host.get("source_urls"), f"{host_id}.source_urls"):
                fail(f"{host_id}.source_urls must not be empty for verified hosts")

        for field in ("detection_hints", "source_urls", "notes"):
            for item in require_list(host.get(field, []), f"{host_id}.{field}"):
                if not isinstance(item, str):
                    fail(f"{host_id}.{field} must contain only strings")

        for field in ("context_files", "skill_or_rule_dirs"):
            scoped = host.get(field)
            if not isinstance(scoped, dict):
                fail(f"{host_id}.{field} must be an object")
            for scope, entries in scoped.items():
                if scope not in {"project", "global", "admin", "plugin"}:
                    fail(f"{host_id}.{field}.{scope} is not a known scope")
                for entry in require_list(entries, f"{host_id}.{field}.{scope}"):
                    if not isinstance(entry, str):
                        fail(f"{host_id}.{field}.{scope} must contain only strings")

    scanned = "\n".join(
        path.read_text()
        for path in (
            HOSTS_PATH,
            README_PATH,
            INSTALL_PATH,
            SKILL_PATH,
            DEDUP_PATH,
            CURSOR_RULE_PATH
        )
        if path.exists()
    )
    for forbidden in FORBIDDEN_TEXT:
        if forbidden in scanned:
            fail(f"forbidden stale token found: {forbidden}")

    for doc_path in (README_PATH, INSTALL_PATH, DEDUP_PATH):
        if "hosts.json" not in doc_path.read_text():
            fail(f"{doc_path.relative_to(ROOT.parents[1])} must mention hosts.json")

    print(f"ok {len(hosts)} hosts validated")


if __name__ == "__main__":
    main()
