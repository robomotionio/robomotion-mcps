# Azure MCP Server

Microsoft's official Azure Model Context Protocol server. Exposes tools across
40+ Azure services — Resource Groups, Storage, Cosmos DB, Azure SQL, Monitor /
Log Analytics, Key Vault, AKS, and more — built on the official Azure SDK and
Azure Identity.

## Transport

**stdio** — `npx -y @azure/mcp@latest server start`. It is spawned host-side by
the **credstdio** bridge; the agent attaches over a loopback socket and never
sees the credentials.

## Credentials

The server uses the Azure Identity SDK (`DefaultAzureCredential`). For
unattended agent runs, authenticate with an Entra service principal via the
following environment variables:

| Variable | Required | Notes |
| --- | --- | --- |
| `AZURE_TENANT_ID` | yes | Entra (Azure AD) tenant ID. |
| `AZURE_CLIENT_ID` | yes | Service-principal / application (client) ID. |
| `AZURE_CLIENT_SECRET` | yes | Client secret for the service principal. |

All three are resolved from bound vault items and injected host-side by
credstdio. (Interactive `az login` / Azure PowerShell are also supported for
local use, but the env-var service principal is the unattended path.)

## Source

- Upstream: https://github.com/microsoft/mcp/tree/main/servers/Azure.Mcp.Server
- npm: `@azure/mcp`
