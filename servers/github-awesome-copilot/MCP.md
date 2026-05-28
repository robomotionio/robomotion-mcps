# GitHub Awesome-Copilot

Microsoft's Awesome Copilot MCP server. Exposes tools to search and load the
community-curated GitHub Copilot customizations published in the
[github/awesome-copilot](https://github.com/github/awesome-copilot) repository —
agents, prompts, instructions, skills, collections, and chat modes.

## Transport

**stdio** — `docker run -i --rm ghcr.io/microsoft/mcp-dotnet-samples/awesome-copilot:latest`.
The container is spawned host-side by the **credstdio** bridge; the agent
attaches over a loopback socket and exchanges only MCP JSON-RPC. The server
fetches the latest catalog from GitHub into memory for the session (no local
disk cache).

## Credentials

None. This server takes no token and reads only public data from the
`github/awesome-copilot` repository.

## Source

- Upstream: https://github.com/microsoft/mcp-dotnet-samples/tree/main/awesome-copilot
- Image: `ghcr.io/microsoft/mcp-dotnet-samples/awesome-copilot:latest`
- Catalog: https://github.com/github/awesome-copilot
