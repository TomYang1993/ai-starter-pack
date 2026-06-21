# Ponytail Adapter

`ponytail` is optional upstream agent behavior, not an AI Starter Pack skill.
The upstream repo owns installation, releases, troubleshooting, host adapters,
hooks, commands, rules, benchmark claims, and licensing:

https://github.com/DietrichGebert/ponytail

Use this file only as the starter-pack adapter: when to offer Ponytail, what not
to overwrite, and which reviewed host install paths are known.

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
- Claude Code and Codex Ponytail plugins run small Node.js lifecycle hooks, so
  `node` must be on the host's non-interactive PATH. If Node is missing, do not
  invent a workaround; explain that the skills may still work but always-on
  activation can stay quiet.
- Treat setup as per-tool/per-scope. A Ponytail install in Claude Code does not
  configure Codex, Cursor, Kilo Code, or any other host.
- Do not trust hooks, install plugin marketplaces, change
  `PONYTAIL_DEFAULT_MODE`, or write `~/.config/ponytail/config.json` without the
  user's approval.

## Reviewed Install Paths

These commands are copied from Ponytail's upstream README and should be
refreshed by the maintainer update job, not re-read during every user install.

| Host | Recommended upstream path |
|---|---|
| Claude Code | `/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail` |
| Claude Code desktop | Use the UI: Customize -> personal plugins -> Create plugin and add marketplace -> Add from repository -> enter the repo URL |
| Codex CLI / desktop | `codex plugin marketplace add DietrichGebert/ponytail`, open `/plugins`, install Ponytail, open `/hooks`, review/trust its lifecycle hooks, then start a new thread |
| GitHub Copilot CLI | `copilot plugin marketplace add DietrichGebert/ponytail` then `copilot plugin install ponytail@ponytail` |
| Gemini CLI | `gemini extensions install https://github.com/DietrichGebert/ponytail` |
| Antigravity CLI | `agy plugin install https://github.com/DietrichGebert/ponytail` |
| Pi agent harness | `pi install git:github.com/DietrichGebert/ponytail` |
| OpenCode | Run from a Ponytail checkout and add `{ "plugin": ["./.opencode/plugins/ponytail.mjs"] }` to `opencode.json`; use an absolute plugin path for a shared checkout |
| OpenClaw | `clawhub install ponytail`; install command skills the same way if wanted |
| Cursor | Copy Ponytail's upstream `.cursor/rules/` file(s) into the target rule location |
| Windsurf | Copy Ponytail's upstream `.windsurf/rules/` file(s) into the target rule location |
| GitHub Copilot editor | Copy Ponytail's upstream `.github/copilot-instructions.md` into the target instruction location |
| Kiro | Copy Ponytail's upstream `.kiro/steering/ponytail.md` into global or project steering |
| Zed / CodeWhale / other AGENTS.md readers | Use Ponytail's upstream `AGENTS.md` or the host mapping in Ponytail's agent-portability docs |

For command-capable hosts, report the commands the user should see after
install: `/ponytail`, `/ponytail-review`, `/ponytail-audit`, `/ponytail-debt`,
`/ponytail-gain`, and `/ponytail-help`. In Codex these are skills, invoked with
`@` such as `@ponytail-review`.

## Normal Flow

1. Confirm the user wants Ponytail and which host/scope to configure.
2. Check for an existing Ponytail install in the current host only:
   - Plugin/marketplace install.
   - Lifecycle hooks or trusted hook entries.
   - Slash commands or skill commands.
   - Instruction-only rule/context file copied from Ponytail upstream.
3. If present, report "Ponytail already configured for this host" and ask before
   reinstalling, changing mode, or switching from rule-only to plugin install.
4. If absent, follow the reviewed install path for the current host.
5. For Codex, remind the user to install from `/plugins`, review/trust hooks in
   `/hooks`, then restart the desktop app or start a new thread.
6. For Claude Code, use slash plugin commands when available; for the desktop UI,
   direct the user through the Ponytail README's UI marketplace flow.
7. For instruction-only hosts, copy only the upstream matching rule file(s).
   Preserve Ponytail's wording and license. Do not synthesize a local ASP
   rewrite.
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
