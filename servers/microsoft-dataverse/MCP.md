# Microsoft Dataverse

The Microsoft Dataverse MCP server exposes tools to list and describe tables,
query and manage records, and work with schema (tables, columns, relationships,
and option sets) through the Dataverse Web API. It connects to your own
Dataverse environment (Power Platform / Dynamics 365).

## Transport

**stdio** — `npx -y @microsoft/dataverse mcp ${DATAVERSE_ENVIRONMENT_URL}`. The
`@microsoft/dataverse` npm package runs as a local proxy that handles
authentication and communication with the Dataverse MCP endpoint
(`/api/mcp`) of your environment. It is spawned host-side by the **credstdio**
bridge; the agent attaches over a loopback socket and never sees the
credentials.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `DATAVERSE_ENVIRONMENT_URL` | yes | Your Dataverse environment (org) URL, e.g. `https://contoso.crm.dynamics.com`. Passed as the proxy argument. |

The proxy authenticates interactively via Microsoft Entra ID on first run. A
tenant administrator must grant admin consent for the **Dataverse CLI** app
(`0c412cc3-0dd6-449b-987f-05b053db9457`) once per tenant, and enable that client
in the Power Platform admin center for the environment. The Dataverse MCP server
must also be enabled for the environment.

The environment URL is resolved from a bound vault item and injected host-side
by credstdio.

## Source

- Docs: https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-mcp
- Non-Microsoft clients: https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-mcp-other-clients
- npm: `@microsoft/dataverse`
