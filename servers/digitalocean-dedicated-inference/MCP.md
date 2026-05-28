# DigitalOcean Dedicated Inference

DigitalOcean's hosted Model Context Protocol server for **Dedicated Inference**.
Exposes tools to manage Dedicated Inference instances for GPU-accelerated model
serving.

## Transport

**http** — the agent connects to
`https://dedicated-inference.mcp.digitalocean.com/mcp` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with permission for the resources you intend to manage. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists. Run it with:

```
npx @digitalocean/mcp --services dedicated-inference
```

This catalog entry uses the hosted http endpoint above.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
