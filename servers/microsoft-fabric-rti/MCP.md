# Microsoft Fabric Real-Time Intelligence

A Microsoft Fabric Real-Time Intelligence (RTI) MCP server exposing tools to
query and manage Kusto / Eventhouse (KQL) databases and Fabric RTI workloads.

## Transport

**stdio** — `uvx microsoft-fabric-rti-mcp`. It is spawned host-side by the
**credstdio** bridge; the agent attaches over a loopback socket and never sees
the credentials.

## Authentication

The server authenticates through the Azure Identity
[`DefaultAzureCredential`](https://learn.microsoft.com/en-us/azure/developer/python/sdk/authentication/credential-chains)
chain (environment variables, Azure CLI, managed identity, interactive browser,
etc.). There is no static token to bind — credentials are resolved host-side by
the Azure Identity SDK; the server never stores or manages tokens directly.

## Configuration

All environment variables are optional — the server starts with demo defaults.
Set these to point at your own cluster and workspace:

| Variable | Required | Notes |
| --- | --- | --- |
| `KUSTO_SERVICE_URI` | no | Default cluster endpoint, e.g. `https://mycluster.westus.kusto.windows.net`. |
| `KUSTO_SERVICE_DEFAULT_DB` | no | Default database name (defaults to `NetDefaultDB`). |
| `FABRIC_API_BASE` | no | Microsoft Fabric API endpoint (defaults to `https://api.fabric.microsoft.com/v1`). |

When present, these are resolved from bound vault items and injected host-side by
credstdio.

## Source

- Upstream: https://github.com/microsoft/fabric-rti-mcp
- Docs: https://aka.ms/rti.mcp.repo
- PyPI: `microsoft-fabric-rti-mcp`
