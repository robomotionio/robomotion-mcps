# Spanner (Google Cloud)

Google Cloud's managed remote Model Context Protocol server for Cloud Spanner.
Exposes tools to list instances and databases, run SQL/GQL queries, and inspect
schema and metadata.

## Transport

**http** — the agent connects to `https://spanner.googleapis.com/mcp` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_ACCESS_TOKEN` | yes | An OAuth 2.0 access token for a Google Cloud identity with the Spanner scopes you need (`https://www.googleapis.com/auth/spanner.admin` and/or `https://www.googleapis.com/auth/spanner.data`). Typically minted from Application Default Credentials (e.g. `gcloud auth application-default print-access-token`). The endpoint does not accept API keys. |
| `GOOGLE_CLOUD_PROJECT` | yes | The Google Cloud project ID, sent as the `x-goog-user-project` quota/billing header. |

The access token is referenced from the request header as
`Authorization=Bearer ${GOOGLE_CLOUD_ACCESS_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to
`spanner.googleapis.com`; the agent never holds the secret.

## Source

- Docs: https://docs.cloud.google.com/spanner/docs/use-spanner-mcp
- Supported products: https://docs.cloud.google.com/mcp/supported-products
- Authentication: https://docs.cloud.google.com/mcp/authenticate-mcp
