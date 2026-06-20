# CodeGraph Adapter

`codegraph` is optional infrastructure, not an AI Starter Pack skill. The
upstream repo owns installation, releases, troubleshooting, host integration,
and benchmark claims:

https://github.com/colbymchenry/codegraph

Use this file only as the starter-pack adapter: when to offer CodeGraph, what
not to overwrite, and which reviewed setup commands are known.

## Policy

- Offer CodeGraph only when the user explicitly asks for it, or when they choose
  optional tools from the setup menu.
- Do not bundle or copy CodeGraph. Fetch/install from upstream or send the user
  to the upstream docs.
- Narrate every command before running it. CodeGraph can modify PATH, host MCP
  configuration, agent permissions/instructions, and per-project indexes.
- If `codegraph --version` works, reuse the existing binary. Do not reinstall it
  just because the starter pack is being updated.
- Treat host setup and project indexing as separate steps. A global CodeGraph
  binary does not mean Claude Code, Codex, Cursor, Kilo Code, etc. are all
  configured, and host setup does not mean the current repo has been indexed.
- Project indexes live in `.codegraph/`. Do not delete, rebuild, or reinitialize
  an existing index unless the user asks.

## Reviewed Commands

These commands are copied from the upstream CodeGraph README's quick-start
section and should be refreshed by the maintainer update job, not re-read during
every user install.

| Step | Command |
|---|---|
| macOS / Linux bundled install | `curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh` |
| Windows bundled install | `irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex` |
| npm install | `npm i -g @colbymchenry/codegraph` |
| Configure installed agents | `codegraph install` |
| One-shot npx setup | `npx @colbymchenry/codegraph` |
| Initialize current project | `codegraph init` |
| Upgrade | `codegraph upgrade` |
| Check for upgrade | `codegraph upgrade --check` |
| Remove host integrations | `codegraph uninstall` |
| Remove project index | `codegraph uninit` |

Prefer the upstream installer path that matches the user's OS and package
manager. Avoid piping remote scripts without explaining the risk and asking for
approval. If the user already has Node and wants the least surprising path, the
npm install is usually easier to review.

## Normal Flow

1. Confirm the user wants CodeGraph.
2. Check `codegraph --version`.
3. If missing, follow the upstream README install path for the user's OS/package
   manager.
4. Run `codegraph install` only for the host(s) the user approves.
5. In each project the user wants indexed, check for `.codegraph/`.
6. If `.codegraph/` is absent, run `codegraph init` from that project root.
7. Ask the user to restart the host if the upstream installer says to, then
   verify that the CodeGraph tools are visible in a fresh agent session when
   possible.

## Caveats to Relay

- CodeGraph helps when the agent actually uses its MCP tools for codebase
  exploration. It does not replace tests, type checks, or linting.
- CodeGraph indexes local code into `.codegraph/`; users may want that ignored
  by git if upstream does not already handle it.
- Host setup is per-tool. Installing CodeGraph for Codex does not automatically
  configure Claude Code, Cursor, Kilo Code, or Antigravity.
- Project setup is per-repo. A configured host still needs `codegraph init` for
  each repo where the user wants indexed code intelligence.
