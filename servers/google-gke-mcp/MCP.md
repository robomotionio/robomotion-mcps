# GKE (open-source MCP)

Google's open-source Google Kubernetes Engine MCP server. Exposes tools to work
with GKE clusters and node pools, apply Kubernetes manifests, query Cloud
Logging, and read GKE release notes and recommendations.

## Transport

**stdio** — `gke-mcp` (stdio is the default transport, no arguments required).
The binary is spawned host-side by the **credstdio** bridge; the agent attaches
over a loopback socket and never sees the credentials.

## Credentials

Authentication uses Google Cloud **Application Default Credentials** (ADC) —
the same mechanism as `gcloud`. The credentials are supplied host-side by the
credstdio bridge and never enter the agent sandbox. There is no token env var
to bind in the wizard; the bound Google Cloud identity determines which projects
and clusters the tools can reach.

## Source

- Upstream: https://github.com/GoogleCloudPlatform/gke-mcp
- Install: `go install github.com/GoogleCloudPlatform/gke-mcp@latest`
- Manual client config (Claude Desktop):

  ```json
  {
    "mcpServers": {
      "gke-mcp": {
        "command": "gke-mcp"
      }
    }
  }
  ```
