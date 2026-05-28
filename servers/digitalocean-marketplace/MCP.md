# DigitalOcean Marketplace (Remote MCP)

DigitalOcean's hosted Marketplace Model Context Protocol server. Exposes tools
to discover and manage DigitalOcean Marketplace applications.

## Transport

**http** — the agent connects to `https://marketplace.mcp.digitalocean.com/mcp`
over the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the operations you intend to perform. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

The same tooling can be run locally as a stdio subprocess via
`npx @digitalocean/mcp --services marketplace`. This catalog entry uses the
hosted http endpoint instead.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://marketplace.mcp.digitalocean.com/mcp
