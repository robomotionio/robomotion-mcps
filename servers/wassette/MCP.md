# Wassette

Microsoft's security-oriented runtime that runs WebAssembly Components via MCP.
It exposes tools to load, manage, and invoke Wasm Components, each isolated by
the Wasmtime sandbox for browser-grade, capability-scoped execution.

## Transport

**stdio** — `wassette run`. The server is spawned host-side by the
**credstdio** bridge; the agent attaches over a loopback socket and exchanges
only MCP JSON-RPC.

> Note: the `wassette` binary must be installed on the host (see the install
> script in the upstream repo). It is not published to npm/PyPI, so there is no
> `npx`/`uvx` bootstrap — the host provides the executable.

## Credentials

None. Wassette requires no API token or identifier to start.

## Source

- Upstream: https://github.com/microsoft/wassette
- Docs: https://microsoft.github.io/wassette/
- MCP client setup: https://github.com/microsoft/wassette/blob/main/docs/mcp-clients.md
