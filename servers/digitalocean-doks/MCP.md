# DigitalOcean Kubernetes (DOKS)

DigitalOcean's hosted Model Context Protocol server for DigitalOcean Kubernetes
Service (DOKS). Exposes tools to manage Kubernetes clusters and node pools.

## Transport

**http** — the agent connects to `https://doks.mcp.digitalocean.com/mcp` over
the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the DOKS tools you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists via
`npx @digitalocean/mcp --services doks`, which spawns the server as a subprocess
and connects to `api.digitalocean.com`. This catalog entry uses the hosted http
endpoint instead.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://doks.mcp.digitalocean.com/mcp
