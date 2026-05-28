# Microsoft Sentinel Data Exploration

The data exploration tool collection of the Microsoft Sentinel Model Context
Protocol (MCP) server. It lets agents search for relevant tables and retrieve
data from the Microsoft Sentinel data lake using natural language and KQL.

## Tools

- `search_tables` — semantic search over the data lake table catalog; returns
  schemas to support query authoring.
- `query_lake` — run a single KQL query against a Microsoft Sentinel data lake
  workspace and return the raw result set.
- `list_sentinel_workspaces` — list available workspace name/ID pairs.
- `analyze_user_entity` / `analyze_url_entity` — start AI entity analysis.
- `get_entity_analysis` — poll for and retrieve entity analysis results.

## Transport

**http** — the agent connects to `https://sentinel.microsoft.com/mcp/data-exploration`
over the streamable-HTTP MCP transport.

## Credentials

No static token is configured. The server authenticates with an interactive
Microsoft Entra OAuth sign-in. The account must hold at least one of the
following roles:

- Security Administrator
- Security Operator
- Security Reader

The entity analyzer tools additionally require the **Security Copilot
Contributor** role (and consume Security Compute Units).

## Prerequisites

- A Microsoft Sentinel data lake.
- One of the supported AI-powered editors or agent-building platforms.

## Source

- Docs: https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-data-exploration-tool
- Short link: https://aka.ms/mcp/data-exploration
- Catalog: https://github.com/microsoft/mcp
