# Installing the AI Starter Pack

Install **the pack** once per tool. The pack then installs individual components
(rails, caveman, design, etc.) for you — no per-component manual steps.

Host-specific paths are maintained in
`skills/ai-starter-pack/references/hosts.json`. The commands below are the
human-facing install shortcuts for that registry.

---

## Claude Code

### Option A — Plugin marketplace (recommended)

```text
/plugin marketplace add TomYang1993/ai-starter-pack
/plugin install ai-starter-pack@ai-starter-pack
```

### Option B — Skills CLI

```bash
npx skills add TomYang1993/ai-starter-pack --skill ai-starter-pack --agent claude-code
```

### Option C — Manual

```bash
# Global
cp -r skills/ai-starter-pack ~/.claude/skills/ai-starter-pack
# Project-local
cp -r skills/ai-starter-pack .claude/skills/ai-starter-pack
```

---

## Codex (OpenAI)

```bash
# Manual — global
mkdir -p ~/.agents/skills
cp -r skills/ai-starter-pack ~/.agents/skills/ai-starter-pack

# Manual — project-local
mkdir -p .agents/skills
cp -r skills/ai-starter-pack .agents/skills/ai-starter-pack
```

Codex reads `AGENTS.md` at the repo root and discovers skills from
`.agents/skills/` in the repo or `~/.agents/skills/` for the user. This repo also
ships a `.codex-plugin/plugin.json` manifest for packaging the pack as a Codex
plugin.

---

## Cursor

Cursor loads rules from `.cursor/rules/*.mdc`. This repo ships
`.cursor/rules/ai-starter-pack.mdc` ready to go.

**If working inside this repo:** Cursor already picks it up — no extra step.

**To install into another project:**

```bash
mkdir -p /path/to/your-project/.cursor/rules
mkdir -p /path/to/your-project/skills
cp .cursor/rules/ai-starter-pack.mdc /path/to/your-project/.cursor/rules/
cp -r skills/ai-starter-pack /path/to/your-project/skills/ai-starter-pack
```

Then open that project in Cursor and say: **"set up my coding environment"**

**Global install:** Cursor's current global surface is **Cursor Settings → Rules**
(`User Rules`). Add a short bootstrap there that points at a stable local copy of
`skills/ai-starter-pack/SKILL.md`. For team/repo installs, prefer the project
rule above because it is versioned and portable.

Cursor also supports `AGENTS.md` in the project root and subdirectories, so a
repo-level `AGENTS.md` bootstrap is the simplest fallback when you do not need
Cursor-specific rule metadata.

---

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

---

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

---

## Aider

Aider loads files via `--read`. Pass the skill at startup:

```bash
aider --read skills/ai-starter-pack/SKILL.md
```

Or add it to `.aider.conf.yml` in your project:

```yaml
read:
  - skills/ai-starter-pack/SKILL.md
```

Then say: **"set up my coding environment"**

---

## Any other agent (generic)

Copy the skill where the agent loads on-demand skills, then tell it to read
`SKILL.md`. As a fallback, paste `SKILL.md` content directly into the context.

The pack's only requirement: **an agent that can read and write files.**

---

## After installing in any tool

Say one of:

> "set up my coding environment"  
> "bootstrap my agent"  
> "install my starter pack"

The pack shows a component menu, runs dedup checks, and writes only what you pick.

---

## Managing installed components

- **List** — "what's in my starter pack here?"
- **Add one** — "add caveman to this project"
- **Update** — "update my starter pack"
- **Remove** — "remove the design skill"
- **rtk** — "install rtk" (opt-in binary; see `references/optional/rtk.md`)

## Self-propagation

Once loaded in one tool, the pack can populate another tool's directories.
Install once in Claude Code, then say:

> "also set up my Cursor environment"

and it cascades — no second manual install needed.

## Notes

- Skills-dir/rules paths per host (`skills/ai-starter-pack/references/dedup.md`)
  are sourced from `skills/ai-starter-pack/references/hosts.json`. Run
  `skills/ai-starter-pack/scripts/validate_hosts.py` after changing host docs.
- `rtk init` flags (`references/optional/rtk.md`) should be checked against
  rtk's current README — it's a fast-moving binary.
- Windsurf/Devin naming has changed over time. Prefer `.devin/rules/` for new
  workspace rules and keep `.windsurf/rules/` / `.windsurfrules` as fallback
  only when the installed client still expects them.
