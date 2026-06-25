---
name: ai-starter-pack
description: Set up a coding agent's everyday environment in one step — upstream-original terse-output style, prose cleanup, engineering skills, and optional tools such as rtk, CodeGraph, and Ponytail — written as portable files that work across Claude Code, Codex, OpenCode, Kilo Code, Antigravity, and any agent that follows the SKILL.md / AGENTS.md standard. Use this whenever the user says "set up my coding environment", "update my coding environment", "bootstrap my agent", "install my starter pack", "configure a new project for me", or starts working in a fresh repo or a freshly installed coding tool and wants their usual defaults in place. Also use when the user asks to add, list, update, or remove any of these components.
---

# AI Starter Pack

A self-installing pack. The agent reading this file **is** the installer — it uses
its own file tools and callable CLIs to perform the setup where the current host
expects it. User permission means: ask, then run the approved command or file
write yourself. Hand commands to the user only when no callable path exists or
the host requires an external approval/UI step the agent cannot operate.
Third-party skills/rules are installed from their upstream originals with their
license notices intact. Before installing or updating a component, fetch the
upstream README/docs for that component and follow the current upstream
instructions. Treat local repo checkouts as caches, not as the source of truth.
Optional tools such as rtk, CodeGraph, and Ponytail follow their upstream
installers and are never bundled.

The pack ships two kinds of content:

- **Collected upstream skills/rules** — original upstream skills such as
  `caveman`, `stop-slop`, and Matt Pocock's skill set, installed from upstream
  docs and copied as-is only when the upstream docs require file copying.

Some components are **not** pure skills. `rtk` is a compiled binary that
compresses shell output below the model, `codegraph` is a local CLI/MCP tool
that indexes projects for code-intelligence queries, and `ponytail` is an
upstream agent plugin/ruleset that reduces over-building. They are opt-in and
installed by following upstream docs, never bundled. See
`references/optional/rtk.md`, `references/optional/codegraph.md`, and
`references/optional/ponytail.md`.

## Run the install
> **Paths in this document are relative to this skill's location** — the folder
> or URL directory that contains this `SKILL.md` (e.g.
> `references/vendor/sources.json`, `LICENSES/...`). If this file was loaded
> from a raw GitHub URL, resolve relative references against the same repo and
> ref. Fetch only the referenced files you need.


Follow these steps in order. Do not skip the dedup checks — re-running this pack,
or running it on a machine that already has some of these files, must never create
duplicates or silently overwrite the user's edits. Resolve concrete install
targets only after the selected component's upstream docs or adapter have made
the target clear.

### 1. Detect the host and setup intent

Default to the host/tool that is currently running this skill. Do **not** install
into other tools' directories just because they exist on disk. Only target
another host when the user explicitly names it (for example "set up Cursor too")
or sets `ASP_AGENT`.

Read `references/dedup.md` → "Host detection" and resolve:

- `HOST` — the active coding agent to configure.
- `SETUP_INTENT` — either `general` for user/global pure-skill defaults in this
  agent/tool, or `project` for this specific repo/workspace.

If detection is ambiguous, ask the user which agent they want rather than
guessing. Honor `ASP_AGENT` when set.

Ask for setup intent unless the user's request explicitly says project-local,
global, or everywhere. Make general/global the default for pure skills, and
explicitly offer project-local as the alternative:

```text
Pure text skills are installed globally by default so this agent can use them in
every project. Do you want that, or should this setup be project-local for the
current repo?
```

Treat "this repo/project/workspace" as `project`. Treat "all projects",
"global", and "everywhere" as `general`. For softer phrases such as "my coding
environment" or "usual defaults", or for a session opened from a parent folder
such as `~/projects` with no specific project target, present the global default
and ask whether the user wants project-local instead. This setup-intent question
applies to pure skills only; optional tools use their own adapter-specific
prompts.

### 2. Offer the menu

Present every component as available, then ask the user to choose the components
once up front. Do not silently install anything just because it is in the pack.
Keep the pitch short: what it is, why it might help, its popularity/quality
signal, and what kind of permission or file change it needs.

If the host supports an interactive terminal picker, use a multi-select
checkbox UI where the user can move with arrow keys, toggle with Space, and
confirm with Enter. If the host only supports chat, show the same checkbox list
and ask the user to reply with names or numbers. Do not present component
selection as a Markdown table.

Suggested checklist copy:

