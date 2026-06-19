---
name: ai-starter-pack
description: Set up a coding agent's everyday environment in one step — behavioral guardrails, terse-output style, design guidance, and shell-command hygiene — written as portable files that work across Claude Code, Codex, Antigravity, and any agent that follows the SKILL.md / AGENTS.md standard. Use this whenever the user says "set up my coding environment", "bootstrap my agent", "install my starter pack", "configure a new project for me", or starts working in a fresh repo or a freshly installed coding tool and wants their usual defaults in place. Also use when the user asks to add, list, update, or remove any of these components.
---

# AI Starter Pack

A self-installing pack. The agent reading this file **is** the installer — it uses
its own file tools to place a small set of behavioral files where the current host
expects them. No shell toolchain, npm, or curl is required for the default install.

The pack ships two kinds of content:

- **Always-on rails** — short behavioral guardrails that belong in the host's
  always-loaded context/rule file (`CLAUDE.md`, `AGENTS.md`, Cursor/Windsurf
  rules, etc.). These must load every session, so they go in the always-on
  surface, *not* in a lazily-triggered skill.
- **On-demand skills/rules** — self-contained `SKILL.md` folders for hosts that
  support skills, or the closest native model-decision/manual rule format for
  rule-only hosts (Cursor, Windsurf/Devin, Copilot).

One component (`rtk`) is **not** a pure skill — it is a compiled binary that
compresses shell output below the model. It is opt-in and installed by fetching
from upstream, never bundled. See `references/optional/rtk.md`.

## Run the install
> **Paths in this document are relative to this skill's directory** — the
> folder that contains this `SKILL.md` (e.g. `references/payloads/rails.md`,
> `LICENSES/...`). Resolve them from there regardless of where the skill is
> installed.


Follow these steps in order. Do not skip the dedup checks — re-running this pack,
or running it on a machine that already has some of these files, must never create
duplicates or silently overwrite the user's edits.

### 1. Detect the host and target directories

Read `references/dedup.md` → "Host detection" and resolve:

- `CONTEXT_FILE` — the always-loaded file (`CLAUDE.md` or `AGENTS.md`).
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
| `rails` | always-on | ✅ on | Guardrails: surface assumptions, stay minimal, make surgical edits, define verifiable success criteria |
| `caveman` | on-demand | optional | Terse output style — cuts filler tokens, keeps technical accuracy |
| `design` | on-demand | optional | Frontend/visual quality guidance — intentional, non-templated UI |
| `command-hygiene` | on-demand | optional | Teaches the agent to issue quiet, low-noise shell commands (a pure-skill stand-in for rtk) |
| `stop-slop` | on-demand (fetched) | off | Strips AI writing tells from prose. Fetched from upstream, not bundled. See `references/vendor/VENDORING.md` + `sources.json` |
| `matt-pocock` | skill set (fetched) | off | Matt Pocock's production engineering skills (TDD, architecture review, planning, git guardrails…). Fetched from upstream; let the user pick sub-skills. See `references/vendor/VENDORING.md` + `sources.json` |
| `rtk` | binary (opt-in) | off | Real deterministic shell-output compression. Needs a fetch + binary install. See `references/optional/rtk.md` |

If the user just says "everything" or "the usual", install `rails` +
`caveman` + `design` + `command-hygiene` and *ask* before doing `rtk`,
`stop-slop`, or `matt-pocock`, since those fetch code from the network (PATH/hook
for rtk; upstream skill folders for the other two).

### 3. Dedup BEFORE writing anything

For every selected component, run the matching check in `references/dedup.md`
→ "Dedup checks". In summary:

- **Already installed by this pack** (our marker present, same version) → skip,
  report "already current".
- **Installed by this pack, older version** → show a diff, ask before replacing.
- **Installed independently by the user** (e.g. they already ran the upstream
  caveman installer, or already have rails-like rules in their context file) →
  do **not** write a second copy. Report what you found and ask whether to leave
  it, replace it, or merge.
- **Absent** → install.

