# DigitalOcean App Platform (Remote MCP)

DigitalOcean's hosted Model Context Protocol server for App Platform. Exposes
tools to manage applications, including deployments and configurations.

## Transport

**http** — the agent connects to `https://apps.mcp.digitalocean.com/mcp` over
the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the App Platform tools you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

The same tooling can run locally as a stdio subprocess via
`npx @digitalocean/mcp --services apps`. This catalog entry uses the hosted
http endpoint; see also the `digitalocean-local` server for the local variant.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://apps.mcp.digitalocean.com/mcp
