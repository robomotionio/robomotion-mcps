# DigitalOcean Container Registry (Remote MCP)

DigitalOcean's hosted "docr" Model Context Protocol server. Exposes tools to
manage Container Registry repositories, tags, manifests, and garbage collection.

## Transport

**http** — the agent connects to `https://docr.mcp.digitalocean.com/mcp` over
the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the Container Registry tools you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists. Spawn the bundled server with the docr
service enabled:

```bash
npx @digitalocean/mcp --services docr
```

This catalog entry uses the hosted http endpoint above.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Remote endpoint: `https://docr.mcp.digitalocean.com/mcp`
