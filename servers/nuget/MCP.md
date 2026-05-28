# NuGet MCP Server

NuGet's official Model Context Protocol server. Exposes tools to search the
nuget.org gallery, inspect package metadata and available versions, and reason
about package dependencies for .NET projects.

## Transport

**stdio** — `dnx NuGet.Mcp.Server --source https://api.nuget.org/v3/index.json --yes`.
It is spawned host-side by the **credstdio** bridge; the agent attaches over a
loopback socket and exchanges only MCP JSON-RPC. Requires the .NET 10 SDK (which
provides the `dnx` command) on the host.

## Credentials

None. The server queries the public nuget.org package feed and does not require
any API token or sign-in.

## Source

- Upstream: https://www.nuget.org/packages/NuGet.Mcp.Server
- Docs: https://learn.microsoft.com/en-us/nuget/concepts/nuget-mcp-server
- Catalog: https://github.com/microsoft/mcp
