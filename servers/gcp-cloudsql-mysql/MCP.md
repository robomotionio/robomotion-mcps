# Cloud SQL for MySQL (Google Cloud)

Google's official managed remote Model Context Protocol server for Cloud SQL for
MySQL. Exposes tools to create, list, update, and manage MySQL instances and to
execute SQL, all through the Cloud SQL Admin API.

## Transport

**http** — the agent connects to `https://sqladmin.googleapis.com/mcp` over the
streamable-HTTP MCP transport. This is the shared global Cloud SQL endpoint
(MySQL, PostgreSQL, and SQL Server route through the same host).

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token with the `https://www.googleapis.com/auth/cloud-platform` scope (or `cloudsql.readonly` for read-only). Obtain via Application Default Credentials, a service account, or `gcloud auth print-access-token`. API keys are not accepted. |
| `GOOGLE_CLOUD_PROJECT` | yes | Your Google Cloud project ID, sent as the `x-goog-user-project` header for quota and billing routing. |

The token is referenced from the request header as
`Authorization=Bearer ${GOOGLE_CLOUD_ACCESS_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to
`sqladmin.googleapis.com`; the agent never holds the secret.

## Source

- Docs: https://docs.cloud.google.com/sql/docs/mysql/use-cloudsql-mcp
- Endpoint list: https://docs.cloud.google.com/mcp/supported-products
- Listing: https://github.com/google/mcp
