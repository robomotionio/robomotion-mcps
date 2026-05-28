# Microsoft Fabric

Microsoft's local-first MCP server for Microsoft Fabric. Exposes tools to explore
Fabric REST API specifications, item definition schemas, and development best
practices so agents can build and operate Fabric workloads with accurate,
up-to-date guidance.

## Transport

**stdio** — `npx -y @microsoft/fabric-mcp@latest server start --mode all`. It is
spawned host-side by the **credstdio** bridge; the agent attaches over a loopback
socket and exchanges only MCP JSON-RPC.

## Credentials

None. The server is local-first: it serves API specifications and guidance from
the bundled package and does not connect to your Fabric environment, so no vault
binding is required to run it.

## Source

- Upstream: https://github.com/microsoft/mcp/tree/main/servers/Fabric.Mcp.Server
- npm: `@microsoft/fabric-mcp`
