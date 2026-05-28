# OneDrive and SharePoint (Agent365)

Microsoft's Agent365 OneDrive and SharePoint MCP server. Exposes tools to
browse, search, read, and manage files and document libraries across OneDrive
and SharePoint, grounded in your tenant through the Microsoft Graph ODSP APIs.

## Transport

**http** — the agent connects to
`https://agent365.svc.cloud.microsoft/agents/tenants/${MICROSOFT_TENANT_ID}/servers/mcp_ODSPRemoteServer`
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
- Endpoint: `https://agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/mcp_ODSPRemoteServer`
