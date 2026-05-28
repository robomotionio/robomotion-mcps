# Kubernetes Engine (GKE, Google Cloud)

Google Cloud's fully managed remote Model Context Protocol server for Google
Kubernetes Engine. Exposes tools to inspect and manage GKE clusters, node pools,
and workloads.

## Transport

**http** — the agent connects to `https://container.googleapis.com/mcp` over the
streamable-HTTP MCP transport. Read-only and delete-restricted toolsets are also
available at `https://container.googleapis.com/mcp/read-only` and
`https://container.googleapis.com/mcp/delete-tools`.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GCP_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token with the `https://www.googleapis.com/auth/cloud-platform` scope. Generate one with `gcloud auth application-default print-access-token`. The GKE MCP server uses OAuth with IAM and does not accept API keys. |

Referenced from the request header as `Authorization=Bearer ${GCP_ACCESS_TOKEN}`.
credproxy swaps the `RM_VAULT__…` placeholder for the real token at TLS egress to
`container.googleapis.com`; the agent never holds the secret.

> Note: Google Cloud access tokens are short-lived (about one hour). Refresh the
> bound vault item before it expires, or bind a credential source that mints a
> fresh token per run.

## Source

- Docs: https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp
- Supported products: https://docs.cloud.google.com/mcp/supported-products
- Remote MCP catalog: https://github.com/google/mcp
