# Azure DevOps

Microsoft's Azure DevOps MCP server. Provides tools for work items, Git
repositories, pull requests, pipelines, test plans, and wikis scoped to a single
Azure DevOps organization.

## Transport

**stdio** — `npx -y @azure-devops/mcp ${AZURE_DEVOPS_ORG}`. The organization
name is passed as a launch argument and expanded from the environment. The
server is spawned host-side by the **credstdio** bridge; the agent attaches over
a loopback socket.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `AZURE_DEVOPS_ORG` | yes | Your Azure DevOps organization name (the `dev.azure.com/<org>` slug). Expanded into the launch args. |
| `AZURE_DEVOPS_PAT` | no | Personal access token. If omitted, the server falls back to the host's Azure CLI login. |

Both values are resolved from bound vault items and injected host-side by
credstdio; neither enters the agent sandbox.

## Source

- Upstream: https://github.com/microsoft/azure-devops-mcp
- npm: `@azure-devops/mcp`
