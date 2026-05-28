# Cloud Run (open-source deploy MCP)

Google's open-source Cloud Run MCP server. Exposes tools to deploy code to
Cloud Run, list and inspect services, read service logs, and (in local mode)
manage Google Cloud projects.

## Transport

**stdio** — `npx -y @google-cloud/cloud-run-mcp`. The server is spawned
host-side by the **credstdio** bridge using the bundled Node runtime; the agent
attaches over a loopback socket and never sees the credentials.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_PROJECT` | yes | Default Google Cloud project ID for Cloud Run services. |
| `GOOGLE_CLOUD_REGION` | yes | Default region for Cloud Run services, e.g. `us-central1`. |
| `GOOGLE_APPLICATION_CREDENTIALS` | yes | Path to the service-account key JSON used for Application Default Credentials (ADC). The server authenticates to Google Cloud via the Google Cloud SDK / ADC. |
| `DEFAULT_SERVICE_NAME` | no | Default service name; defaults to the working directory name. |

The project, region, and ADC credentials are resolved from bound vault items and
injected host-side by credstdio.

## Source

- Upstream: https://github.com/GoogleCloudPlatform/cloud-run-mcp
- npm: `@google-cloud/cloud-run-mcp`
- Listed in Google's MCP catalog: https://github.com/google/mcp
