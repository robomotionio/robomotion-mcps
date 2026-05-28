# Cloud Storage (Google Cloud)

Google Cloud's managed remote Model Context Protocol server for Cloud Storage.
Exposes tools to work with buckets and objects — list, read, write, and manage
storage resources through the Cloud Storage API.

## Transport

**http** — the agent connects to `https://storage.googleapis.com/storage/mcp`
over the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_ACCESS_TOKEN` | yes | A Google Cloud OAuth2 access token with the `https://www.googleapis.com/auth/cloud-platform` (or `devstorage`) scope. Obtain it via Application Default Credentials (`gcloud auth application-default login`) or `gcloud auth print-access-token`, or from a service account. |

Referenced from the request header as
`Authorization=Bearer ${GOOGLE_CLOUD_ACCESS_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to Google Cloud; the
agent never holds the secret.

Note: Google Cloud access tokens are short-lived (~1 hour). Refresh the bound
vault item before the token expires.

## Source

- Reference docs: https://docs.cloud.google.com/storage/docs/reference/mcp
- Supported products: https://docs.cloud.google.com/mcp/supported-products
- Authentication: https://docs.cloud.google.com/mcp/authenticate-mcp
