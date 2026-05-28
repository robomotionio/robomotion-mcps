# DigitalOcean (Remote MCP)

DigitalOcean's hosted Model Context Protocol server. Gives an agent tools to
manage **App Platform** resources — list and inspect apps, trigger and read
deployments, manage app-level databases, and read logs.

## Transport

**http** — the agent connects to `https://apps.mcp.digitalocean.com/mcp` over
the streamable-HTTP MCP transport. No local process is spawned.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with `app:read`/`app:write` scopes. |

The token is referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. At runtime Robomotion injects
only an `RM_VAULT__…` placeholder into the sandbox; the real token is swapped in
by **credproxy** at the moment the HTTPS request leaves for DigitalOcean. The
agent never holds the secret.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- DigitalOcean MCP docs: https://docs.digitalocean.com/

> Launch spec is a curated starting point — verify the endpoint and required
> token scopes against the current DigitalOcean MCP documentation.
