# Google Analytics

Google's official Google Analytics MCP server. Exposes tools to explore your
Google Analytics 4 (GA4) account properties and run reports through the
Analytics Admin API and the Analytics Data API.

## Transport

**stdio** — `pipx run analytics-mcp`. It is spawned host-side by the
**credstdio** bridge; the agent attaches over a loopback socket and never sees
the credentials.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_APPLICATION_CREDENTIALS` | yes | Path to the credentials JSON used for Application Default Credentials, granted the `https://www.googleapis.com/auth/analytics.readonly` scope. |
| `GOOGLE_PROJECT_ID` | no | Your Google Cloud project ID. Recommended; some setups infer it from the credentials. |

Resolved from bound vault items and injected host-side by credstdio.

## Source

- Upstream: https://github.com/googleanalytics/google-analytics-mcp
- PyPI: `analytics-mcp`
