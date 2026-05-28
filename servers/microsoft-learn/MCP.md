# Microsoft Learn

Microsoft's official remote Model Context Protocol server for Microsoft Learn.
Exposes tools to search the official Microsoft documentation, fetch complete
articles, and search through code samples, backed by the Learn knowledge
service that powers Ask Learn and Copilot for Azure.

## Transport

**http** — the agent connects to `https://learn.microsoft.com/api/mcp` over the
streamable-HTTP MCP transport. The endpoint is for programmatic MCP clients
only; a browser request returns `405 Method Not Allowed`.

## Credentials

None. The Microsoft Learn MCP server is publicly available and requires no
authentication, so no header template ships and the sandbox holds no secret.

## Source

- Upstream/docs: https://learn.microsoft.com/training/support/mcp
- Catalog: https://github.com/microsoft/mcp
