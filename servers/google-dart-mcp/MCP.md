# Flutter / Dart MCP

The official Dart MCP server, distributed as part of the Dart SDK. Exposes tools
to analyze Dart and Flutter projects, run tests, manage `pub` dependencies,
search pub.dev, apply automated fixes, and connect to running apps through the
Dart Tooling Daemon (DTD) and the VM Service.

## Transport

**stdio** — `dart mcp-server`. The server is part of the Dart SDK (Dart 3.9.0 or
later; on earlier dev builds add `--experimental-mcp-server`). It is spawned
host-side by the **credstdio** bridge; the agent attaches over a loopback socket
and exchanges only MCP JSON-RPC.

## Credentials

None. This server requires no API token or identifier to run. It operates on the
local Dart/Flutter workspace and reaches pub.dev for package search.

## Source

- Upstream: https://github.com/dart-lang/ai/tree/main/pkgs/dart_mcp_server
- Listed at: https://github.com/google/mcp
