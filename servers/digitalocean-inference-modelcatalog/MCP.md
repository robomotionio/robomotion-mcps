# DigitalOcean Inference Model Catalog (Remote MCP)

DigitalOcean's hosted Inference Model Catalog Model Context Protocol server.
Exposes tools to browse the DigitalOcean Inference model catalog, search for
models, and get model cards.

## Transport

**http** — the agent connects to
`https://inference-modelcatalog.mcp.digitalocean.com/mcp` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio equivalent is available via the bundled DigitalOcean MCP package:

```bash
npx @digitalocean/mcp --services inference-modelcatalog
```

This catalog entry uses the hosted http endpoint.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
