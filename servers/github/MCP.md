# GitHub (Remote MCP)

GitHub's official remote Model Context Protocol server. Exposes tools to work
with repositories, issues, pull requests, GitHub Actions, code search, and more.

## Transport

**http** — the agent connects to `https://api.githubcopilot.com/mcp/` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | yes | A GitHub PAT (fine-grained or classic) with the scopes for the tools you intend to use. |

Referenced from the request header as
`Authorization=Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to GitHub; the agent
never holds the secret.

## Source

- Upstream: https://github.com/github/github-mcp-server
- Remote endpoint docs: https://docs.github.com/
