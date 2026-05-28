# Genmedia (Imagen / Veo)

Google Cloud's Vertex AI **generative-media** MCP servers. The catalog entry
launches the **Imagen** server (image generation and editing); the same
distribution ships sibling stdio binaries for the other media services:

| Binary | Service |
| --- | --- |
| `mcp-imagen-go` | Imagen 3 / 4 — image generation and editing (this entry) |
| `mcp-veo-go` | Veo 3 / 3.1 — video creation |
| `mcp-gemini-go` | Gemini image generation |
| `mcp-chirp3-go` | Chirp 3 HD / Gemini text-to-speech |
| `mcp-lyria-go` | Lyria music generation |
| `mcp-avtool-go` | Audio/video compositing |

## Transport

**stdio** — `mcp-imagen-go` (default transport). The pre-compiled Go binary is
spawned host-side by the **credstdio** bridge; the agent attaches over a
loopback socket and never sees the credentials. The binary is installed from the
upstream installer:

```
curl -sL https://raw.githubusercontent.com/GoogleCloudPlatform/vertex-ai-creative-studio/main/experiments/mcp-genmedia/mcp-genmedia-go/install-online.sh | bash
```

To use Veo instead of Imagen, swap the `command` in `mcp.yaml` to `mcp-veo-go`.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_CLOUD_PROJECT` | yes | Your Google Cloud project ID. The server terminates at startup if unset. |
| `GOOGLE_APPLICATION_CREDENTIALS` | yes* | Path to a service-account key JSON. *Optional only if Application Default Credentials (`gcloud auth application-default login`) are already configured host-side. |
| `GOOGLE_CLOUD_LOCATION` | no | Vertex AI region. Defaults to `us-central1`. |
| `GENMEDIA_BUCKET` | no | Default Cloud Storage bucket for outputs when a request omits one. |

The project ID and service-account credentials are resolved from bound vault
items and injected host-side by credstdio; they never enter the agent sandbox.

## Source

- Upstream: https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio/tree/main/experiments/mcp-genmedia
- License: Apache-2.0 ("This is not an officially supported Google product.")
