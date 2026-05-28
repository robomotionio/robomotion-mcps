#!/usr/bin/env python3
"""Generate index.yaml — the discovery manifest for this MCP-server repo.

Walks ``servers/<name>/.robomotion/mcp.yaml`` (our authoritative per-server
metadata + launch spec). For each server we emit one flat row carrying the
same attribution fields a skill row has (name, title, summary, author,
source_url, license, version, category, tags, env) PLUS the launch spec the
runtime needs to start the server:

    transport  stdio | http
    command    stdio: executable (e.g. npx)
    args       stdio: argv list
    url        http:  endpoint URL
    headers    http:  list of "Header=Value" templates (may reference ${ENV})
    timeout    seconds

MCP servers have no "group / inner skill" nesting — each ``servers/<name>``
is a standalone unit — so the index is a single flat ``servers:`` list (the
analog of the skills index's standalone ``skills:`` list).

Output is deterministic (no timestamps) so CI drift-checks are stable.
Content hashes capture "what changed".

Usage::

    python3 build-index.py            # write index.yaml
    python3 build-index.py --check    # exit 1 if index.yaml is out of date
"""

from __future__ import annotations

import hashlib
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

SCHEMA_VERSION = 1
ROBOMOTION_DIR = ".robomotion"
MCP_YAML = "mcp.yaml"
SERVERS_DIR = "servers"


# ---------- env helpers ------------------------------------------------------

def env_names(path: str) -> list:
    if not os.path.isfile(path):
        return []
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            name = line.split("=", 1)[0].strip()
            if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", name):
                out.append(name)
    return out


# ---------- file / hash helpers ----------------------------------------------

def _prune(dirs: list) -> None:
    dirs[:] = [d for d in dirs if d != "__pycache__"]


def _is_artifact(f: str) -> bool:
    return f.endswith((".pyc", ".pyo"))


def file_list(d: str) -> list:
    out = []
    for root, dirs, files in os.walk(d):
        _prune(dirs)
        for f in files:
            if _is_artifact(f):
                continue
            out.append(os.path.relpath(os.path.join(root, f), d).replace(os.sep, "/"))
    return sorted(out)


def dir_content_hash(d: str) -> str:
    h = hashlib.sha256()
    for root, dirs, files in os.walk(d):
        _prune(dirs)
        for f in sorted(files):
            if _is_artifact(f):
                continue
            p = os.path.join(root, f)
            rel = os.path.relpath(p, d).replace(os.sep, "/")
            h.update(rel.encode())
            h.update(b"\0")
            with open(p, "rb") as fh:
                h.update(fh.read())
            h.update(b"\0")
    return h.hexdigest()[:12]


# ---------- mcp.yaml discovery -----------------------------------------------

def load_mcp_yaml(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def find_servers(repo_root: str) -> list:
    """Return relative paths of every servers/<name> holding
    .robomotion/mcp.yaml."""
    servers_root = os.path.join(repo_root, SERVERS_DIR)
    if not os.path.isdir(servers_root):
        return []
    out = []
    for name in sorted(os.listdir(servers_root)):
        d = os.path.join(servers_root, name)
        if not os.path.isdir(d) or name.startswith("."):
            continue
        if os.path.isfile(os.path.join(d, ROBOMOTION_DIR, MCP_YAML)):
            out.append(f"{SERVERS_DIR}/{name}")
    return out


def read_server(repo_root: str, server_rel: str) -> dict:
    server_abs = os.path.join(repo_root, server_rel)
    my = load_mcp_yaml(os.path.join(server_abs, ROBOMOTION_DIR, MCP_YAML))
    name = my.get("name") or os.path.basename(server_rel)
    transport = (my.get("transport") or "stdio").strip()

    entry = {
        "name": name,
        "path": server_rel,
        "title": my.get("title") or name,
        "summary": my.get("summary", ""),
        "version": str(my.get("version", "")),
        "author": my.get("author", ""),
        "source_url": my.get("source_url", ""),
        "license": my.get("license", ""),
        "category": my.get("category", "") or "",
        "tags": my.get("tags", []) or [],
        # ---- launch spec ----
        "transport": transport,
        "command": my.get("command", "") or "",
        "args": my.get("args", []) or [],
        "url": my.get("url", "") or "",
        "headers": my.get("headers", []) or [],
        "timeout": int(my.get("timeout", 300) or 300),
        # ---- env contract (verbatim from env.required / env.optional) ----
        "env": {
            "required": env_names(os.path.join(server_abs, "env.required")),
            "optional": env_names(os.path.join(server_abs, "env.optional")),
        },
        "content_hash": dir_content_hash(server_abs),
        "files": file_list(server_abs),
    }
    return entry


# ---------- main -------------------------------------------------------------

def build(repo_root: str) -> dict:
    servers = [read_server(repo_root, r) for r in find_servers(repo_root)]
    return {
        "schema_version": SCHEMA_VERSION,
        "servers": servers,
    }


def main() -> int:
    repo_root = os.path.abspath(os.path.dirname(__file__))
    index = build(repo_root)
    text = yaml.dump(
        index,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
        width=120,
    )
    out = os.path.join(repo_root, "index.yaml")
    n_servers = len(index["servers"])

    if "--check" in sys.argv:
        current = open(out, encoding="utf-8").read() if os.path.isfile(out) else ""
        if current != text:
            sys.stderr.write("index.yaml is stale — run `python3 build-index.py` and commit.\n")
            return 1
        print(f"index.yaml up to date ({n_servers} server(s))")
        return 0

    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote index.yaml: {n_servers} server(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
