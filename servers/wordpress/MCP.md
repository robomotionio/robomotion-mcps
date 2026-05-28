# WordPress

A WordPress MCP server exposing tools to manage posts, pages, media, users,
comments, and site settings through the WordPress REST API.

## Transport

**stdio** — `npx -y @automattic/mcp-wordpress-remote`. The bridge connects to
your WordPress site using the credentials below. It is spawned host-side by the
**credstdio** bridge; the agent attaches over a loopback socket and never sees
the credentials.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `WORDPRESS_API_URL` | yes | Your site URL, e.g. `https://example.com`. |
| `WORDPRESS_USERNAME` | yes | A WordPress username. |
| `WORDPRESS_PASSWORD` | yes | An [application password](https://wordpress.org/documentation/article/application-passwords/) for that user (not the login password). |

All three are resolved from bound vault items and injected host-side by
credstdio.

## Source

- Upstream: https://github.com/Automattic/wordpress-mcp
- npm: `@automattic/mcp-wordpress-remote`
