# DigitalOcean Insights

DigitalOcean's hosted "insights" Model Context Protocol server. Exposes tools to
monitor your resources and endpoints and alert you when they're slow,
unavailable, or their SSL certificates are expiring.

## Transport

**http** — the agent connects to `https://insights.mcp.digitalocean.com/mcp`
over the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the tools you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists:

```bash
npx @digitalocean/mcp --services insights
```

This catalog entry uses the hosted http endpoint instead.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://insights.mcp.digitalocean.com/mcp
