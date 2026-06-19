# AI Starter Pack

A one-step setup for a coding agent's everyday defaults. Works best in agents
with first-class `SKILL.md` support (Claude Code and Codex) and also bootstraps
rule/instruction-based tools such as Cursor, Windsurf/Devin, GitHub Copilot,
Aider, Antigravity, and other `AGENTS.md` readers.

The pack is **self-installing**: the agent reading it uses its own file tools to
place the right files where your host expects them. The installer itself is just
files, but selected third-party components are fetched from their upstream repos
at a pinned commit so the original authors' work stays intact. You install *the
pack* once; the pack installs the components for you, conversationally.

## Install

Install **the pack** once per tool. The pack then installs individual components
(andrej-karpathy-skills, caveman, impeccable, etc.) for you — no per-component
manual steps. After installing in any tool, say **"set up my coding environment"**
and pick from the menu.

### Claude Code

**Option A — Plugin marketplace (recommended)**

```text
/plugin marketplace add TomYang1993/ai-starter-pack
/plugin install ai-starter-pack@ai-starter-pack
```

**Option B — Skills CLI**

```bash
npx skills add TomYang1993/ai-starter-pack --skill ai-starter-pack --agent claude-code
```

**Option C — Manual**

```bash
# Global
cp -r skills/ai-starter-pack ~/.claude/skills/ai-starter-pack
# Project-local
cp -r skills/ai-starter-pack .claude/skills/ai-starter-pack
```

### Codex (OpenAI)

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

### Cursor

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

### Windsurf / Devin

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

### GitHub Copilot (VS Code / JetBrains)

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

### Aider

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

### Any other agent (generic)

Copy the skill where the agent loads on-demand skills, then tell it to read
`SKILL.md`. As a fallback, paste `SKILL.md` content directly into the context.
The pack's only requirement: **an agent that can read and write files.**

### After installing

Say one of: **"set up my coding environment"**, **"bootstrap my agent"**, or
**"install my starter pack"**. The pack shows the component menu, runs dedup
checks, and writes only what you pick. Manage it later with:

- **List** — "what's in my starter pack here?"
- **Add one** — "add caveman to this project"
- **Update** — "update my starter pack"
- **Remove** — "remove the impeccable skill"
- **rtk** — "install rtk" (opt-in binary; see `references/optional/rtk.md`)

Once loaded in one tool, the pack can populate another's directories — install
once in Claude Code, then say "also set up my Cursor environment" and it cascades.

**Notes:** Skills-dir/rules paths per host
(`skills/ai-starter-pack/references/dedup.md`) use current documented conventions;
verify against your actual install if a tool moved its dirs. `rtk init` flags
(`references/optional/rtk.md`) track a fast-moving binary. Windsurf/Devin naming
has shifted over time — prefer `.devin/rules/` for new workspace rules and keep
`.windsurf/rules/` / `.windsurfrules` as fallback only when the client expects them.

## What's in it

| Component | Type | Default | Source | What it does |
|---|---|---|---|---|
| `andrej-karpathy-skills` | always-on | recommended | Forrest Chang's `andrej-karpathy-skills` | Karpathy-style coding-agent guardrails |
| `caveman` | on-demand | optional | Julius Brussee's `caveman` | Terse output — fewer tokens, same accuracy |
| `impeccable` | on-demand | optional | Paul Bakaus's `impeccable` | Frontend/UI craft, critique, polish, and design workflows |
| `stop-slop` | on-demand | opt-in | Hardik Pandya's `stop-slop` | Strips AI writing tells from prose |
| `matt-pocock` | skill set | opt-in | Matt Pocock's `skills` | Engineering skills — TDD, architecture review, planning… |
| `rtk` | binary | opt-in | `rtk-ai/rtk` | Real deterministic shell-output compression |

`andrej-karpathy-skills` installs into your always-loaded context file or native
rule file (`CLAUDE.md`, `AGENTS.md`, Cursor/Windsurf rules, etc.) so it applies
every session. Third-party skills install from upstream originals at pinned
commits with their licenses and notices preserved. In skill-capable hosts, the
on-demand components load only when their topic comes up. In rule-only hosts, the
pack writes the closest native model-decision/manual rule format the host
supports. `rtk` is infrastructure and only installs if you ask.

## Repo layout

```
ai-starter-pack/
├── README.md                      # this file (install steps live here)
├── AGENTS.md                      # root bootstrap for Codex / Windsurf / Aider / generic
├── LICENSE                        # MIT (this pack's original content)
├── .claude-plugin/                # Claude Code plugin marketplace manifests
├── .codex-plugin/                 # Codex plugin manifest
├── .cursor/rules/                 # Cursor auto-loaded rule
└── skills/
    └── ai-starter-pack/           # the skill itself (the distributable unit)
        ├── SKILL.md               # orchestrator: menu, host-detect, dedup, install
        ├── NOTICE.md              # provenance & attribution
        ├── LICENSES/
        └── references/
            ├── dedup.md           # host-detection + dedup algorithm
            ├── optional/          # rtk opt-in install flow
            └── vendor/            # upstream-original source registry
```

## Safe to re-run

Every component is marked, so re-running never duplicates anything. If you
already installed one of these — or have your own guardrails in your context
file — the pack detects it and asks rather than writing a second copy. See
`skills/ai-starter-pack/references/dedup.md`.

## Credits & Thanks

| Component | What it installs | Credit |
|---|---|---|
| `andrej-karpathy-skills` | Always-on guardrails in your context file | **[Forrest Chang](https://github.com/forrestchang)** — [`andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills) (MIT), based on coding-agent guidance from **[Andrej Karpathy](https://github.com/karpathy)** |
| `caveman` | On-demand terse-output skill | **[Julius Brussee](https://github.com/JuliusBrussee)** — [`caveman`](https://github.com/JuliusBrussee/caveman) (MIT) |
| `impeccable` | On-demand frontend/UI design skill | **[Paul Bakaus](https://github.com/pbakaus)** — [`impeccable`](https://github.com/pbakaus/impeccable) (Apache-2.0) |
| `stop-slop` | On-demand prose-cleanup skill (fetched as-is) | **[Hardik Pandya](https://hvpandya.com)** — [`hardikpandya/stop-slop`](https://github.com/hardikpandya/stop-slop) (MIT) |
| `matt-pocock` | Engineering skill set (fetched as-is) | **[Matt Pocock](https://github.com/mattpocock)** — [`mattpocock/skills`](https://github.com/mattpocock/skills) (MIT) |
| `rtk` | Opt-in shell-output compression binary | **[rtk-ai](https://github.com/rtk-ai/rtk)** — RTK "Rust Token Killer" (Apache-2.0); fetched from upstream, never bundled |

This pack is glue around your work, all credit is yours.
If you maintain one of these and want the attribution worded
differently, open an issue.
