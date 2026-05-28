# Cloud Run (Google Cloud)

Google Cloud's managed remote Model Context Protocol server for Cloud Run.
Exposes tools to deploy, inspect, and manage Cloud Run services, revisions, and
jobs through the Cloud Run Admin API.

## Transport

**http** — the agent connects to `https://run.googleapis.com/mcp` over the
streamable-HTTP MCP transport. This is a Google-managed endpoint that implements
the MCP authorization specification, backed by OAuth 2.0 and Cloud IAM.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_ACCESS_TOKEN` | yes | A short-lived Google Cloud access token, e.g. from `gcloud auth application-default print-access-token`. The identity must hold the Cloud Run IAM roles for the tools you intend to use. |
| `GOOGLE_CLOUD_PROJECT` | yes | Your Google Cloud project ID, sent as the `x-goog-user-project` (quota/billing) header. |

Referenced from the request headers as
`Authorization=Bearer ${GOOGLE_CLOUD_ACCESS_TOKEN}` and
`x-goog-user-project=${GOOGLE_CLOUD_PROJECT}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to
`run.googleapis.com`; the agent never holds the secret.

## Source

- Endpoint reference: https://docs.cloud.google.com/run/docs/reference/mcp
- Using the Cloud Run MCP server: https://docs.cloud.google.com/run/docs/use-cloud-run-mcp
- Authentication: https://docs.cloud.google.com/mcp/authenticate-mcp
- Supported products: https://docs.cloud.google.com/mcp/supported-products
