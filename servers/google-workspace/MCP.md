# Google Workspace (Remote MCP)

A Google Workspace MCP server exposing tools across Gmail, Drive, Calendar,
Docs, Sheets, and Slides, served over the streamable-HTTP MCP transport.

## Transport

**http** — the agent connects to your Workspace MCP deployment's `/mcp`
endpoint. Google Workspace MCP servers are typically **self-hosted** (they run
the Google OAuth flow and broker the Google APIs), so the `url` in this entry is
a placeholder you must point at your own deployment.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_WORKSPACE_MCP_TOKEN` | no | Bearer token your deployment accepts (if it gates access). Swapped into the Authorization header at egress by credproxy. |

> This entry is a template. Deploy a Google Workspace MCP server (see the
> upstream project), set `url` to its `/mcp` endpoint, and adjust the auth
> header to match how your deployment authenticates callers.

## Source

- Upstream: https://github.com/taylorwilsdon/google_workspace_mcp
