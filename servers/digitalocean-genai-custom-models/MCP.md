# DigitalOcean GenAI Custom Models (Remote MCP)

DigitalOcean's hosted Model Context Protocol server for the GenAI platform's
custom (bring-your-own) models. Exposes tools to import, list, update, and
delete custom models.

## Transport

**http** — the agent connects to
`https://genai-custom-models.mcp.digitalocean.com/mcp` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with permission to manage GenAI custom models. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative is available via the bundled DigitalOcean MCP package:

```
npx @digitalocean/mcp --services genai-custom-models
```

This catalog entry uses the hosted http endpoint above.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