Idempotency comes from markers, so re-running is always safe:

- Context-file/rule blocks are wrapped in
  `<!-- BEGIN ai-starter-pack:rails v1 -->` … `<!-- END ai-starter-pack:rails -->`.
- Each on-demand skill/rule is named `asp-<component>` and carries
  `# source: ai-starter-pack <component> v1` near the top of the body.

### 4. Write the selected components

- **rails** → read `references/payloads/rails.md`. If `CONTEXT_FILE` does not
  exist, create it with the marked block. If it exists and has no
  `ai-starter-pack:rails` marker, append the marked block after one blank line —
  never rewrite the file. Preserve everything already there. For Cursor or
  Windsurf/Devin native rules, create a project rule file instead if the user
  chose that host-native format.
- **caveman / design / command-hygiene**:
  - `skill-folder` → copy `references/payloads/<name>.md` to
    `SKILLS_DIR/asp-<name>/SKILL.md`, creating the folder. Keep the frontmatter
    and source marker intact.
  - `cursor-rule` → convert the payload to `.cursor/rules/asp-<name>.mdc` with
    Cursor frontmatter (`description`, `globs: []`, `alwaysApply: false`) and
    keep the source marker in the body.
  - `windsurf-rule` → convert the payload to `.devin/rules/asp-<name>.md` with
    `trigger: model_decision` and a concise `description`; use
    `.windsurf/rules/` only when `.devin/rules/` is unavailable for the current
    client.
  - `copilot-instruction` → Copilot has no generic on-demand skill loader. Ask
    before turning optional components into broader repository instructions in
    `AGENTS.md`, `.github/copilot-instructions.md`, or
    `.github/instructions/asp-<name>.instructions.md`.
  - `read-only` → report the component as available to load via `--read` or by
    pasting/attaching the payload; do not invent a persistent install path.
- **stop-slop / matt-pocock** → only if explicitly chosen. These have **no
  bundled payload** — they install by fetching the upstream skill as-is. Follow
  `references/vendor/VENDORING.md` using the matching `sources.json` entry:
  detect a fetch primitive, resolve a concrete commit for any `PIN_AT_INSTALL`
  source, read the upstream LICENSE, copy the
  `SKILL.md` (+ listed reference files) into `SKILLS_DIR/asp-<name>/`, and write
  the upstream MIT notice to `LICENSES/<name>-upstream-MIT.txt`. For `matt-pocock`,
  let the user pick which of the ~21 sub-skills to install (or all). Stop and ask
  if no fetch tool is available.
- **rtk** → only if explicitly chosen. Follow `references/optional/rtk.md` exactly:
  detect a fetch primitive, narrate each command, install for the detected host,
  verify, and report. Stop and ask if no fetch tool is available.

### 5. Report

Summarize per component: installed / skipped (already current) / skipped (user
already had it) / updated. Tell the user the trigger phrases for the on-demand
skills and confirm the rails are active for the next session. Do not re-read or
narrate these instructions back to the user.

## Provenance and licensing

The default payloads in `references/payloads/` are original content authored for this pack
(MIT, see `LICENSES/`). They express well-known, freely-usable *ideas* (e.g.
"state your assumptions", "keep it minimal") in their own words; copying them
carries no third-party obligation.

If the user specifically wants the canonical upstream files instead (forrestchang's
Karpathy guidelines, JuliusBrussee's caveman), follow `references/vendor/VENDORING.md`: it
fetches those files at a pinned commit and installs their MIT notices alongside,
so attribution is correct. Default install does not require this.

## Adding, listing, updating, removing

- **list** → scan `CONTEXT_FILE` for the rails marker and `SKILLS_DIR` for
  `asp-*` folders; report what's present and at what version.
- **add** → run steps 1–5 for just the named component.
- **update** → re-run with the newer payload; the version bump in the marker
  triggers the diff-and-confirm path in step 3.
- **remove** → delete the marked block (rails) or the `asp-<name>` folder
  (skills). Never touch content outside the markers.
