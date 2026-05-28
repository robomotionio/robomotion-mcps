# BigQuery (Google Cloud)

Google Cloud's fully managed remote Model Context Protocol server for BigQuery.
Exposes tools to list datasets and tables, inspect schemas, and run SQL queries
against your BigQuery data warehouse.

## Transport

**http** — the agent connects to `https://bigquery.googleapis.com/mcp` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GCP_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token with the `https://www.googleapis.com/auth/bigquery` scope. Generate one with `gcloud auth application-default print-access-token`. The BigQuery MCP server uses OAuth with IAM and does not accept API keys. |

Referenced from the request header as `Authorization=Bearer ${GCP_ACCESS_TOKEN}`.
credproxy swaps the `RM_VAULT__…` placeholder for the real token at TLS egress to
`bigquery.googleapis.com`; the agent never holds the secret.

> Note: Google Cloud access tokens are short-lived (about one hour). Refresh the
> bound vault item before it expires, or bind a credential source that mints a
> fresh token per run.

## Source

- Docs: https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp
- MCP reference: https://docs.cloud.google.com/bigquery/docs/reference/mcp
- Supported products: https://docs.cloud.google.com/mcp/supported-products
