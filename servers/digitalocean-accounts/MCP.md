# DigitalOcean Accounts

DigitalOcean's hosted Model Context Protocol server for account management.
Exposes tools to get information about your DigitalOcean account, billing,
balance, invoices, and SSH keys.

## Transport

**http** — the agent connects to `https://accounts.mcp.digitalocean.com/mcp`
over the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists via
`npx @digitalocean/mcp --services accounts`, which spawns the same accounts
tooling as a subprocess. This catalog entry uses the hosted http endpoint.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://accounts.mcp.digitalocean.com/mcp
