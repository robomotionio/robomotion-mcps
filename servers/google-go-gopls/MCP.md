# Go (gopls MCP)

The official Go language server, [gopls](https://go.dev/gopls), run in detached
MCP mode. Exposes tools to navigate, analyze, and edit Go code — symbol lookup,
references, diagnostics, and workspace context — for an agent working in a Go
repository.

## Transport

**stdio** — `gopls mcp` (the "detached" mode, which runs a standalone gopls
instance speaking MCP over stdin/stdout). It is spawned host-side by the
**credstdio** bridge; the agent attaches over a loopback socket and exchanges
only MCP JSON-RPC.

Requires gopls v0.20 or newer. Install with
`go install golang.org/x/tools/gopls@latest`.

(gopls also supports an "attached" HTTP/SSE mode via
`gopls serve -mcp.listen=localhost:8092` that shares an existing LSP session;
this entry uses the standalone stdio launch.)

## Credentials

None. gopls operates purely on local Go source on disk and makes no outbound
API calls, so there are no credentials to bind and nothing egresses.

## Source

- Feature docs: https://go.dev/gopls/features/mcp
- Upstream: https://github.com/golang/tools/tree/master/gopls
