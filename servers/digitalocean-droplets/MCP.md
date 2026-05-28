# DigitalOcean Droplets (Remote MCP)

DigitalOcean's hosted Model Context Protocol server for droplets. Exposes tools
to create, manage, resize, snapshot, and monitor droplets (virtual machines) on
DigitalOcean.

## Transport

**http** — the agent connects to `https://droplets.mcp.digitalocean.com/mcp`
over the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the droplet operations you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists. Run it with
`npx @digitalocean/mcp --services droplets` (host-side via the credstdio bridge).
This catalog entry uses the hosted http endpoint.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Remote endpoint: https://droplets.mcp.digitalocean.com/mcp
