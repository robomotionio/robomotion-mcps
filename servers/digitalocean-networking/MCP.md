# DigitalOcean Networking (Remote MCP)

DigitalOcean's hosted Model Context Protocol server for networking resources.
Exposes tools to manage domains, DNS records, certificates, firewalls, load
balancers, reserved IPs, BYOIP prefixes, VPCs, and CDNs.

## Transport

**http** — the agent connects to `https://networking.mcp.digitalocean.com/mcp`
over the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DIGITALOCEAN_API_TOKEN` | yes | A DigitalOcean personal access token with the scopes for the networking resources you intend to manage. |

Referenced from the request header as
`Authorization=Bearer ${DIGITALOCEAN_API_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to DigitalOcean; the
agent never holds the secret.

## Local alternative

A local stdio alternative exists via the bundled npx runtime:

```
npx @digitalocean/mcp --services networking
```

This catalog entry uses the hosted http endpoint instead.

## Source

- Upstream: https://github.com/digitalocean-labs/mcp-digitalocean
- Hosted endpoint: `https://networking.mcp.digitalocean.com/mcp`
