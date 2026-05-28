# Cloud Resource Manager (Google Cloud)

Google Cloud's managed Cloud Resource Manager remote Model Context Protocol
server. Exposes tools to manage projects, folders, and organizations, along with
their IAM policies and metadata.

## Transport

**http** — the agent connects to `https://cloudresourcemanager.googleapis.com/mcp`
over the streamable-HTTP MCP transport. The server runs on Google
infrastructure; you must enable MCP servers and set up authentication on your
Google Cloud project before use.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GCP_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token. Obtain one from Application Default Credentials (`gcloud auth application-default print-access-token`) or a service account. API-key credentials are not supported for IAM-scoped services. |

Referenced from the request header as `Authorization=Bearer ${GCP_ACCESS_TOKEN}`.
credproxy swaps the `RM_VAULT__…` placeholder for the real token at TLS egress to
Google Cloud; the agent never holds the secret.

## Source

- Reference docs: https://docs.cloud.google.com/resource-manager/reference/mcp
- Google Cloud MCP servers overview: https://docs.cloud.google.com/mcp/supported-products
- Authentication guide: https://docs.cloud.google.com/mcp/authenticate-mcp
