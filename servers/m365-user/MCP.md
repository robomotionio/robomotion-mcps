# Microsoft 365 User (Agent365)

Microsoft's Agent365 User MCP server. Exposes tools to retrieve the signed-in
user's profile details, their manager, team, and direct reports through the
Microsoft Graph APIs — the self-knowledge and organizational-awareness layer.

## Transport

**http** — the agent connects to
`https://agent365.svc.cloud.microsoft/agents/tenants/${MICROSOFT_TENANT_ID}/servers/mcp_MeServer`
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
- Endpoint: `https://agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_MeServer`
