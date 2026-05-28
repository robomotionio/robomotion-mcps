# Compute Engine (Google Cloud)

Google Cloud's managed remote Model Context Protocol server for Compute Engine.
Exposes tools to manage virtual machine instances, disks, images, networks, and
related compute resources in your Google Cloud projects.

## Transport

**http** — the agent connects to `https://compute.googleapis.com/mcp` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GCP_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token with the `https://www.googleapis.com/auth/cloud-platform` scope. Generate one with `gcloud auth application-default print-access-token`. The Compute Engine MCP server uses OAuth with IAM and does not accept API keys. |

Referenced from the request header as `Authorization=Bearer ${GCP_ACCESS_TOKEN}`.
credproxy swaps the `RM_VAULT__…` placeholder for the real token at TLS egress to
`compute.googleapis.com`; the agent never holds the secret.

> Note: Google Cloud access tokens are short-lived (about one hour). Refresh the
> bound vault item before it expires, or bind a credential source that mints a
> fresh token per run.

## Source

- Docs: https://docs.cloud.google.com/compute/docs/reference/mcp
- Supported products: https://docs.cloud.google.com/mcp/supported-products
