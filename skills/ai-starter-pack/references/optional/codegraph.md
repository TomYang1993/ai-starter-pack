# CodeGraph Adapter

`codegraph` is optional infrastructure, not an AI Starter Pack skill. The
upstream repo owns installation, releases, troubleshooting, host integration,
and benchmark claims:

https://github.com/colbymchenry/codegraph

Use this file only as the starter-pack adapter: when to offer CodeGraph, what
not to overwrite, and how to safely follow upstream docs.

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

## Upstream README First

- If `codegraph --version` works, the current host MCP/setup is present, and the
  current project already has the intended `.codegraph/` index, do not fetch
  upstream docs during a normal setup run. Report it as already present.
- If the binary is missing, host setup is missing, the project index is missing,
  the user asked to update/repair CodeGraph, or the host is unfamiliar, fetch the
  upstream README from `https://github.com/colbymchenry/codegraph` and follow the
  current instructions.
- Treat the upstream README as canonical. Do not rely on memorized commands or
  old command tables in this pack.
- Fetch only the README/docs needed to identify install, host setup, update, or
  project-index commands. Do not clone the whole repo unless upstream explicitly
  requires it.
- Prefer the upstream installer path that matches the user's OS and package
  manager. Avoid piping remote scripts without explaining the risk and asking for
  approval.

## Normal Flow

1. Confirm the user wants CodeGraph.
2. Check `codegraph --version`.
3. Inspect only the current approved host for CodeGraph MCP/setup.
4. In the current project, check for `.codegraph/` when the user wants project
   indexing.
5. If binary, host setup, and project index are already present, report what is
   already configured and stop.
6. If install, update, repair, host setup, or project indexing is needed, fetch
   the upstream README and follow the current instructions for that step.
7. Narrate exact commands, ask for permission, run only the approved steps, and
   report what changed.
8. Ask the user to restart the host if the upstream installer says to, then
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
