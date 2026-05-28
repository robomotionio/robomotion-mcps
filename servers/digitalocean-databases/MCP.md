# DigitalOcean Databases

DigitalOcean's hosted Model Context Protocol server for managed databases.
Exposes tools to provision, manage, and monitor managed database clusters
(PostgreSQL, MySQL, Redis, and more).

## Transport

**http** — the agent connects to `https://databases.mcp.digitalocean.com/mcp`
over the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the database tools you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists via
`npx @digitalocean/mcp --services databases`, which runs the same database
tooling as a subprocess. This catalog entry uses the hosted http endpoint.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
