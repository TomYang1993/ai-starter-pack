# Install

You can run the pack directly from GitHub. Installing the pack into a tool is
optional; it only makes the trigger phrase shorter in future chats.

## Fastest path - no clone

For any agent that can read public GitHub URLs, say:

> "Read https://github.com/TomYang1993/ai-starter-pack and set up my coding environment. Start from `skills/ai-starter-pack/SKILL.md`."

The agent reads `SKILL.md`, fetches only the referenced files it needs from the
same GitHub ref, detects your host, shows the component menu, runs the dedup
checks, and writes everything for you. **This is the primary flow.**

For updates, say:

> "Read https://github.com/TomYang1993/ai-starter-pack and update my coding environment. Start from `skills/ai-starter-pack/SKILL.md`."

## Local checkout path

When you already have this repo open locally, say:

> "Read `skills/ai-starter-pack/SKILL.md` from this repo and set up my coding environment."

Clone the repo when you want to audit the files locally, pin a commit, develop
the pack, or use the manual copy commands below.

## Persistent install path

Install **the pack** once per tool when you want the shorter phrase
**"set up my coding environment"** to work in fresh chats without pasting the raw
GitHub URL. The pack then installs individual components (`caveman`, optional
tools, etc.) for you - no per-component manual steps.

For Codex, use the built-in skill installer:

> "Use $skill-installer to install: https://github.com/TomYang1993/ai-starter-pack/tree/main/skills/ai-starter-pack"

The per-tool commands below are for persistent installs or manual fallback.

Use one pack entrypoint per tool. If the pack is already installed through a
marketplace/plugin, do not also copy the same skill folder manually unless you
are testing duplicate detection. Multiple entrypoints can make the tool show the
same pack twice; remove or ignore the older one after confirming which copy is
current.

Each tool installs its own copy/config. Claude Code should set up Claude Code;
Codex should set up Codex; Cursor should set up Cursor. Ask for another tool by
name only when you intentionally want cross-tool setup.

## Claude Code

**Option A - Plugin marketplace (recommended)**

```text
/plugin marketplace add TomYang1993/ai-starter-pack
/plugin install ai-starter-pack@ai-starter-pack
```

**Option B - Skills CLI**

```bash
npx skills add TomYang1993/ai-starter-pack --skill ai-starter-pack --agent claude-code
```

**Option C - Manual**

```bash
# Global
cp -r skills/ai-starter-pack ~/.claude/skills/ai-starter-pack
# Project-local
cp -r skills/ai-starter-pack .claude/skills/ai-starter-pack
```

## Codex (OpenAI)

**Option A - Skill installer (recommended)**

In Codex, say:

```text
Use $skill-installer to install: https://github.com/TomYang1993/ai-starter-pack/tree/main/skills/ai-starter-pack
```

Restart Codex if the skill does not appear, then say:

> "set up my coding environment"

**Option B - Plugin marketplace (packaged/advanced)**

Use this when you want the pack installed as a Codex plugin package rather than
as a plain skill.

```bash
codex plugin marketplace add TomYang1993/ai-starter-pack
codex plugin add ai-starter-pack@ai-starter-pack
```

Restart if prompted, then say:

> "set up my coding environment"

You can also open Codex's plugin directory with `/plugins`, choose the AI
Starter Pack entry, and install it from there.

**Option C - Manual skill install (local testing/fallback)**

```bash
# Manual - global
mkdir -p ~/.agents/skills
cp -r skills/ai-starter-pack ~/.agents/skills/ai-starter-pack

# Manual - project-local
mkdir -p .agents/skills
cp -r skills/ai-starter-pack .agents/skills/ai-starter-pack
```

Codex reads `AGENTS.md` at the repo root and discovers skills from user and
repo skill directories. The `$skill-installer` path is the normal Codex skill
install flow. This repo also ships a `.codex-plugin/plugin.json` manifest and
`.agents/plugins/marketplace.json` catalog for packaging the pack as a Codex
plugin.

## Kilo Code

Kilo Code has native Agent Skills support. For a project-local install:

```bash
mkdir -p /path/to/your-project/.kilo/skills
cp -r skills/ai-starter-pack /path/to/your-project/.kilo/skills/ai-starter-pack
```

For a global install:

```bash
mkdir -p ~/.kilo/skills
cp -r skills/ai-starter-pack ~/.kilo/skills/ai-starter-pack
```

Then start a new Kilo Code session and say:

> "set up my coding environment"

Kilo Code also reads `.agents/skills/` as a compatibility directory, so a shared
Codex/Kilo project can use that path deliberately. Prefer `.kilo/skills/` for a
Kilo-only install because it is Kilo's native location. The skill folder name
should match the `name:` in `SKILL.md`; this pack already uses
`ai-starter-pack`.

If you use `AGENTS.md`, keep it as a bootstrap/context file that points to the
installed skill. Kilo also supports extra `skills.paths` and `skills.urls` in
`kilo.jsonc` when you intentionally want a shared or remote skill source.

## Cursor

Cursor loads rules from `.cursor/rules/*.mdc`. This repo ships
`.cursor/rules/ai-starter-pack.mdc` ready to go.

**If working inside this repo:** Cursor already picks it up - no extra step.

**To install into another project:**

