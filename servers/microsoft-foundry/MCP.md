# Microsoft Foundry (Remote MCP)

Foundry MCP Server (preview) is Microsoft's cloud-hosted Model Context Protocol
endpoint for Azure AI Foundry. It exposes curated tools that let agents perform
read and write operations against Foundry services — discovering models,
inspecting projects, and interacting with Azure resources — without calling the
backend APIs directly.

## Transport

**http** — the agent connects to `https://mcp.ai.azure.com` over the
streamable-HTTP MCP transport.

## Credentials

No static token is bound. The server authenticates with **Microsoft Entra ID**
using an interactive OAuth sign-in (On-Behalf-Of flow) performed by the MCP
client; access is governed by your Azure role assignments (Contributor or higher
on the target Foundry project). Because there is no long-lived secret to inject,
this server ships with `headers: []` and no `env.required` file.

## Source

- Upstream / docs: https://learn.microsoft.com/azure/ai-foundry/mcp/get-started
- Remote endpoint: `https://mcp.ai.azure.com`

## Notes

Foundry MCP Server is in public preview and is provided without a service-level
agreement.
