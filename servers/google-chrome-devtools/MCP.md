# Chrome DevTools MCP

Google's Chrome DevTools MCP server. Exposes tools to control a Chrome browser
through the DevTools protocol: navigate and interact with pages, inspect the DOM
and network requests, capture performance traces and screenshots, and evaluate
JavaScript in the page context.

## Transport

**stdio** — `npx -y chrome-devtools-mcp@latest`. It is spawned host-side by the
**credstdio** bridge; the agent attaches over a loopback socket and exchanges
only MCP JSON-RPC. A Chrome browser (current stable or newer) and a Node.js LTS
runtime are required on the host.

## Credentials

None. The server requires no authentication token or API key to operate.

## Configuration (optional)

| Variable | Notes |
| --- | --- |
| `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS` | Disable usage statistics collection. |
| `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS` | Disable periodic npm update checks. |

These are non-blocking convenience toggles, not credentials.

## Source

- Upstream: https://github.com/ChromeDevTools/chrome-devtools-mcp
- npm: `chrome-devtools-mcp`