```bash
mkdir -p /path/to/your-project/.cursor/rules
mkdir -p /path/to/your-project/skills
cp .cursor/rules/ai-starter-pack.mdc /path/to/your-project/.cursor/rules/
cp -r skills/ai-starter-pack /path/to/your-project/skills/ai-starter-pack
```

Then open that project in Cursor and say: **"set up my coding environment"**

**Global install:** Cursor's current global surface is **Cursor Settings > Rules**
(`User Rules`). Add a short bootstrap there that points at a stable local copy of
`skills/ai-starter-pack/SKILL.md`. For team/repo installs, prefer the project
rule above because it is versioned and portable.

Cursor also supports `AGENTS.md` in the project root and subdirectories, so a
repo-level `AGENTS.md` bootstrap is the simplest fallback when you do not need
Cursor-specific rule metadata.

## Windsurf / Devin

Windsurf/Devin currently prefers `.devin/rules/*.md` for workspace rules and
keeps `.windsurf/rules/*.md` plus root `.windsurfrules` as legacy/fallback
surfaces. It also reads `AGENTS.md`.

**Project install:**

```bash
# Clone or copy this repo into your project, then:
cp -r skills/ai-starter-pack /path/to/your-project/skills/

# Add bootstrap as a workspace rule
mkdir -p /path/to/your-project/.devin/rules
cat > /path/to/your-project/.devin/rules/ai-starter-pack.md << 'EOF'
---
trigger: model_decision
description: Load AI Starter Pack when the user wants coding-agent defaults installed.
---

# AI Starter Pack
When the user says "set up my coding environment" or "bootstrap my agent",
load and run skills/ai-starter-pack/SKILL.md to install components.
EOF
```

**Global install:**

```bash
mkdir -p ~/.codeium/windsurf/memories
cp -r skills/ai-starter-pack ~/.codeium/windsurf/memories/
cat >> ~/.codeium/windsurf/memories/global_rules.md << 'EOF'

# AI Starter Pack
When the user says "set up my coding environment" or "bootstrap my agent",
load and run the skill at ~/.codeium/windsurf/memories/ai-starter-pack/SKILL.md.
EOF
```

## GitHub Copilot (VS Code / JetBrains)

Copilot supports repository-wide `.github/copilot-instructions.md`,
path-specific `.github/instructions/*.instructions.md`, and agent instructions
via `AGENTS.md`.

```bash
mkdir -p /path/to/your-project/.github
mkdir -p /path/to/your-project/.github/ai-starter-pack

cp -r skills/ai-starter-pack /path/to/your-project/.github/ai-starter-pack/ai-starter-pack

cat >> /path/to/your-project/.github/copilot-instructions.md << 'EOF'

## AI Starter Pack
When the user says "set up my coding environment" or "bootstrap my agent",
load and run `.github/ai-starter-pack/ai-starter-pack/SKILL.md` to install components.
EOF
```

For Copilot agents, adding the same bootstrap to `AGENTS.md` is often cleaner
because Copilot now recognizes `AGENTS.md` agent instructions directly.

## Any other agent

Copy the skill where the agent loads on-demand skills, then tell it to read
`SKILL.md`. As a fallback, paste `SKILL.md` content directly into the context.
The pack's only requirement: **an agent that can read and write files.**

## After installing

For initial setup, say:

> "set up my coding environment"

When you want to refresh the environment managed by AI Starter Pack, say:

> "update my coding environment"

If the tool does not auto-load installed skills or cannot find the pack, say:

> "Read `skills/ai-starter-pack/SKILL.md` from this repo and update my coding environment."

The pack shows the component menu, runs dedup checks, and writes only what you
pick. During updates, it replaces only AI Starter Pack-managed files that still
match what the pack previously installed.

## Advanced management

These are optional follow-up commands for users who want more control:

- **List** - "what's in my starter pack here?"
- **Add one** - "add caveman to this project"
- **Remove** - "remove the caveman skill"
- **rtk** - "install rtk" (opt-in binary with per-tool hook setup; see
  `skills/ai-starter-pack/references/optional/rtk.md`)
- **CodeGraph** - "install codegraph" (opt-in local CLI/MCP with per-tool host
  setup and per-project indexing; see
  `skills/ai-starter-pack/references/optional/codegraph.md`)
- **Ponytail** - "install ponytail" (opt-in upstream plugin/ruleset with
  per-tool setup; see
  `skills/ai-starter-pack/references/optional/ponytail.md`)

## Notes

Skills-dir/rules paths per host (`skills/ai-starter-pack/references/dedup.md`)
use current documented conventions; verify against your actual install if a tool
moved its dirs. rtk, CodeGraph, and Ponytail setup use upstream docs, with only
starter-pack-specific adapter notes in
`skills/ai-starter-pack/references/optional/rtk.md`,
`skills/ai-starter-pack/references/optional/codegraph.md`, and
`skills/ai-starter-pack/references/optional/ponytail.md`.
Windsurf/Devin naming has shifted over time - prefer `.devin/rules/` for new
workspace rules and keep `.windsurf/rules/` / `.windsurfrules` as fallback only
when the client expects them.

Cross-tool setup is file-based, not magic. An agent can help write project-local
files for another host when those paths are available in the workspace, and it
can write global host files only when the user approves those file writes. It
cannot silently change another app's private settings, install marketplace
plugins, or bypass OS/sandbox permissions.
