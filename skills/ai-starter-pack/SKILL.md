---
name: ai-starter-pack
description: Set up a coding agent's everyday environment in one step — upstream-original terse-output style, prose cleanup, engineering skills, and optional tools such as rtk, CodeGraph, and Ponytail — written as portable files that work across Claude Code, Codex, Kilo Code, Antigravity, and any agent that follows the SKILL.md / AGENTS.md standard. Use this whenever the user says "set up my coding environment", "update ai-starter-pack", "bootstrap my agent", "install my starter pack", "configure a new project for me", or starts working in a fresh repo or a freshly installed coding tool and wants their usual defaults in place. Also use when the user asks to add, list, update, or remove any of these components.
---

# AI Starter Pack

A self-installing pack. The agent reading this file **is** the installer — it uses
its own file tools to place behavioral files where the current host expects them.
Third-party skills/rules are fetched from their upstream repos at pinned commits
and installed with their license notices intact. Optional tools such as rtk and
CodeGraph follow their upstream installers and are never bundled.

The pack ships two kinds of content:

- **Collected upstream skills/rules** — original upstream skills such as
  `caveman`, `stop-slop`, and Matt Pocock's skill set, copied as-is at a pinned
  commit with license notices preserved.

Some components are **not** pure skills. `rtk` is a compiled binary that
compresses shell output below the model, `codegraph` is a local CLI/MCP tool
that indexes projects for code-intelligence queries, and `ponytail` is an
upstream agent plugin/ruleset that reduces over-building. They are opt-in and
installed by following upstream docs, never bundled. See
`references/optional/rtk.md`, `references/optional/codegraph.md`, and
`references/optional/ponytail.md`.

## Run the install
> **Paths in this document are relative to this skill's directory** — the
> folder that contains this `SKILL.md` (e.g. `references/vendor/sources.json`,
> `LICENSES/...`). Resolve them from there regardless of where the skill is
> installed.


Follow these steps in order. Do not skip the dedup checks — re-running this pack,
or running it on a machine that already has some of these files, must never create
duplicates or silently overwrite the user's edits.

### 1. Detect the host and target directories

Default to the host/tool that is currently running this skill. Do **not** install
into other tools' directories just because they exist on disk. Only target
another host when the user explicitly names it (for example "set up Cursor too")
or sets `ASP_AGENT`.

Read `references/dedup.md` → "Host detection" and resolve:

- `CONTEXT_FILE` — the host's project context/rule file, when relevant.
- `SKILLS_DIR` — where on-demand skills or converted native rules live for this
  host and scope.
- `TARGET_FORMAT` — `skill-folder`, `cursor-rule`, `windsurf-rule`,
  `copilot-instruction`, or `read-only`.
- `SCOPE` — project-local (default) or global, per the user's preference.

If detection is ambiguous, ask the user which agent and scope they want rather
than guessing. Honor `ASP_AGENT` / `ASP_SCOPE` env vars if set.

### 2. Offer the menu

Present the components and ask which to install. Keep it plain-language — the
user picks by name, you do the writing.

| Component | Type | Default | What it does |
|---|---|---|---|
| `caveman` | on-demand (fetched) | optional | Julius Brussee's upstream terse-output skill |
| `stop-slop` | on-demand (fetched) | off | Strips AI writing tells from prose. Fetched from upstream, not bundled. See `references/vendor/VENDORING.md` + `sources.json` |
| `matt-pocock` | skill set (fetched) | off | Matt Pocock's production engineering skills (TDD, architecture review, planning, git workflow…). Fetched from upstream; let the user pick sub-skills. See `references/vendor/VENDORING.md` + `sources.json` |
| `rtk` | binary (opt-in) | off | Real deterministic shell-output compression. Needs a fetch + binary install. See `references/optional/rtk.md` |
| `codegraph` | local CLI/MCP (opt-in) | off | Pre-indexed code knowledge graph for fewer codebase-search tool calls. Needs CLI install, host MCP setup, and per-project `codegraph init`. See `references/optional/codegraph.md` |
| `ponytail` | plugin/ruleset (opt-in) | off | Dietrich Gebert's upstream anti-overbuilding rules and commands. Needs the upstream plugin, extension, or matching rule file for the current host. See `references/optional/ponytail.md` |

