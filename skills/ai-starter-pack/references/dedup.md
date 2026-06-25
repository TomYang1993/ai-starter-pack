# Host detection and dedup

Detail kept out of `SKILL.md` so the orchestrator stays short. Read this when
running host detection and dedup.

## Host detection

Resolve only the active `HOST` during host detection. Do not choose component
scope or target directories until after the user has chosen components and the
selected component's upstream README/docs or adapter have shown the concrete
install method for that host and intent. For pure skills,
`SETUP_INTENT=general` means agent-side/user install by default, and
`SETUP_INTENT=project` means project-level install.

### Scope

After the user chooses components, explain placement only if at least one pure
skill was selected. Use "agent-side defaults" as the user-facing term for the
recommended `general` intent; mention "global" only as a clarification or when a
tool flag uses that word. Use "project-level" for `project`. Treat scope as
component-specific after that because upstream tools may use different flags or
prompts. For example, the `skills` CLI defaults to project-local when no scope
flag is given, so pure-skill agent-side setup must pass `-g/--global` or choose
Global when the CLI asks. Honor `ASP_SCOPE=project|global` only after it is
compatible with the selected component's upstream install path and user intent.
Optional tools such as `rtk`, CodeGraph, and Ponytail are not governed by the
pure-skill agent-side default; their adapters decide when to ask.

### Signals

The active host is the tool currently running this installer. Install into that
host by default. Other host directories in the same repo or home folder are only
inventory and duplicate-check signals; they are not permission to configure
those tools, and they must not override the current runtime.

Resolve the host in this order:

1. Explicit override: `ASP_AGENT=claude|cursor|windsurf|codex|opencode|copilot|antigravity|kilo|generic`.
2. Explicit user target in the prompt, e.g. "set up Kilo Code" or "configure
   Cursor too".
3. The current agent/runtime identity, when the host exposes it or the agent
   knows it is running inside Claude Code, Codex, Kilo Code, Cursor, etc.
4. Existing host-specific files/directories in the **target project** only as
   weak evidence. If these conflict or only point to tools other than the
   current runtime, ask which host to configure.

Do **not** infer the active host from the AI Starter Pack source repo itself, a
GitHub URL checkout, or unrelated host directories in the user's home folder.
For example, if the user is running this flow in Kilo Code and the project also
has `.claude/` or `CLAUDE.md`, the active host is still Kilo Code unless the user
explicitly asks to configure Claude Code.

If the active host cannot be identified confidently, ask the user which tool and
agent they want. Do not guess from filesystem hints alone.

Resolve `SETUP_INTENT` after the component menu, only when pure skills were
selected:

- `general` — the user accepts the recommended agent-side defaults, or says
  "agent-side", "all projects", "global", "everywhere", "usual defaults", or
  similar.
- `project` — the user is configuring the current repo/workspace, or explicitly
  says "project-level", "this project", "this repo", or similar.
- If the current directory is a parent/workspace folder such as `~/projects`, or
  the prompt only says "set up my coding environment" or "usual defaults",
  still show the component menu first. After selection, explain that agent-side
  defaults are recommended for the curated pure skills and ask whether the user
  instead wants project-level setup.

The table below is a reference for dedup and manual fallbacks after upstream docs
have resolved the selected component's actual target. It is not the install plan
for every component.

| Host | Project context/rule file | Global context/rule file | Project skill/rule dir | Global skill/rule dir | Target format |
|---|---|---|---|---|---|
| Claude Code | `CLAUDE.md` | `~/.claude/CLAUDE.md` | `.claude/skills/` | `~/.claude/skills/` | `skill-folder` |
| Codex | `AGENTS.md` | `~/.codex/AGENTS.md` | `.agents/skills/` | `~/.codex/skills/` | `skill-folder` |
| OpenCode | `AGENTS.md` or `opencode.json` | `~/.config/opencode/opencode.json` | `.agents/skills/` when using the upstream `skills` CLI for project scope | `~/.config/opencode/skills/` for pure-skill agent-side/general scope with upstream `-g/--global` | `skill-folder` |
| Cursor | `AGENTS.md` or `.cursor/rules/ai-starter-pack.mdc` | Cursor Settings → Rules | `.cursor/rules/` | Cursor Settings → Rules | `cursor-rule` |
| Windsurf / Devin | `AGENTS.md` or `.devin/rules/ai-starter-pack.md` | `~/.codeium/windsurf/memories/global_rules.md` | `.devin/rules/` | `~/.codeium/windsurf/memories/` | `windsurf-rule` |
| GitHub Copilot | `AGENTS.md` or `.github/copilot-instructions.md` | none | `.github/instructions/` | none | `copilot-instruction` |
| Antigravity | `AGENTS.md` | verify current host docs | `.agents/skills/` if supported | `~/.agents/skills/` if supported | `skill-folder` if supported, otherwise `read-only` |
| Kilo Code | `AGENTS.md` | verify current host docs | `.kilo/skills/` native, or `.agents/skills/` compatibility | `~/.kilo/skills/` | `skill-folder` |
| Generic / other | `AGENTS.md` | `~/.agents/AGENTS.md` if supported | `.agents/skills/` | `~/.agents/skills/` | `skill-folder` |

