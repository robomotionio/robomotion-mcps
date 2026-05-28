# Firebase (Gemini CLI extension)

Firebase's official Model Context Protocol server, shipped inside the Firebase
CLI (`firebase-tools`). Exposes tools for Firestore, Authentication, Cloud
Storage, Realtime Database, Cloud Messaging, App Hosting, and project/app
management. On startup it detects the `firebase.json` in the working directory
and activates the relevant tool categories.

## Transport

**stdio** — `npx -y firebase-tools@latest mcp`. It is spawned host-side by the
**credstdio** bridge; the agent attaches over a loopback socket and never sees
the credentials.

## Credentials

| Variable | Required | Notes |
| --- | --- | --- |
| `GOOGLE_APPLICATION_CREDENTIALS` | yes | Path to a Google service-account JSON key file. The Firebase MCP server authorizes tool calls with the same Application Default Credentials the Firebase CLI uses; in a non-interactive sandbox this is supplied via ADC. |
| `FIREBASE_PROJECT` | no | Default Firebase project ID to operate against (otherwise read from `firebase.json` / ADC). |

Credentials are resolved from bound vault items and injected host-side by
credstdio.

## Source

- Upstream: https://github.com/firebase/firebase-tools/tree/master/src/mcp
- Docs: https://firebase.google.com/docs/ai-assistance/mcp-server
- Gemini CLI extension: https://github.com/firebase/agent-skills (formerly
  https://github.com/gemini-cli-extensions/firebase)
