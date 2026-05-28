# Google Security Operations (Chronicle)

Google's managed remote Model Context Protocol server for Google Security
Operations (Chronicle / SecOps). Exposes tools to run SIEM/UDM searches, query
detections and alerts, manage cases, look up indicators of compromise, and pull
threat intelligence from your SecOps tenant.

## Transport

**http** — the agent connects to
`https://chronicle.<REGION>.rep.googleapis.com/mcp` over the streamable-HTTP MCP
transport. `<REGION>` is the regional endpoint for your SecOps tenant (for
example `us`, `europe`, `northamerica-northeast2`), bound at hire time via the
`CHRONICLE_REGION` identifier.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token scoped to `https://www.googleapis.com/auth/chronicle`, e.g. from `gcloud auth application-default print-access-token` or a service account. |
| `CHRONICLE_REGION` | yes | The regional endpoint of your SecOps tenant (binds the URL host), e.g. `us`, `europe`. |

The token is referenced from the request header as
`Authorization=Bearer ${GOOGLE_CLOUD_ACCESS_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to the Chronicle
endpoint; the agent never holds the secret.

Per-request parameters such as Customer ID (your tenant UUID) and Project ID
(your GCP project) are supplied as tool arguments by the agent.

## Source

- MCP reference: https://docs.cloud.google.com/chronicle/docs/reference/mcp
- Usage guide: https://docs.cloud.google.com/chronicle/docs/secops/use-google-secops-mcp
- Supported products: https://docs.cloud.google.com/mcp/supported-products
