# Google Developer Knowledge API (Remote MCP)

Google's managed remote Model Context Protocol server for the Developer
Knowledge API. Exposes tools that ground responses in official Google developer
and Google Cloud documentation, code samples, and product references.

## Transport

**http** — the agent connects to `https://developerknowledge.googleapis.com/mcp`
over the streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_API_KEY` | yes | A Google Cloud API key, created in the Google Cloud Console and restricted to the Developer Knowledge API. |

Referenced from the request header as `X-Goog-Api-Key=${GOOGLE_API_KEY}`.
credproxy swaps the `RM_VAULT__…` placeholder for the real API key at TLS egress
to Google; the agent never holds the secret.

> The Developer Knowledge API also supports OAuth via gcloud Application Default
> Credentials and manual OAuth client IDs. This catalog entry uses the API key
> path because it maps cleanly onto the credproxy header-injection model.

## Source

- Upstream docs: https://developers.google.com/knowledge/mcp
- Supported products / endpoints: https://docs.cloud.google.com/mcp/supported-products
- Listed at: https://github.com/google/mcp
