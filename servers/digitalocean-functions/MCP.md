# DigitalOcean Functions (Remote MCP)

DigitalOcean's hosted Model Context Protocol server for serverless Functions.
Exposes tools to manage function namespaces, actions, packages, triggers, and
activations.

## Transport

**http** — the agent connects to `https://functions.mcp.digitalocean.com/mcp`
over the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the Functions tools you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists via
`npx @digitalocean/mcp --services functions`, which runs the same Functions
tooling as a subprocess. This catalog entry uses the hosted http endpoint.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Remote endpoint: `https://functions.mcp.digitalocean.com/mcp`
