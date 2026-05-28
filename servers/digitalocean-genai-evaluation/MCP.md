# DigitalOcean GenAI Evaluation

DigitalOcean's hosted MCP server for the GenAI platform's evaluation features.
Exposes tools to manage and run evaluation workflows against your GenAI agents
and models.

## Transport

**http** — the agent connects to
`https://genai-evaluation.mcp.digitalocean.com/mcp` over the streamable-HTTP MCP
transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the GenAI evaluation tools you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists. Run it with:

```
npx @digitalocean/mcp --services genai-evaluation
```

This catalog entry uses the hosted http endpoint above.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://genai-evaluation.mcp.digitalocean.com/mcp
