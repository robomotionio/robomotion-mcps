# Microsoft Clarity

A Microsoft Clarity MCP server exposing tools to query your Clarity project's
data through the [Clarity Data Export API](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-data-export-api).
Retrieve live insights — traffic, engagement time, scroll depth, popular pages,
and behavior metrics — broken down by dimensions such as browser, device, OS,
country/region, and source.

## Transport

**stdio** — `npx @microsoft/clarity-mcp-server --clarity_api_token=${CLARITY_API_TOKEN}`.
It is spawned host-side by the **credstdio** bridge; the agent attaches over a
loopback socket and never sees the credentials.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `CLARITY_API_TOKEN` | yes | A Clarity API access token. Generate one as a project admin from **Settings → Data Export → Generate new API token**. |

The token is referenced from the launch args; credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to
`www.clarity.ms`, so the agent never holds the secret.

## Source

- Upstream: https://github.com/microsoft/clarity-mcp-server
- npm: `@microsoft/clarity-mcp-server`
- API docs: https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-data-export-api
