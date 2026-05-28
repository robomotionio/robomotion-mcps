# Microsoft 365 Agents Toolkit

The Microsoft 365 Agents Toolkit MCP server connects AI coding agents to the
toolkit so you can scaffold, build, test, and deploy apps and agents for
Microsoft 365 and Microsoft 365 Copilot — including custom engine agents,
declarative agents, Teams apps, and Adaptive Cards.

## Transport

**stdio** — `npx -y @microsoft/m365agentstoolkit-mcp@latest server start`. It is
spawned host-side by the **credstdio** bridge; the agent attaches over a
loopback socket and exchanges only MCP JSON-RPC. Requires Node.js on the host.

## Credentials

No static credential is bound. The server is a local developer-tooling bridge;
when an operation needs Microsoft 365 access (e.g. provisioning or deploying),
authentication is performed interactively as a Microsoft sign-in, so no token
placeholder ships and the sandbox never holds a long-lived secret.

## Source

- Upstream: https://github.com/OfficeDev/microsoft-365-agents-toolkit
- Catalog listing: https://github.com/microsoft/mcp
- npm: `@microsoft/m365agentstoolkit-mcp`