```text
Choose what to install. Space toggles, Enter confirms.

[ ] caveman
    Very popular terse-output skill from Julius Brussee.
    Helps with shorter replies and less token waste.
    Impact: pure skill; defaults to global/user-level, project-local if chosen.

[ ] stop-slop
    Popular prose cleanup skill from Hardik Pandya.
    Helps remove obvious AI writing tells from docs, posts, and messages.
    Impact: pure text skill; defaults to global/user-level, project-local if chosen.

[ ] matt-pocock
    Very popular production engineering skill set from Matt Pocock.
    Helps with TDD, debugging, planning, architecture review, and git workflow.
    Impact: follows upstream skills CLI; defaults to global/user-level here.
    Special case: setup-matt-pocock-skills still configures each project.

[ ] rtk
    Popular shell-output compression tool from rtk-ai.
    Helps when terminal output burns too much context.
    Impact: may install a binary and per-host hooks.

[ ] codegraph
    Popular local code knowledge graph from Colby McHenry.
    Helps agents explore codebases with fewer search/read loops.
    Impact: may install CLI/MCP config and create a per-project .codegraph/.

[ ] ponytail
    Popular anti-overbuilding plugin/ruleset from Dietrich Gebert.
    Helps agents choose the smallest sufficient implementation.
    Impact: may install plugin hooks or rules depending on host.
```

If the user asks for "everything", preselect all components and ask for one
confirmation. Otherwise, show the checklist and let the user choose. Once the
selection is confirmed, say which components were selected and start installing
them in menu order:

1. `caveman`
2. `stop-slop`
3. `matt-pocock`
4. `rtk`
5. `codegraph`
6. `ponytail`

Do not ask again whether to install a selected component. Pause only when user
action is actually needed: permission to run a command, network/file-system
access, a host-specific approval screen, a duplicate/conflict decision, a
`matt-pocock` sub-skill choice, or an optional-tool setup choice from its
adapter file. Use the setup-intent answer from step 1 for pure-skill scope; do
not re-ask per pure skill unless upstream instructions conflict or the user
changes their mind.
Infrastructure items (`rtk`, `codegraph`, `ponytail`) still need explicit
permission at the moment they modify PATH, plugins, MCP/hooks, project indexes,
lifecycle hooks, or rule files.

When upstream instructions are written as slash commands, TUI actions, or
multiple prompts, do not assume the user must perform them. First look for the
host's callable CLI or shell equivalent, ask permission with the exact steps,
and run the approved steps in the required order. If no safe callable equivalent
exists, try an available UI automation/control tool when appropriate. Fall back
to guided manual steps only when the agent cannot run or operate the step; give
the user the exact command/action, wait for completion, then resume verification.

### 3. Resolve upstream install plan and dedup BEFORE writing anything

If the tool can see multiple AI Starter Pack entrypoints (for example plugin plus
manual skill folder), use `references/dedup.md` → "Pack entrypoint duplicates"
before continuing. Use the single entrypoint when only one exists; when multiple
exist, choose the one tagged or described as recommended, otherwise choose the
first discovered entrypoint. Avoid installing another copy of the pack itself.

For every selected component:

1. Fetch and read that component's current upstream README/docs, or the
   component adapter named below.
2. Determine the concrete install method and target for the active `HOST` from
   those docs.
3. For pure skills, apply the setup intent after reading upstream: `general`
   means user/global install, and `project` means project-local install. Be
   explicit when that means passing `-g/--global` or choosing Global for an
   upstream installer whose no-flag default is project-local.
4. Run the matching check in `references/dedup.md` → "Dedup checks" against the
   concrete target(s) the component will touch.

In summary:

- **Already installed by this pack** (our marker present, same version) → skip,
  report "already current".
- **Installed by this pack, older version** → show a diff, ask before replacing.
- **Installed independently by the user** (e.g. they already ran the upstream
  caveman installer) →
  do **not** write a second copy. Report what you found and ask whether to leave
  it, replace it, or merge.
- **Absent** → install.

Re-running is safe because the installer checks both ASP-owned installs and
user-owned installs before writing:

- ASP-owned installs carry
  `# source: ai-starter-pack <component> <upstream-repo>@<commit>` or the richer
  ASP metadata block near the top of the body.
- User-owned installs usually do **not** have ASP metadata, so detect them by
  host location, folder name, `SKILL.md` frontmatter `name:`, upstream repo
  hints, and component-specific heuristics from `references/dedup.md`.