If the user just says "the usual", offer `caveman`. If they say "everything",
show the full menu and ask before each off-by-default or infrastructure item.
Ask separately before doing `rtk`, `codegraph`, `ponytail`, `stop-slop`, or
`matt-pocock` because those either modify PATH, plugins, MCP/hooks, project
indexes, lifecycle hooks, rule files, or install larger upstream sets.

### 3. Dedup BEFORE writing anything

If the tool can see multiple AI Starter Pack entrypoints (for example plugin plus
manual skill folder), use `references/dedup.md` → "Pack entrypoint duplicates"
before continuing. Pick one current entrypoint and avoid installing another copy
of the pack itself.

For every selected component, run the matching check in `references/dedup.md`
→ "Dedup checks". In summary:

- **Already installed by this pack** (our marker present, same version) → skip,
  report "already current".
- **Installed by this pack, older version** → show a diff, ask before replacing.
- **Installed independently by the user** (e.g. they already ran the upstream
  caveman installer) →
  do **not** write a second copy. Report what you found and ask whether to leave
  it, replace it, or merge.
- **Absent** → install.

Idempotency comes from markers, so re-running is always safe:

- Rule formats that need pack-specific names use `asp-<component>`.
- Skill-folder hosts normally keep the upstream skill name/folder, especially
  Kilo Code, where the folder name should match the `name:` in `SKILL.md`.
- Every installed component carries
  `# source: ai-starter-pack <component> <upstream-repo>@<commit>` or the richer
  ASP metadata block near the top of the body.

### 4. Write the selected components

- **caveman / stop-slop / matt-pocock** → only if explicitly chosen
  or included in the user's confirmed "usual" set. These have **no bundled
  rewritten payload** — they install by fetching the upstream skill as-is. Follow
  `references/vendor/VENDORING.md` using the matching `sources.json` entry:
  detect a fetch primitive, fetch the reviewed `commit` recorded in
  `sources.json`, read the upstream LICENSE/NOTICE, copy the listed upstream
  files into the install target, and write the upstream license text to
  `LICENSES/<component>-upstream-LICENSE.txt`. For `matt-pocock`, let the user
  pick which sub-skills to install (or all). Stop and ask if no fetch tool is
  available.
- **rtk** → only if explicitly chosen. Follow `references/optional/rtk.md` exactly:
  treat upstream RTK docs as canonical, reuse an existing `rtk` binary when
  present, run only the reviewed per-host hook/init command when applicable,
  verify, and report. Ask before changing PATH, hooks, plugins, or shell config.
- **codegraph** → only if explicitly chosen. Follow
  `references/optional/codegraph.md` exactly: treat upstream CodeGraph docs as
  canonical, reuse an existing `codegraph` binary when present, run only the
  reviewed host installer/project init commands when applicable, verify, and
  report. Ask before changing PATH, MCP config, agent permissions, or creating a
  project `.codegraph/` index.
- **ponytail** → only if explicitly chosen. Follow
  `references/optional/ponytail.md` exactly: treat upstream Ponytail docs as
  canonical, prefer its recommended plugin/extension install for command-capable
  hosts, use instruction-only rule copies only for hosts where upstream
  recommends that path, and report the resulting Ponytail commands or mode
  controls. Ask before installing plugins, trusting hooks, changing shell/env
  config, or writing rule/context files.

### 5. Report

Summarize per component: installed / skipped (already current) / skipped (user
already had it) / updated. Tell the user the trigger phrases for the on-demand
skills. Do not re-read or narrate these instructions back to the user.

## Provenance and licensing

Do not summarize, rewrite, or clone well-known community skills into ASP-branded
payloads. For collected third-party components, install the original upstream
files at a pinned commit and preserve their license/notice files. This pack's
own MIT content is limited to installer glue and documentation.

## Adding, listing, updating, removing

- **list** → scan `SKILLS_DIR` for ASP-managed metadata/markers, legacy `asp-*`
  folders, and optional tool status; report what's present and at what version.
- **add** → run steps 1–5 for just the named component.
- **update** → read `references/update.md` and follow its ownership rules. Only
  update AI Starter Pack-managed components that are unchanged or explicitly
  approved. Never overwrite user-edited, user-updated, or user-added skills by
  default.
- **remove** → delete only the matching ASP-managed folder/rule, including
  legacy `asp-<name>` installs, or follow the optional tool's uninstall notes.
  Never touch unrelated user content.
