# DigitalOcean NFS

DigitalOcean's hosted Model Context Protocol server for NFS. Exposes tools to
manage NFS file shares and file share snapshots.

## Transport

**http** — the agent connects to `https://nfs.mcp.digitalocean.com/mcp` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with permissions for the NFS resources you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative also exists via the bundled DigitalOcean MCP package:

```
npx @digitalocean/mcp --services nfs
```

This catalog entry uses the hosted http endpoint above.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: https://nfs.mcp.digitalocean.com/mcp
