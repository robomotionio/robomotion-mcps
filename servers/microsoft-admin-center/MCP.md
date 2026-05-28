# Microsoft Admin Center (Agent365)

Microsoft's Agent365 Admin Center MCP server. Exposes tools that integrate with
the Microsoft Admin Center APIs to provide tenant administration capabilities.

## Transport

**http** — the agent connects to
`https://agent365.svc.cloud.microsoft/agents/tenants/${MICROSOFT_TENANT_ID}/servers/mcp_AdminTools`
over the streamable-HTTP MCP transport. The host is fixed; your Microsoft Entra
tenant ID is bound into the request path.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `MICROSOFT_TENANT_ID` | yes | Your Microsoft Entra tenant ID (GUID). Bound into the endpoint path at hire time. |

The tenant identifier is referenced from the URL path as
`${MICROSOFT_TENANT_ID}`. credproxy swaps the `RM_VAULT__…` placeholder for the
real value at TLS egress to Agent365; the agent never holds the secret.

## Source

- Upstream: https://github.com/microsoft/mcp
- Endpoint: `https://agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_AdminTools`