- Rule formats that need pack-specific names use `asp-<component>`.
- Skill-folder hosts normally keep the upstream skill name/folder, especially
  Kilo Code, where the folder name should match the `name:` in `SKILL.md`.
- If a likely user-owned equivalent exists, do not install another copy by
  default. Report what was found and ask whether to leave it, replace it, or
  keep both.

### 4. Write the selected components

- **caveman / stop-slop / matt-pocock** → only if explicitly chosen
  or included in the user's confirmed "usual" set. These have **no bundled
  rewritten payload**. Follow `references/vendor/VENDORING.md`: use
  `sources.json` for repo identity and hints, fetch the upstream README first,
  follow the upstream install instructions for the active `HOST`, and fetch only
  the exact payload files/folders plus LICENSE/NOTICE files needed for the
  selected component. If upstream provides an installer command for the active
  host, prefer that installer over hand-copying files. Pure skills default to
  user/global placement because their content is reusable across projects; use
  project-local placement only when the user chose project setup or upstream
  offers no safe global target. Apply component-specific scope rules:
  - Special cases when defaulting pure skills global: `setup-matt-pocock-skills`
    can be globally available as a trigger but still configures only the repo it
    runs inside; optional tools (`rtk`, CodeGraph, Ponytail) are not pure skills
    and do not inherit this default; if the active host has no safe global skill
    target, explain that and ask before falling back to project-local.
  - `caveman`: default to the active host's user/global skill location when
    `SETUP_INTENT=general`, and tell the user before running commands if
    upstream may configure the active agent broadly. If `SETUP_INTENT=project`,
    use upstream project-local options when available; otherwise explain the
    broader impact and ask before continuing.
  - `stop-slop`: default to the active host's user/global skill location when
    `SETUP_INTENT=general`; use project-local placement when
    `SETUP_INTENT=project`.
  - `matt-pocock`: the current upstream quickstart is the `skills` CLI. For
    `SETUP_INTENT=general`, say that ASP is intentionally using the CLI's global
    path for reusable skills, then pass `-g/--global` or choose Global if the CLI
    asks. For `SETUP_INTENT=project`, run the upstream command without
    `-g/--global`, let the CLI resolve host paths, choose Project if it asks for
    scope, and include `setup-matt-pocock-skills` when upstream recommends it.
    Special case: `setup-matt-pocock-skills` may be available globally as a
    trigger, but its work is still per-project; running it in one repo does not
    configure every repo.
  Stop and ask if no fetch/install tool is available or the upstream README is
  unclear.
- **rtk** → only if explicitly chosen. Follow `references/optional/rtk.md` exactly:
  treat upstream RTK docs as canonical, reuse an existing `rtk` binary when
  present, fetch the upstream README only when install/update/repair is needed,
  verify, and report. Ask before changing PATH, hooks, plugins, or shell config.
- **codegraph** → only if explicitly chosen. Follow
  `references/optional/codegraph.md` exactly: treat upstream CodeGraph docs as
  canonical, reuse an existing `codegraph` binary when present, fetch the
  upstream README only when install/update/repair is needed, verify, and report.
  Ask before changing PATH, MCP config, agent permissions, or creating a project
  `.codegraph/` index.
- **ponytail** → only if explicitly chosen. Follow
  `references/optional/ponytail.md` exactly: treat upstream Ponytail docs as
  canonical, fetch the upstream README only when install/update/repair is
  needed, prefer its current recommended plugin/extension install for
  command-capable hosts, translate slash/TUI plugin steps to callable host CLI
  commands when safe and available, otherwise fall back to guided manual steps,
  use instruction-only rule copies only for hosts where upstream recommends that
  path, and report the resulting Ponytail commands or mode controls. Ask before
  installing plugins, trusting hooks, changing
  shell/env config, or writing rule/context files.

### 5. Report

Summarize per component: installed / skipped (already current) / skipped (user
already had it) / updated. Tell the user the trigger phrases for the on-demand
skills. Do not re-read or narrate these instructions back to the user.

## Provenance and licensing

Do not summarize, rewrite, or clone well-known community skills into ASP-branded
payloads. For collected third-party components, use the upstream README/docs as
the source of truth, fetch only the selected upstream payload files when needed,
and preserve license/notice files. This pack's own MIT content is limited to
installer glue and documentation.

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
