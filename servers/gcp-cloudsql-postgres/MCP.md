# Cloud SQL for PostgreSQL (Google Cloud)

Google's managed remote Model Context Protocol server for Cloud SQL for
PostgreSQL. Exposes tools to create and manage instances, databases, users, and
backups, and to run SQL against your Cloud SQL instances through the Cloud SQL
Admin API.

## Transport

**http** — the agent connects to `https://sqladmin.googleapis.com/mcp` over the
streamable-HTTP MCP transport. Only the global endpoint is supported; regional
endpoints cannot be used to reach the remote MCP server.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token (e.g. `gcloud auth print-access-token`, or from Application Default Credentials / a service account). The server uses IAM and does not accept API keys. |
| `GOOGLE_CLOUD_PROJECT` | yes | Your Google Cloud project ID, sent as the `x-goog-user-project` header to set the quota/billing project. |

The token is referenced from the request header as
`Authorization=Bearer ${GOOGLE_CLOUD_ACCESS_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to
`sqladmin.googleapis.com`; the agent never holds the secret.

## Source

- Docs: https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp
- Supported products: https://docs.cloud.google.com/mcp/supported-products
- Listing: https://github.com/google/mcp
