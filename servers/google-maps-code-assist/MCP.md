# Google Maps Platform Code Assist

Google's official Maps Platform Code Assist toolkit, exposed as an MCP server.
It grounds your AI coding assistant in the latest Google Maps Platform
documentation, official code samples, and expert-authored best practices so the
Maps code it generates is accurate, optimal, and up to date.

## Transport

**stdio** — `npx -y @googlemaps/code-assist-mcp@latest`. It is spawned host-side
by the **credstdio** bridge; the agent attaches over a loopback socket and
exchanges only MCP JSON-RPC.

## Credentials

None. The Code Assist toolkit's documentation-retrieval tools do not require a
Google Maps API key. (If you generate code that calls live Maps APIs, you
provide a Maps API key in that code separately — it is not consumed by this
server.)

## Source

- Upstream: https://github.com/googlemaps/platform-ai/tree/main/packages/code-assist
- npm: `@googlemaps/code-assist-mcp`
- Docs: https://developers.google.com/maps/ai/mcp
