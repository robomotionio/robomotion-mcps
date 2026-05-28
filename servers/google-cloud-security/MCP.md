# Google Cloud Security (Chronicle SecOps)

The Google Security Operations (SecOps) MCP server from Google's
[`mcp-security`](https://github.com/google/mcp-security) suite. Exposes tools to
search UDM events, query and manage detection rules, inspect alerts and cases,
and run threat detection across your Chronicle SecOps instance.

## Transport

**stdio** — `uvx --from google-secops-mcp secops_mcp`. It is spawned host-side by
the **credstdio** bridge; the agent attaches over a loopback socket and never
sees the credentials.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `CHRONICLE_PROJECT_ID` | yes | Your Google Cloud project ID bound to the Chronicle instance. |
| `CHRONICLE_CUSTOMER_ID` | yes | Your Chronicle customer / instance UUID. |
| `CHRONICLE_REGION` | yes | Chronicle region, e.g. `us`, `eu`, or `asia`. |
| `SECOPS_SA_PATH` | no | Path to a Google Cloud service-account key JSON. If omitted, Application Default Credentials are used. |

The identifiers and the service-account key are resolved from bound vault items
and injected host-side by credstdio.

## Source

- Upstream: https://github.com/google/mcp-security
- PyPI: `google-secops-mcp` (run via `uvx --from google-secops-mcp secops_mcp`)
