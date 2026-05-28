# Microsoft SQL

Microsoft's MSSQL Model Context Protocol server. Exposes tools to list tables,
inspect schemas, run queries, and insert/update/delete data across SQL Server,
Azure SQL Database, and Microsoft Fabric.

## Transport

**stdio** — the server is spawned host-side by the **credstdio** bridge and
connects to your SQL instance using the connection details below. The agent
attaches over a loopback socket and never sees the credentials.

> Note: `aka.ms/MssqlMcp` resolves to the
> [Azure-Samples/SQL-AI-samples](https://github.com/Azure-Samples/SQL-AI-samples/tree/main/MssqlMcp)
> repository, which ships the server as buildable source (Node and .NET) rather
> than a published `npx`/`dnx` package. Upstream runs the Node build with
> `node <repo>/dist/index.js` after `npm install && npm run build`. The
> `command`/`args` in `mcp.yaml` are a marked placeholder pending a published
> build artifact; the environment contract below is verified against upstream.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `SERVER_NAME` | yes | The SQL server, e.g. `my-server.database.windows.net` or `localhost`. |
| `DATABASE_NAME` | yes | The target database name. |
| `READONLY` | no | `"true"` for read-only tools, `"false"` for full read/write (default). |
| `TRUST_SERVER_CERTIFICATE` | no | `"true"` to accept self-signed certificates. |

All are resolved from bound vault items and injected host-side by credstdio.
The Node server authenticates to Azure SQL via Azure AD; for on-premises SQL
Server the connection details flow through the same variables.

## Source

- Upstream: https://github.com/Azure-Samples/SQL-AI-samples/tree/main/MssqlMcp/Node
- Short link: https://aka.ms/MssqlMcp