Detection hints:

- Current runtime says Claude Code, or user explicitly targets Claude Code →
  Claude Code. A `.claude/` directory or `CLAUDE.md` is only supporting evidence.
- Current runtime says Cursor, or user explicitly targets Cursor → Cursor. A
  `.cursor/` directory or `.cursorrules` file is only supporting evidence.
- Current runtime says Windsurf/Devin, or user explicitly targets them →
  Windsurf / Devin. `.devin/`, `.windsurf/`, or `.windsurfrules` are supporting
  evidence.
- Current runtime says Codex, or user explicitly targets Codex → Codex. A
  `.codex/` directory is only supporting evidence.
- Current runtime says OpenCode, or user explicitly targets OpenCode →
  OpenCode. `.opencode/` and `opencode.json` are supporting evidence. OpenCode
  is installed by the upstream `skills` CLI to `.agents/skills/` for project
  scope and `~/.config/opencode/skills/` for pure-skill agent-side/general scope.
  Let the selected component's upstream installer decide paths; add
  `-g/--global` only when `SETUP_INTENT=general` or the user explicitly asked
  for global/everywhere.
- Current runtime says GitHub Copilot, or user explicitly targets Copilot →
  Copilot. `.github/copilot-instructions.md` is supporting evidence.
- Explicit user request for Kilo Code, `ASP_AGENT=kilo`, or a project-local
  `.kilo/` directory → Kilo Code. Use `.kilo/skills/` for Kilo-native skill
  installs; use `.agents/skills/` only when the user asks for a shared
  compatibility path.
- An `AGENTS.md` with no Claude markers → treat as the generic `AGENTS.md`
  family (Codex / Kilo Code / Antigravity / others all read `AGENTS.md`).

If nothing matches, ask the user. The old safest default of
`AGENTS.md` + `.agents/skills/` is only acceptable after telling the user that
the host was not detected and getting confirmation to use a generic Agent Skills
install.

## Component target discovery

Before checking for duplicates for a selected component:

1. Read the component's current upstream README/docs or the optional-tool adapter
   referenced by `SKILL.md`.
2. Determine the exact command, file path, plugin path, hook path, or project
   index the component will touch for the active `HOST`.
3. Combine upstream install mechanics with `SETUP_INTENT`. For pure skills,
   `general` means agent-side/user install by default, even when the upstream
   command's no-flag default is project-local. Explain that scope choice before
   adding a global flag or choosing Global. For `project`, use the upstream
   project-local path or prompt choice.
4. Then run the dedup checks below against those exact targets.

## Pack entrypoint duplicates

Some hosts can load AI Starter Pack through more than one mechanism, such as a
marketplace/plugin install, a Skills CLI install, and a manually copied skill
folder. Treat these as duplicate entrypoints for the **pack itself**, not as
separate environments to configure.

Before installing the pack or when diagnosing duplicate triggers:

1. Look for the same `ai-starter-pack` skill/plugin in every known entrypoint for
   the current host and scope (for example Claude Code marketplace/plugin plus
   `.claude/skills/ai-starter-pack` or `~/.claude/skills/ai-starter-pack`).
2. If exactly one entrypoint exists, use it and continue.
3. If multiple entrypoints exist, choose the one tagged or described as
   recommended. If none is tagged recommended, choose the first discovered
   entrypoint in the scan order from step 1.
4. Do not copy another skill folder just because one entrypoint was already
   present. Report which entrypoint was chosen, and mention any ignored duplicate
   entrypoints without asking unless the chosen entrypoint is unreadable,
   stale/broken, or conflicts with an explicit user request.
