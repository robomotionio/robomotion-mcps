# DigitalOcean Docs

DigitalOcean's hosted documentation MCP server. Exposes tools to search and
retrieve DigitalOcean's public product documentation from the agent.

## Transport

**http** — the agent connects to `https://docs.mcp.digitalocean.com/mcp` over
the streamable-HTTP MCP transport.

## Credentials

None. The documentation endpoint is public, so no API token is required and no
credential ever enters the sandbox.

## Local alternative

A local stdio variant is also available via the DigitalOcean MCP package:

```
npx @digitalocean/mcp --services docs
```

This catalog entry uses the hosted http endpoint above.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://docs.mcp.digitalocean.com/mcp
