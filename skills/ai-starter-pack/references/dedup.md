# Host detection and dedup

Detail kept out of `SKILL.md` so the orchestrator stays short. Read this when
running install steps 1 and 3.

## Host detection

Resolve three values: `CONTEXT_FILE`, `SKILLS_DIR`, `SCOPE`.

### Scope

Default to **project-local** (writes land in the current repo, travel with it,
and are easy to review in a diff). Use **global** only if the user asks for
"all my projects" / "everywhere". Override with `ASP_SCOPE=project|global`.

### Signals

Check, in order, and stop at the first confident match. If two hosts both look
present (e.g. both `CLAUDE.md` and `AGENTS.md` exist), ask the user.

| Host | Context file | Project skills dir | Global skills dir |
|---|---|---|---|
| Claude Code | `CLAUDE.md` | `.claude/skills/` | `~/.claude/skills/` |
| Cursor | `.cursorrules` | `.cursor/rules/` | `~/.cursor/rules/` |
| Windsurf | `.windsurfrules` | `.windsurf/rules/` | `~/.codeium/windsurf/memories/` |
| Codex | `AGENTS.md` | `.codex/skills/` | `~/.codex/skills/` |
| Aider | `AGENTS.md` | `.aider/skills/` | `~/.aider/skills/` |
| Copilot | `.github/copilot-instructions.md` | `.github/` | `~/.github/` |
| Antigravity | `AGENTS.md` | `.agents/skills/` | `~/.agents/skills/` |
| Generic / other | `AGENTS.md` | `.agents/skills/` | `~/.agents/skills/` |

Detection hints:

- A `.claude/` directory or an existing `CLAUDE.md` → Claude Code.
- A `.cursor/` directory or `.cursorrules` file → Cursor.
- A `.windsurfrules` file or `.windsurf/` directory → Windsurf.
- A `.codex/` directory → Codex.
- A `.github/copilot-instructions.md` file → Copilot.
- An `AGENTS.md` with no Claude markers → treat as the generic `AGENTS.md`
  family (Codex / Aider / Antigravity / others all read `AGENTS.md`).
- `ASP_AGENT=claude|cursor|windsurf|codex|copilot|aider|antigravity|generic`
  overrides all of the above.

If nothing matches, the safest default is `AGENTS.md` + `.agents/skills/`, since
`AGENTS.md` is the most widely-read context file. Tell the user what you picked.

## Dedup checks

The goal: never write a file the user already has, never clobber their edits,
and make re-running a no-op. Two layers, two strategies.

### Layer 1 — rails in the context file

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

### Layer 2 — on-demand skills in the skills dir

For each of `caveman`, `design`, `command-hygiene`:

1. **Our copy present** — `SKILLS_DIR/asp-<name>/SKILL.md` exists:
   - Read its source-marker line. Same version → skip. Older → diff + confirm.
2. **User's independent copy present** — a sibling folder whose `SKILL.md` `name`
   frontmatter (or folder name) matches the component's purpose. Examples to look
   for before writing `asp-caveman`: a folder named `caveman`, or any `SKILL.md`
   whose `name` is `caveman` / contains "caveman". For `command-hygiene`, also
   check whether `rtk` is already installed (run `rtk --version`); if rtk is
   active, command-hygiene is redundant — say so and default to skipping it.
   - If found: do **not** write `asp-<name>`. Report the existing install and
     ask whether to leave it, replace it with the pack's version, or keep both
     (discouraged — two skills with the same job confuse triggering).
3. **Absent** — create `SKILLS_DIR/asp-<name>/` and write `SKILL.md`.

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
- On-demand skill, first body line after frontmatter:
  ```
  # source: ai-starter-pack <component> v1
  ```

Bump the version suffix when a payload changes; the bump is what drives the
diff-and-confirm path on the next run.
