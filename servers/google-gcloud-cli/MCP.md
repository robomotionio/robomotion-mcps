# gcloud CLI MCP

Google's gcloud CLI MCP server. It wraps the locally installed `gcloud`
command-line tool and exposes it as MCP tools, letting an agent run Google Cloud
operations across Compute Engine, Cloud Storage, IAM, Cloud Run, GKE, and the
rest of the gcloud surface. Certain destructive commands are restricted by
default for safety. This is a preview project and not an officially supported
Google product.

## Transport

**stdio** — `npx -y @google-cloud/gcloud-mcp`. It is spawned host-side by the
**credstdio** bridge; the agent attaches over a loopback socket and never sees
the credentials. Requires Node.js 20+ and the `gcloud` CLI installed on the
host.

## Credentials

The server's permissions are tied to the active gcloud account. Authentication
comes from the host gcloud configuration / Application Default Credentials
(`gcloud auth login` or `gcloud auth application-default login`), so no
vault-bound token is required to start.

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_APPLICATION_CREDENTIALS` | no | Path to a service-account key file, when authenticating as a service account instead of the host's logged-in user / ADC. Injected host-side by credstdio. |

## Source

- Upstream: https://github.com/googleapis/gcloud-mcp/tree/main/packages/gcloud-mcp
- npm: `@google-cloud/gcloud-mcp`
- Init for Gemini CLI: `npx @google-cloud/gcloud-mcp init --agent=gemini-cli`
