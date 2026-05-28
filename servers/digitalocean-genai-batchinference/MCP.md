# DigitalOcean GenAI Batch Inference

DigitalOcean's hosted GenAI Batch Inference MCP server. Exposes tools to create,
manage, and monitor batch inference jobs for asynchronous bulk AI processing.

## Transport

**http** — the agent connects to
`https://genai-batchinference.mcp.digitalocean.com/mcp` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the batch inference operations you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local stdio alternative

A local stdio variant of the same service is available via the bundled
DigitalOcean MCP package:

```
npx @digitalocean/mcp --services genai-batchinference
```

This catalog entry uses the hosted http endpoint above.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://genai-batchinference.mcp.digitalocean.com/mcp
