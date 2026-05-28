# Google Cloud Storage (open-source)

Google's open-source Cloud Storage MCP server. Exposes tools to work with
Google Cloud Storage buckets and objects — list buckets, list/read/upload
objects, and manage storage resources. The MCP's permissions are tied directly
to the permissions of the authenticated user or service account.

## Transport

**stdio** — `npx -y @google-cloud/storage-mcp`. It is spawned host-side by the
**credstdio** bridge; the agent attaches over a loopback socket and never sees
the credentials. Requires Node.js 20+.

## Credentials

Authentication uses Google Cloud Application Default Credentials (ADC). In a
headless/sandbox context this is provided as a service-account key file.

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_APPLICATION_CREDENTIALS` | yes | Path to a service-account JSON key file used for Application Default Credentials. Scopes the MCP's permissions to that service account. |
| `GOOGLE_CLOUD_PROJECT` | no | Default Google Cloud project ID for operations. |

The service-account key is resolved from a bound vault item and injected
host-side by credstdio; it never enters the agent sandbox.

## Source

- Upstream: https://github.com/googleapis/gcloud-mcp/tree/main/packages/storage-mcp
- npm: `@google-cloud/storage-mcp`
