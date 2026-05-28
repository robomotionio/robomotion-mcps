# Azure Kubernetes Service (AKS)

Microsoft's AKS MCP server. Exposes tools to inspect and operate Azure
Kubernetes Service clusters — cluster and node-pool details, networking,
diagnostics, and `kubectl`-driven workload operations — through the Azure
Resource Manager APIs.

## Transport

**stdio** — `docker run -i --rm ghcr.io/azure/aks-mcp:latest --transport stdio`.
The official Microsoft container is spawned host-side by the **credstdio**
bridge; the agent attaches over a loopback socket and never sees the
credentials.

The server accepts `--access-level readonly|readwrite|admin` (default
`readonly`). Append it to `args` to raise the permitted operation set.

## Credentials

The server authenticates to Azure with a service principal. Configure:

| Variable | Required | Notes |
| --- | --- | --- |
| `AZURE_CLIENT_ID` | yes | Service principal (app registration) client ID. |
| `AZURE_CLIENT_SECRET` | yes | Service principal client secret. |
| `AZURE_TENANT_ID` | yes | Azure AD tenant ID. |
| `AZURE_SUBSCRIPTION_ID` | no | Subscription to target; otherwise the SP default is used. |

All are resolved from bound vault items and injected host-side by credstdio.
Other auth modes documented upstream (workload identity, managed identity, or a
pre-authenticated `az login` session) are not used in the sandboxed flow.

## Source

- Upstream: https://github.com/Azure/aks-mcp
- Container image: `ghcr.io/azure/aks-mcp:latest`
- Catalog listing: https://github.com/microsoft/mcp
