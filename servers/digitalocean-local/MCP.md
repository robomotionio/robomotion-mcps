# DigitalOcean (Local MCP)

The same DigitalOcean App Platform tooling as the remote server, but launched
locally as a **stdio** subprocess (`npx @digitalocean/mcp`).

## Transport

**stdio** — `npx @digitalocean/mcp --services apps,databases`.

Because stdio servers read their credential straight from the process
environment, Robomotion does **not** spawn this server inside the agent
sandbox. Instead the **credstdio** bridge (deskbot) spawns it host-side with the
real `DIGITALOCEAN_API_TOKEN` and exposes a per-flow loopback socket; the
sandboxed agent attaches to that socket and exchanges only MCP JSON-RPC. The
secret never enters the sandbox.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | DigitalOcean personal access token. Resolved from the bound vault item and injected host-side by credstdio. |

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- npm: `@digitalocean/mcp`
