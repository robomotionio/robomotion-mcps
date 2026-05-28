# Google Cloud Observability

Google's MCP server for Cloud Observability. Exposes tools to query Cloud
Logging entries, Cloud Monitoring time series, and related telemetry across your
Google Cloud projects through natural language.

## Transport

**stdio** — `npx -y @google-cloud/observability-mcp`. It is spawned host-side by
the **credstdio** bridge; the agent attaches over a loopback socket and never
sees the credentials.

## Credentials

This server authenticates with **gcloud Application Default Credentials (ADC)**,
not an environment-variable token. Before use, the host running the bridge must
be authenticated:

```shell
gcloud auth login
gcloud auth application-default login
gcloud auth application-default set-quota-project YOUR_QUOTA_PROJECT_ID
```

The permissions of the MCP server are tied to the active gcloud account, and the
relevant APIs (e.g. Cloud Logging API, Cloud Monitoring API) must be enabled on
the quota project. No secret enters the agent sandbox.

For environments where a key file is impractical, the server also accepts a
service account via the `GOOGLE_CLIENT_EMAIL` and `GOOGLE_PRIVATE_KEY`
environment variables instead of ADC. When used, these are resolved host-side
and injected by credstdio.

## Source

- Upstream: https://github.com/googleapis/gcloud-mcp/tree/main/packages/observability-mcp
- npm: `@google-cloud/observability-mcp`
