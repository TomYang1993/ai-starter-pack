# rtk Adapter

`rtk` ("Rust Token Killer") is optional infrastructure, not an AI Starter Pack
skill. The upstream repo owns installation, releases, troubleshooting, and host
integration details:

https://github.com/rtk-ai/rtk

Use this file only as the starter-pack adapter: when to offer rtk, what not to
overwrite, and which reviewed host init commands are known.

## Policy

- Offer rtk only when the user explicitly asks for it.
- Do not bundle or copy rtk. Fetch/install from upstream or send the user to the
  upstream docs.
- Narrate every command before running it. rtk modifies PATH and host hook/plugin
  config, so the user should see what changes.
- If `rtk --version` works, reuse the existing binary. Do not reinstall it just
  because the starter pack is being updated.
- Treat hook setup as per-tool/per-scope. A global rtk binary does not mean
  Claude Code, Codex, Kilo Code, etc. are all configured.

## Reviewed Host Init Commands

These commands are copied from the upstream RTK README's quick-start section and
should be refreshed by the maintainer update job, not re-read during every user
install.

| Host | Init command |
|---|---|
| Claude Code / default hook agents | `rtk init -g` |
| Codex | `rtk init -g --codex` |
| Cursor | `rtk init -g --agent cursor` |
| Windsurf | `rtk init -g --agent windsurf` |
| Cline / Roo Code | `rtk init --agent cline` |
| Kilo Code | `rtk init --agent kilocode` |
| Antigravity | `rtk init --agent antigravity` |

Use the global (`-g`) form only when the user asked for global scope. For project
scope, prefer the non-global form if upstream supports it for that host. If the
host is missing from this table, check `rtk init --help` or the upstream README
before guessing.

## Normal Flow

1. Confirm the user wants rtk.
2. Check `rtk --version`.
3. If missing, follow the upstream README install path for the user's OS/package
   manager.
4. Run the reviewed init command for the current host/scope.
5. Ask the user to restart the host, then verify with a shell command such as
   `git status`.

## Caveats to Relay

- rtk compresses shell/Bash command output. Host-native read/grep/glob tools may
  bypass it.
- rtk compresses output tokens, not the model's reasoning.
- rtk usually does not need routine starter-pack updates. Re-check upstream when
  the user adds a new host/tool, changes scope, reinstalls a host, or a host
  changes its hook/plugin API.
