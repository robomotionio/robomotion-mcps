# MCP Toolbox for Databases

Google's open-source MCP server (formerly "Gen AI Toolbox for Databases") that
connects AI agents directly to enterprise databases. With the `--prebuilt` flag
it exposes ready-to-use generic tools such as `list_tables` and `execute_sql`
for instant schema exploration and querying — no `tools.yaml` boilerplate
required.

Supported engines include PostgreSQL, MySQL, SQL Server, Oracle, MongoDB,
Redis, Elasticsearch, CockroachDB, ClickHouse, Neo4j, Snowflake, and the Google
Cloud databases AlloyDB, BigQuery, Cloud SQL, Spanner, and Firestore.

## Transport

**stdio** — `npx -y @toolbox-sdk/server --prebuilt=postgres --stdio`. This entry
ships the PostgreSQL prebuilt; change `--prebuilt=<database>` for another engine.
It is spawned host-side by the **credstdio** bridge; the agent attaches over a
loopback socket and never sees the credentials.

## Credentials

The prebuilt PostgreSQL configuration reads its connection details from
environment variables:

| Variable | Required | Notes |
| --- | --- | --- |
| `POSTGRES_HOST` | yes | Hostname or IP of the PostgreSQL server, e.g. `127.0.0.1`. |
| `POSTGRES_DATABASE` | yes | Name of the database to connect to. |
| `POSTGRES_USER` | yes | Database username. |
| `POSTGRES_PASSWORD` | yes | Password for that user. |
| `POSTGRES_PORT` | no | Server port (defaults to `5432`). |

All are resolved from bound vault items and injected host-side by credstdio.

## Source

- Upstream: https://github.com/googleapis/genai-toolbox (renamed to
  https://github.com/googleapis/mcp-toolbox)
- Docs: https://mcp-toolbox.dev/
- npm: `@toolbox-sdk/server`
