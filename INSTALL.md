# Installing the AI Starter Pack

Install **the pack** once per tool. The pack then installs individual components
(rails, caveman, design, etc.) for you — no per-component manual steps.

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
# Skills CLI
npx skills add TomYang1993/ai-starter-pack --skill ai-starter-pack --agent codex

# Manual — global
cp -r skills/ai-starter-pack ~/.codex/skills/ai-starter-pack
# Manual — project-local
cp -r skills/ai-starter-pack .codex/skills/ai-starter-pack
```

Codex also reads `AGENTS.md` at the repo root — already present in this repo, so
cloning it into a project gives Codex the bootstrap automatically.

---

## Cursor

Cursor loads rules from `.cursor/rules/*.mdc`. This repo ships
`.cursor/rules/ai-starter-pack.mdc` ready to go.

**If working inside this repo:** Cursor already picks it up — no extra step.

**To install into another project:**

```bash
mkdir -p /path/to/your-project/.cursor/rules
cp .cursor/rules/ai-starter-pack.mdc /path/to/your-project/.cursor/rules/
cp -r skills/ai-starter-pack /path/to/your-project/.cursor/rules/
```

Then open that project in Cursor and say: **"set up my coding environment"**

**Global install (applies to all Cursor projects):**

```bash
mkdir -p ~/.cursor/rules
cp .cursor/rules/ai-starter-pack.mdc ~/.cursor/rules/
cp -r skills/ai-starter-pack ~/.cursor/rules/
```

---

## Windsurf

Windsurf reads `.windsurfrules` (project) or `~/.codeium/windsurf/memories/global_rules.md` (global).
It also reads `AGENTS.md`.

**Project install:**

```bash
# Clone or copy this repo into your project, then:
cp -r skills/ai-starter-pack /path/to/your-project/skills/

# Add bootstrap to .windsurfrules
cat >> /path/to/your-project/.windsurfrules << 'EOF'

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

Copilot reads `.github/copilot-instructions.md` automatically in VS Code.

```bash
mkdir -p /path/to/your-project/.github
mkdir -p /path/to/your-project/.github/ai-starter-pack

cp -r skills/ai-starter-pack /path/to/your-project/.github/ai-starter-pack/

cat >> /path/to/your-project/.github/copilot-instructions.md << 'EOF'

## AI Starter Pack
When the user says "set up my coding environment" or "bootstrap my agent",
load and run `.github/ai-starter-pack/SKILL.md` to install components.
EOF
```

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

- Skills-dir paths per host (`skills/ai-starter-pack/references/dedup.md`) use
  common conventions; verify against your actual install if a tool moved its dirs.
- `rtk init` flags (`references/optional/rtk.md`) should be checked against
  rtk's current README — it's a fast-moving binary.
- Windsurf path `~/.codeium/windsurf/memories/` is current as of mid-2025; check
  Windsurf docs if the global rules location has changed.
