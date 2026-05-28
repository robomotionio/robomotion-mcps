# Playwright

Microsoft's Playwright MCP server. Exposes tools to drive a real browser using
Playwright — navigate to URLs, click, type, fill forms, capture accessibility
snapshots and screenshots, handle dialogs and tabs, and run end-to-end web
automation.

## Transport

**stdio** — `npx @playwright/mcp@latest`. It is spawned host-side by the
**credstdio** bridge; the agent attaches over a loopback socket and exchanges
only MCP JSON-RPC.

## Credentials

None. This server runs a local browser and requires no API key, token, or other
external credential, so nothing is bound at hire time.

## Source

- Upstream: https://github.com/microsoft/playwright-mcp
- npm: `@playwright/mcp`
