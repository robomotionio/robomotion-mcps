# Bigtable (Google Cloud)

Google Cloud's managed remote Model Context Protocol server for Cloud Bigtable.
Exposes tools to manage instances, clusters, and tables, configure IAM, and read
and query data through the Bigtable Admin API.

## Transport

**http** — the agent connects to `https://bigtableadmin.googleapis.com/mcp` over
the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token with the `https://www.googleapis.com/auth/bigtable.admin` scope. Obtain it from Application Default Credentials (`gcloud auth application-default print-access-token`) or a service account. The Bigtable MCP server does not accept API keys. |

Referenced from the request header as
`Authorization=Bearer ${GOOGLE_CLOUD_ACCESS_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to Google Cloud; the
agent never holds the secret.

Note: ADC-generated access tokens expire roughly every hour and must be
refreshed; a service account is recommended for production workloads.

## Source

- Docs: https://docs.cloud.google.com/bigtable/docs/use-bigtable-mcp
- Supported products: https://docs.cloud.google.com/mcp/supported-products
- Authentication: https://docs.cloud.google.com/mcp/authenticate-mcp
