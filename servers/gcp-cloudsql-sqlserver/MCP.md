# Cloud SQL for SQL Server (Google Cloud)

Google's managed remote Model Context Protocol server for Cloud SQL for SQL
Server. Exposes tools to manage SQL Server instances, databases, users, and
long-running operations through the Cloud SQL Admin API.

## Transport

**http** — the agent connects to `https://sqladmin.googleapis.com/mcp` over the
streamable-HTTP MCP transport. The server runs on Google infrastructure.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token with IAM permissions for Cloud SQL. Typically obtained from Application Default Credentials (`gcloud auth application-default login`) or a service account. |

Referenced from the request header as
`Authorization=Bearer ${GOOGLE_CLOUD_ACCESS_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to
`sqladmin.googleapis.com`; the agent never holds the secret.

Cloud SQL MCP servers use the OAuth 2.0 protocol with Identity and Access
Management (IAM) for authentication and authorization.

## Source

- Docs: https://docs.cloud.google.com/sql/docs/sqlserver/use-cloudsql-mcp
- Endpoint catalog: https://docs.cloud.google.com/mcp/supported-products
- Authentication: https://docs.cloud.google.com/mcp/authenticate-mcp
