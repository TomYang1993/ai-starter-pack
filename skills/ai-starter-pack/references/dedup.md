# Host detection and dedup

Detail kept out of `SKILL.md` so the orchestrator stays short. Read this when
running install steps 1 and 3.

## Host detection

Resolve four values: `CONTEXT_FILE`, `SKILLS_DIR`, `TARGET_FORMAT`, `SCOPE`.

### Scope

Default to **project-local** (writes land in the current repo, travel with it,
and are easy to review in a diff). Use **global** only if the user asks for
"all my projects" / "everywhere". Override with `ASP_SCOPE=project|global`.

### Signals

The active host is the tool currently running this installer. Install into that
host by default. Other host directories in the same repo or home folder are only
inventory and duplicate-check signals; they are not permission to configure
those tools, and they must not override the current runtime.

Resolve the host in this order:

1. Explicit override: `ASP_AGENT=claude|cursor|windsurf|codex|copilot|antigravity|kilo|generic`.
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
scope they want. Do not guess from filesystem hints alone.

| Host | Project context/rule file | Global context/rule file | Project skill/rule dir | Global skill/rule dir | Target format |
|---|---|---|---|---|---|
| Claude Code | `CLAUDE.md` | `~/.claude/CLAUDE.md` | `.claude/skills/` | `~/.claude/skills/` | `skill-folder` |
| Codex | `AGENTS.md` | `~/.codex/AGENTS.md` | `.agents/skills/` | `~/.agents/skills/` | `skill-folder` |
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

## Pack entrypoint duplicates

Some hosts can load AI Starter Pack through more than one mechanism, such as a
marketplace/plugin install, a Skills CLI install, and a manually copied skill
folder. Treat these as duplicate entrypoints for the **pack itself**, not as
separate environments to configure.

Before installing the pack or when diagnosing duplicate triggers:

1. Look for the same `ai-starter-pack` skill/plugin in every known entrypoint for
   the current host and scope (for example Claude Code marketplace/plugin plus
   `.claude/skills/ai-starter-pack` or `~/.claude/skills/ai-starter-pack`).
2. Prefer the host-native package/plugin entrypoint when it exists and is current.
3. Do not copy another skill folder just because one entrypoint was already
   present. Report the duplicate and ask whether to keep the current entrypoint,
   remove the older copy, or intentionally keep both for testing.
4. Component install/update dedup still runs after the pack entrypoint is chosen.

## Dedup checks

The goal: never write a file the user already has, never clobber their edits,
and make re-running a no-op.

### Layer 1 — on-demand skills or converted rules

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
3. **Absent** — install according to `TARGET_FORMAT`: skill folder for
   skill-capable hosts, native `.mdc`/`.md` rule for Cursor or Windsurf/Devin,
   explicit confirmation before broad Copilot instructions, and read-only report
   for read-only flows. For Kilo-native skill folders, preserve the upstream
   folder/name and record ASP ownership in metadata instead of adding an
   `asp-` prefix.

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
