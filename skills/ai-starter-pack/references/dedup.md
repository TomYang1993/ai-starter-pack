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

Check, in order, and stop at the first confident match. If two hosts both look
present (e.g. both `CLAUDE.md` and `AGENTS.md` exist), ask the user.

| Host | Project context/rule file | Global context/rule file | Project skill/rule dir | Global skill/rule dir | Target format |
|---|---|---|---|---|---|
| Claude Code | `CLAUDE.md` | `~/.claude/CLAUDE.md` | `.claude/skills/` | `~/.claude/skills/` | `skill-folder` |
| Codex | `AGENTS.md` | `~/.codex/AGENTS.md` | `.agents/skills/` | `~/.agents/skills/` | `skill-folder` |
| Cursor | `AGENTS.md` or `.cursor/rules/asp-rails.mdc` | Cursor Settings → Rules | `.cursor/rules/` | Cursor Settings → Rules | `cursor-rule` |
| Windsurf / Devin | `AGENTS.md` or `.devin/rules/asp-rails.md` | `~/.codeium/windsurf/memories/global_rules.md` | `.devin/rules/` | `~/.codeium/windsurf/memories/` | `windsurf-rule` |
| GitHub Copilot | `AGENTS.md` or `.github/copilot-instructions.md` | none | `.github/instructions/` | none | `copilot-instruction` |
| Aider | `AGENTS.md` or a file loaded with `--read` | `.aider.conf.yml` `read:` entry | none | none | `read-only` |
| Antigravity | `AGENTS.md` | verify current host docs | `.agents/skills/` if supported | `~/.agents/skills/` if supported | `skill-folder` if supported, otherwise `read-only` |
| Generic / other | `AGENTS.md` | `~/.agents/AGENTS.md` if supported | `.agents/skills/` | `~/.agents/skills/` | `skill-folder` |

Detection hints:

- A `.claude/` directory or an existing `CLAUDE.md` → Claude Code.
- A `.cursor/` directory or `.cursorrules` file → Cursor.
- A `.devin/`, `.windsurf/`, or `.windsurfrules` file → Windsurf / Devin.
- A `.codex/` directory → Codex.
- A `.github/copilot-instructions.md` file → Copilot.
- An `AGENTS.md` with no Claude markers → treat as the generic `AGENTS.md`
  family (Codex / Aider / Antigravity / others all read `AGENTS.md`).
- `ASP_AGENT=claude|cursor|windsurf|codex|copilot|aider|antigravity|generic`
  overrides all of the above.

If nothing matches, the safest default is `AGENTS.md` + `.agents/skills/` with
`TARGET_FORMAT=skill-folder`, since `AGENTS.md` is the most widely-read context
file and `.agents/skills/` is the shared skill location used by current Codex and
the open Agent Skills ecosystem. Tell the user what you picked.

## Dedup checks

The goal: never write a file the user already has, never clobber their edits,
and make re-running a no-op. Two layers, two strategies.

### Layer 1 — rails in the context/rule file

1. If `CONTEXT_FILE` is missing → no conflict, install creates it.
2. If it exists, search for `<!-- BEGIN ai-starter-pack:rails`:
   - **Marker found, same version** (`v1`) → already current, skip.
   - **Marker found, older version** → extract the old block, show the user a
     diff against `references/payloads/rails.md`, install only on confirmation by replacing
     the bytes *between* the BEGIN/END markers. Leave the rest of the file byte-
     for-byte unchanged.
3. If no marker, scan for signs the user already has equivalent rules
   (independent install). Heuristic phrases: "surface assumptions", "surgical",
   "minimal change", "success criteria", "do not over-engineer", or a heading
   like "Karpathy". If two or more appear:
   - Report: "Your context file already contains guardrail-style rules that
     overlap with `rails`." Ask: leave as-is / append ours anyway / show me both.
   - Default to **leave as-is** — duplicate guardrails waste context and can
     contradict each other.
4. Only if none of the above → append the marked block after one blank line.

Never rewrite or reorder the existing context file. Append or splice the marked
region only.

### Layer 2 — on-demand skills or converted rules

For each of `caveman`, `design`, `command-hygiene`, `stop-slop`, `matt-pocock`:

1. **Our copy present**:
   - `skill-folder`: `SKILLS_DIR/asp-<name>/SKILL.md` exists.
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
   whose `name` is `caveman` / contains "caveman". For `command-hygiene`, also
   check whether `rtk` is already installed (run `rtk --version`); if rtk is
   active, command-hygiene is redundant — say so and default to skipping it.
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
   for Aider-style flows.

### Detection is best-effort, confirmation is the backstop

File-name and phrase heuristics will miss renamed or reworded installs. That is
fine: when unsure, *surface what you found and ask* rather than writing blind.
A duplicate guardrail or a clobbered edit is far worse than one extra question.

## Marker reference

- Rails block in context file:
  ```
  <!-- BEGIN ai-starter-pack:rails v1 -->
  ...payload...
  <!-- END ai-starter-pack:rails -->
  ```
- On-demand skill/rule, first body line after frontmatter when possible:
  ```
  # source: ai-starter-pack <component> v1
  ```

Bump the version suffix when a payload changes; the bump is what drives the
diff-and-confirm path on the next run.