5. Component install/update dedup still runs after the pack entrypoint is chosen.

## Dedup checks

The goal: never write a file the user already has, never clobber their edits,
and make re-running a no-op.

### Layer 1 — on-demand skills or converted rules

Here `SKILLS_DIR`, `TARGET_FORMAT`, and scope mean the values resolved during
"Component target discovery", after applying `SETUP_INTENT`, not values chosen
solely from host detection.

For each of `caveman`, `stop-slop`, `matt-pocock`:

1. **Our copy present**:
   - `skill-folder`: `SKILLS_DIR/asp-<name>/SKILL.md` exists. For Kilo-native
     installs, also check `SKILLS_DIR/<upstream-skill-name>/SKILL.md` because
     Kilo expects the directory to match the skill's `name:`.
   - `cursor-rule`: `.cursor/rules/asp-<name>.mdc` exists.
   - `windsurf-rule`: `.devin/rules/asp-<name>.md` or
     `.windsurf/rules/asp-<name>.md` exists.
   - `copilot-instruction`: `.github/instructions/asp-<name>.instructions.md`
     exists, or the component marker is in `AGENTS.md` /
     `.github/copilot-instructions.md`.
   - Read its source-marker line. Same version → skip. Older → diff + confirm.
2. **User's independent copy present** — a sibling folder whose `SKILL.md` `name`
   frontmatter (or folder name) matches the component's purpose. Examples to look
   for before writing `asp-caveman`: a folder named `caveman`, or any `SKILL.md`
   whose `name` is `caveman` / contains "caveman".
   - **`stop-slop`** — many users already have the upstream installed. Look for a
     folder named `stop-slop` or a `SKILL.md` whose `name` is `stop-slop` (check
     both `SKILLS_DIR` and the host's default skills dir, e.g. `~/.claude/skills/`).
     If present, do not fetch a second copy.
   - **`matt-pocock`** — look for folders matching the upstream sub-skill names
     (e.g. `setup-matt-pocock-skills`, or any `SKILL.md` authored by Matt Pocock).
     If the set is already present, report it and skip the ones that exist.
   - If found: do **not** write `asp-<name>`. Report the existing install and
     ask whether to leave it, replace it with the pack's version, or keep both
     (discouraged — two skills with the same job confuse triggering).
3. **Absent** — install with the upstream-resolved method and target. For manual
   fallbacks, use `TARGET_FORMAT`: skill folder for skill-capable hosts, native
   `.mdc`/`.md` rule for Cursor or Windsurf/Devin, explicit confirmation before
   broad Copilot instructions, and read-only report for read-only flows. For
   Kilo-native skill folders, preserve the upstream folder/name and record ASP
   ownership in metadata instead of adding an `asp-` prefix.

### Layer 2 — optional tools

For `rtk`, `codegraph`, and `ponytail`, do not look for `asp-*` skill folders.
They are external tools or upstream plugin/ruleset installs with their own host
integrations and update flows.

- **rtk** — check `rtk --version`, then inspect only the current approved host
  hook/plugin setup. A global rtk binary does not imply every host is configured.
- **codegraph** — check `codegraph --version`, then inspect only the current
  approved host MCP setup and the current project's `.codegraph/` directory. A
  global CodeGraph binary does not imply every host is configured, and host MCP
  setup does not imply every project has an index.
- **ponytail** — inspect only the current approved host's Ponytail plugin,
  extension, hook, command, or instruction-rule setup. A Ponytail install in one
  host does not imply another host is configured. A rule-only copy is not the
  same as a command-capable plugin install.
- If the binary exists, report "binary already installed" and ask before running
  any host init/install command.
- If the host integration exists, report "host already configured" and ask
  before reinstalling, trusting hooks, or changing scope.
- If `.codegraph/` exists, report "project already indexed" and do not run
  `codegraph init` unless the user asks.

### Detection is best-effort, confirmation is the backstop

File-name and phrase heuristics will miss renamed or reworded installs. That is
fine: when unsure, *surface what you found and ask* rather than writing blind.
A duplicate install or a clobbered edit is far worse than one extra question.

## Marker reference

- On-demand skill/rule, first body line after frontmatter when possible:
  ```
  # source: ai-starter-pack <component> v1
  ```

Bump the version suffix when a payload changes; the bump is what drives the
diff-and-confirm path on the next run.
