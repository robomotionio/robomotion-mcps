# Microsoft Dev Box

The Microsoft Dev Box MCP server. Exposes tools to manage cloud-based developer
workstations: list projects and dev box pools, create / start / stop / delete
dev boxes, manage shutdown schedules, and apply customizations through the Dev
Box control plane.

## Transport

**stdio** — `npx -y @microsoft/devbox-mcp@latest`. It is spawned host-side by
the **credstdio** bridge; the agent attaches over a loopback socket and
exchanges only MCP JSON-RPC.

## Credentials

This server does **not** take a static token. It authenticates with
`DefaultAzureCredential`, which walks a credential chain (environment variables,
managed identity, Azure CLI, Azure PowerShell, Windows SSO / WAM). On the
deskbot host you sign in once via `az login` (or an equivalent Azure
credential); the server reuses that session. No vault-bound secret enters the
agent sandbox.

You need the **Dev Box User** role (or higher) on the target Dev Box resources.

## Source

- Upstream: https://github.com/microsoft/devbox-mcp-server
- npm: `@microsoft/devbox-mcp`
- Docs: https://learn.microsoft.com/en-us/azure/dev-box/overview-what-is-dev-box-mcp-server
