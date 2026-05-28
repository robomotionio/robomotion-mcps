# Azure Resource Manager (Remote MCP)

Microsoft's Azure Resource Manager (ARM) MCP Server (preview) is a cloud-hosted
Model Context Protocol endpoint that gives agents first-class access to Azure
infrastructure operations through Azure Resource Manager. It exposes tools to
generate, validate, and execute Azure Resource Graph (ARG) queries across all
Azure resource types, and to deploy and manage ARM template deployments.

## Transport

**http** — the agent connects to `https://mcp.management.azure.com` over the
streamable-HTTP MCP transport.

## Credentials

No static token is bound. The server authenticates with **Microsoft Entra ID**
using an interactive OAuth sign-in performed by the MCP client; all operations
run in the context of the signed-in user and respect your Azure RBAC
permissions and governance policies. Because there is no long-lived secret to
inject, this server ships with `headers: []` and no `env.required` file.

## Source

- Upstream: https://github.com/Azure/Azure-Resource-Manager-MCP
- Install / docs: https://aka.ms/JoinARMMCP
- Remote endpoint: `https://mcp.management.azure.com`

## Notes

The Azure Resource Manager MCP Server is in public preview and is provided
without a service-level agreement.
