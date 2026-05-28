# robomotion-mcps

A curated catalog of **MCP (Model Context Protocol) servers** that Robomotion
hub "Teams" agents can use as a first-class capability — the MCP analog of
[`robomotion-skills`](https://github.com/robomotionio/robomotion-skills).

Each server is browseable and toggleable in the Agent Editor's **MCP** tab, and
its declared credentials flow into the Setup wizard as vault-binding steps —
exactly like Skills.

## Layout

```
robomotion-mcps/
  README.md
  build-index.py        # generates index.yaml from the servers/ tree
  validate.sh           # checks the server contract + index drift
  index.yaml            # generated discovery manifest (committed)
  servers/
    <name>/
      .robomotion/
        mcp.yaml         # metadata + launch spec (authoritative)
      MCP.md             # human-readable docs (shown in Designer / hub)
      env.required       # one env var per line — blocks the run until bound
      env.optional       # one env var per line — never blocks the run
```

## `mcp.yaml`

The authoritative per-server file. It is the skill.yaml fields plus a **launch
spec**:

```yaml
type: mcp
name: digitalocean
title: DigitalOcean
author: DigitalOcean
version: 1.0.0
license: MIT
category: DevOps
summary: One-line description shown on the card.
source_url: https://github.com/digitalocean-labs/mcp-digitalocean
tags: [digitalocean, devops]
transport: stdio          # stdio | http
command: npx              # stdio: executable
args: ["@digitalocean/mcp", "--services", "apps,databases"]   # stdio: argv
url: ""                   # http: endpoint URL
headers: []               # http: ["Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}"]
timeout: 300
```

`${VAR}` references in `headers` (http) and `args` (stdio) are expanded from the
agent's environment at runtime.

## Security model

The agent sandbox **never holds a real secret**. Two transports, two paths:

- **http** servers ride the existing **credproxy**. The credential is referenced
  from a header template (`Authorization=Bearer ${TOKEN}`); the sandbox only sees
  an `RM_VAULT__…` placeholder, which credproxy swaps for the real value at TLS
  egress to the MCP endpoint.
- **stdio** servers run through the **credstdio** bridge. Robomotion (deskbot)
  spawns the real server **host-side** with the real credentials and exposes a
  per-flow loopback socket; the sandboxed agent attaches to that socket and
  exchanges only MCP JSON-RPC. The secret never enters the sandbox.

## Building the index

```bash
python3 build-index.py          # regenerate index.yaml
python3 build-index.py --check  # CI: fail if index.yaml is stale
./validate.sh                   # validate the server contract + index drift
```

`index.yaml` is committed so the Designer and api-service can fetch one file per
repo instead of probing every server directory.
