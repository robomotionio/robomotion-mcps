# Markitdown

Microsoft's MarkItDown MCP server. Exposes a tool to convert files and URIs —
PDF, Word/Excel/PowerPoint, images (with OCR), audio (with transcription),
HTML, CSV, JSON, XML, ZIP archives, and more — into clean Markdown suitable for
LLM consumption.

## Transport

**stdio** — `uvx markitdown-mcp`. The server runs in STDIO mode by default and
is spawned host-side by the **credstdio** bridge; the agent attaches over a
loopback socket and exchanges only MCP JSON-RPC.

## Credentials

None. The server does not support authentication and requires no external API
tokens. It runs with the privileges of the user running it and converts the
files or URIs the agent supplies.

## Source

- Upstream: https://github.com/microsoft/markitdown
- MCP package: https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp
- PyPI: `markitdown-mcp`
