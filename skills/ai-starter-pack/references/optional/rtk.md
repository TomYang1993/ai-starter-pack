# rtk Adapter

`rtk` ("Rust Token Killer") is optional infrastructure, not an AI Starter Pack
skill. The upstream repo owns installation, releases, troubleshooting, and host
integration details:

https://github.com/rtk-ai/rtk

Use this file only as the starter-pack adapter: when to offer rtk, what not to
overwrite, and how to safely follow upstream docs.

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

## Upstream README First

- If `rtk --version` works and the current host hook is already configured, do
  not fetch upstream docs during a normal setup run. Report it as already
  present.
- If rtk is missing, the host hook is missing, the user asked to update/repair
  rtk, or the host is unfamiliar, fetch the upstream README from
  `https://github.com/rtk-ai/rtk` and follow the current install instructions.
- Treat the upstream README as canonical. Do not rely on memorized commands or
  old command tables in this pack.
- Fetch only the README/docs needed to identify the install/init command. Do not
  clone the whole repo unless upstream explicitly requires it.
- Use global commands only when the user asked for global scope. For
  project-local setup, prefer the upstream project-local command if one exists.

## Normal Flow

1. Confirm the user wants rtk.
2. Check `rtk --version`.
3. Inspect only the current host/scope for an existing rtk hook/plugin setup.
4. If the binary and current host hook are already present, report "rtk already
   configured for this host" and stop.
5. If install, update, repair, or hook setup is needed, fetch the upstream README
   and follow the current instructions for the user's OS/package manager, host,
   and scope.
6. Narrate the exact command, ask for permission, run it, and report what
   changed.
7. Ask the user to restart the host when upstream says to, then verify with a
   shell command such as
   `git status`.

## Caveats to Relay

- rtk compresses shell/Bash command output. Host-native read/grep/glob tools may
  bypass it.
- rtk compresses output tokens, not the model's reasoning.
- rtk usually does not need routine starter-pack updates. Re-check upstream when
  the user adds a new host/tool, changes scope, reinstalls a host, or a host
  changes its hook/plugin API.
