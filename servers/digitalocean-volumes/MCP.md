# DigitalOcean Volumes

DigitalOcean's hosted Model Context Protocol server for block storage. Exposes
tools to manage block storage volumes and volume snapshots — create, resize,
attach to and detach from Droplets, snapshot, and delete.

## Transport

**http** — the agent connects to `https://volumes.mcp.digitalocean.com/mcp`
over the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with read/write scope for the resources you intend to manage. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative exists via
`npx @digitalocean/mcp --services volumes`, which spawns the same volume tooling
as a subprocess. This catalog entry uses the hosted http endpoint.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://volumes.mcp.digitalocean.com/mcp
