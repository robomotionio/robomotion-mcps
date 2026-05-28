# AlloyDB for PostgreSQL (Google Cloud)

Google Cloud's managed remote Model Context Protocol server for AlloyDB for
PostgreSQL. Exposes tools to explore clusters and instances, execute SQL, and
work with AlloyDB AI features.

## Transport

**http** — the agent connects to `https://alloydb.googleapis.com/mcp` over the
streamable-HTTP MCP transport. A regional endpoint
(`https://alloydb.REGION.rep.googleapis.com/mcp`) is also available in Preview.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_ACCESS_TOKEN` | yes | A Google Cloud OAuth 2.0 access token with the `https://www.googleapis.com/auth/alloydb` scope, e.g. from `gcloud auth print-access-token` or Application Default Credentials. IAM authorizes the underlying AlloyDB operations. |

Referenced from the request header as
`Authorization=Bearer ${GOOGLE_CLOUD_ACCESS_TOKEN}`. credproxy swaps the
`RM_VAULT__…` placeholder for the real token at TLS egress to
`alloydb.googleapis.com`; the agent never holds the secret.

## Source

- Docs: https://docs.cloud.google.com/alloydb/docs/ai/use-alloydb-mcp
- Supported products: https://docs.cloud.google.com/mcp/supported-products
- Catalog: https://github.com/google/mcp
