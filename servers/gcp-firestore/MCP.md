# Firestore (Google Cloud)

Google Cloud's managed remote Model Context Protocol server for Firestore in
Native mode. Exposes tools to query, read, and write documents and collections,
and to inspect database and index structure.

## Transport

**http** — the agent connects to `https://firestore.googleapis.com/mcp` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token with the `https://www.googleapis.com/auth/cloud-platform` scope, e.g. from `gcloud auth application-default print-access-token`. Access tokens are short-lived (~1 hour) and must be refreshed. |
| `GOOGLE_CLOUD_PROJECT` | yes | The Google Cloud project ID that holds the Firestore database (sent as the `x-goog-user-project` quota/billing project header). |

The Firestore remote MCP server uses OAuth 2.0 with Identity and Access
Management (IAM) for authentication and authorization. The token is referenced
from the request header as `Authorization=Bearer ${GOOGLE_CLOUD_ACCESS_TOKEN}`;
credproxy swaps the `RM_VAULT__…` placeholder for the real token at TLS egress
to Firestore, so the agent never holds the secret. The project ID is a
non-secret identifier injected into the `x-goog-user-project` header.

## Source

- Docs: https://docs.cloud.google.com/firestore/native/docs/use-firestore-mcp
- Endpoint list: https://docs.cloud.google.com/mcp/supported-products
- Authentication: https://docs.cloud.google.com/mcp/authenticate-mcp
