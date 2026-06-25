# Ponytail Adapter

`ponytail` is optional upstream agent behavior, not an AI Starter Pack skill.
The upstream repo owns installation, releases, troubleshooting, host adapters,
hooks, commands, rules, benchmark claims, and licensing:

https://github.com/DietrichGebert/ponytail

Use this file only as the starter-pack adapter: when to offer Ponytail, what not
to overwrite, and how to safely follow upstream docs.

## Policy

- Offer Ponytail only when the user explicitly asks for it, or when they choose
  optional tools from the setup menu.
- Do not bundle, rewrite, summarize, or rebrand Ponytail rules. Install from
  upstream using the host's recommended Ponytail plugin, extension, or matching
  upstream rule file.
- Prefer upstream plugin/extension installs for command-capable hosts. Use
  instruction-only rule copies only when Ponytail's upstream README recommends
  that path for the current host.
- Narrate every command before running it. Ponytail can add plugins, lifecycle
  hooks, commands, always-on rules, and optional config.
- The agent owns execution after approval. If upstream shows slash-command or
  TUI steps such as `/plugin ...`, first look for a callable host CLI equivalent
  and run the approved commands yourself. If no safe CLI/tool equivalent exists,
  ask the user to perform the exact manual step, then resume verification.
- Claude Code and Codex Ponytail plugins run small Node.js lifecycle hooks, so
  `node` must be on the host's non-interactive PATH. If Node is missing, do not
  invent a workaround; explain that the skills may still work but always-on
  activation can stay quiet.
- Treat setup as per-tool/per-scope. A Ponytail install in Claude Code does not
  configure Codex, Cursor, Kilo Code, or any other host.
- Do not trust hooks, install plugin marketplaces, change
  `PONYTAIL_DEFAULT_MODE`, or write `~/.config/ponytail/config.json` without the
  user's approval.

## Upstream README First

- If Ponytail is already configured for the current host and the user is not
  updating/repairing it, do not fetch upstream docs during a normal setup run.
  Report it as already present.
- If Ponytail is missing, the user asked to update/repair it, the host is
  unfamiliar, or the existing install is rule-only and the user wants plugin
  commands, fetch the upstream README from
  `https://github.com/DietrichGebert/ponytail` and follow the current host
  instructions.
- Treat the upstream README as canonical. Do not rely on memorized commands or
  old command tables in this pack.
- Fetch only the README/docs needed to identify the current host install path
  and, for rule-only hosts, the exact upstream rule files. Do not clone the whole
  repo unless upstream explicitly requires it.
- For command-capable hosts, after following the README, report the Ponytail
  commands or mode controls the user should expect. Do not invent command names;
  read them from upstream.
- If upstream requires steps to be split across prompts, preserve that order in
  separate agent-run commands after approval. For Claude Code plugin slash
  commands, check the `claude plugin ...` CLI equivalent before asking the user
  to type `/plugin` manually. If the equivalent is missing or unsafe, guide the
  user through the split prompts exactly as upstream requires.

## Normal Flow

1. Confirm the user wants Ponytail and which host/scope to configure.
2. Check for an existing Ponytail install in the current host only:
   - Plugin/marketplace install.
   - Lifecycle hooks or trusted hook entries.
   - Slash commands or skill commands.
   - Instruction-only rule/context file copied from Ponytail upstream.
3. If present, report "Ponytail already configured for this host" and ask before
   reinstalling, changing mode, or switching from rule-only to plugin install.
4. If install, update, repair, mode changes, or plugin/rule conversion is needed,
   fetch the upstream README and follow the current instructions for the current
   host.
5. For command-capable hosts, follow the README's plugin/extension flow and any
   hook-trust or restart steps it requires. Translate slash/TUI plugin actions
   to host CLI commands when safe and available, then run the approved steps
   yourself. If translation is not available, use a guided manual fallback and
   continue verification after the user completes it.
6. For instruction-only hosts, copy only the upstream matching rule file(s).
   Preserve Ponytail's wording and license. Do not synthesize a local ASP
   rewrite.
7. Narrate exact commands or file writes, ask for permission, run only the
   approved steps yourself when tools allow it, and report what changed.
8. Verify by checking the host exposes Ponytail commands or that the target rule
   file exists. If verification needs a fresh session, tell the user.

## Caveats to Relay

- Ponytail is opinionated. Keep it opt-in and make it easy to turn off or set to
  `lite`, `full`, `ultra`, or `off`.
- Plugin installs and rule-only installs are not equivalent. Rule-only installs
  load always-on guidance but may not add Ponytail commands or lifecycle hooks.
- Ponytail mode can be set with `PONYTAIL_DEFAULT_MODE` or
  `~/.config/ponytail/config.json`, but no config is required.
- Do not install Ponytail into other tools just because their directories exist.
  Configure only the current host, unless the user names another host.
