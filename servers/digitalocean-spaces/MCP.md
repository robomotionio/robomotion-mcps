# DigitalOcean Spaces

DigitalOcean's hosted Spaces Model Context Protocol server. Exposes tools to
manage Spaces object storage buckets and Spaces access keys for S3-compatible
storage.

## Transport

**http** — the agent connects to `https://spaces.mcp.digitalocean.com/mcp` over
the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the Spaces tools you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists via
`npx @digitalocean/mcp --services spaces`, which runs the Spaces tooling as a
subprocess. This catalog entry uses the hosted http endpoint instead.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://spaces.mcp.digitalocean.com/mcp
