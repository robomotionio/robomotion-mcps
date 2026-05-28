# Google Maps Grounding Lite (Remote MCP)

Google's managed Maps Grounding Lite Model Context Protocol server. Exposes
tools to ground model responses in Google Maps data — place search, place
details, geocoding, and directions.

## Transport

**http** — the agent connects to `https://mapstools.googleapis.com/mcp` over the
streamable-HTTP MCP transport.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_MAPS_API_KEY` | yes | A Google Maps Platform API key for a Cloud project with the Maps Grounding Lite API enabled. |

Referenced from the request header as `X-Goog-Api-Key=${GOOGLE_MAPS_API_KEY}`.
credproxy swaps the `RM_VAULT__…` placeholder for the real key at TLS egress to
Google; the agent never holds the secret.

> The endpoint also supports OAuth access tokens (scope
> `https://www.googleapis.com/auth/maps-platform.mapstools`). This catalog entry
> uses the simpler API-key header path.

## Source

- Docs: https://developers.google.com/maps/ai/grounding-lite
- Remote MCP registry: https://github.com/google/mcp
- Supported endpoints: https://docs.cloud.google.com/mcp/supported-products
