# AI Starter Pack

A one-step setup for a coding agent's everyday defaults. Works best in agents
with first-class `SKILL.md` support (Claude Code and Codex) and also bootstraps
rule/instruction-based tools such as Cursor, Windsurf/Devin, GitHub Copilot,
Aider, Antigravity, and other `AGENTS.md` readers.

The pack is **self-installing**: the agent reading it uses its own file tools to
place the right files where your host expects them. No npm, curl, or toolchain
needed for the default install — the only capability required is "an agent that
can write a file." You install *the pack* once; the pack installs the components
for you, conversationally. There is no per-component manual step.

## Supported tools

| Tool | How the pack loads | Install entry point |
|---|---|---|
| **Claude Code** | Plugin marketplace or skills dir | `.claude-plugin/` manifests, `~/.claude/skills/` |
| **Codex** | Reads root `AGENTS.md` + `.agents/skills/` | `AGENTS.md`, `.agents/skills/`, `~/.agents/skills/` |
| **Cursor** | Reads Project Rules and `AGENTS.md` | `.cursor/rules/ai-starter-pack.mdc`, `AGENTS.md` |
| **Windsurf / Devin** | Reads Rules and `AGENTS.md` | `.devin/rules/`, `.windsurf/rules/`, `AGENTS.md` |
| **GitHub Copilot** | Reads repo and agent instructions | `.github/copilot-instructions.md`, `.github/instructions/`, `AGENTS.md` |
| **Aider** | Loaded via `--read` / `AGENTS.md` | `aider --read skills/ai-starter-pack/SKILL.md` |
| **Antigravity** | Uses `AGENTS.md`-style agent instructions where available | `AGENTS.md`, verify current host-specific skill/rule path |
| **Any other agent** | Reads `SKILL.md` / `AGENTS.md` | generic `AGENTS.md` + skills dir |

Exact commands for each are in [INSTALL.md](INSTALL.md).

## What's in it

| Component | Type | Default | What it does |
|---|---|---|---|
| `rails` | always-on | ✅ | Guardrails: surface assumptions, stay minimal, surgical edits, verify success |
| `caveman` | on-demand | optional | Terse output — fewer tokens, same accuracy |
| `design` | on-demand | optional | Intentional, non-templated UI work |
| `command-hygiene` | on-demand | optional | Quiet, low-noise shell commands (pure-skill rtk stand-in) |
| `stop-slop` | on-demand | opt-in | Strips AI writing tells from prose (fetched from upstream) |
| `matt-pocock` | skill set | opt-in | Matt Pocock's engineering skills — TDD, architecture review, planning… (fetched) |
| `rtk` | binary | opt-in | Real deterministic shell-output compression (fetched, not bundled) |

`rails` install into your always-loaded context file or native rule file
(`CLAUDE.md`, `AGENTS.md`, Cursor/Windsurf rules, etc.) so they apply every
session. In skill-capable hosts, the on-demand components load only when their
topic comes up. In rule-only hosts, the pack writes the closest native
model-decision/manual rule format the host supports. `rtk` is infrastructure and
only installs if you ask.

## Install & use

See [INSTALL.md](INSTALL.md) for the exact commands per tool. The short version:

1. Install the pack with one command (or one paste) in the tool you use most.
2. Say: **"set up my coding environment"**
3. Pick components from the menu. The pack writes only what you choose.

Because the pack is just an agent writing files, once it's loaded in one tool it
can populate another tool's directories too — install once, then say "also set
up my Cursor environment" and it cascades.

## Repo layout

```
ai-starter-pack/
├── README.md                      # this file
├── INSTALL.md                     # how to install in each tool
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
            ├── payloads/          # the installable content (original, MIT)
            ├── optional/          # rtk opt-in install flow
            └── vendor/            # optional canonical-upstream vendoring
```

## Safe to re-run

Every component is marked, so re-running never duplicates anything. If you
already installed one of these — or have your own guardrails in your context
file — the pack detects it and asks rather than writing a second copy. See
`skills/ai-starter-pack/references/dedup.md`.

## Provenance & licensing

Default payloads are original MIT content (`skills/ai-starter-pack/LICENSES/`,
`skills/ai-starter-pack/NOTICE.md`). They express well-known, freely-usable ideas
in their own words, so the default install carries no third-party obligation. If
you want the canonical upstream files (forrestchang's Karpathy guidelines,
JuliusBrussee's caveman) instead, `skills/ai-starter-pack/references/vendor/VENDORING.md`
installs them at a pinned commit with correct attribution. `rtk` is fetched from
[its upstream](https://github.com/rtk-ai/rtk), never redistributed here.

This is a personal-tooling convenience, not legal advice; if you publish it,
glance at each upstream's real LICENSE first.

## Components, credits & thanks

Everything this pack can install for you, what it does, and who to thank for the
idea or the tool behind it. The default payloads ship in original wording, but
the *ideas* — and the optional canonical files and binary — come from the people
below. Go star their work.

### Tools the pack installs into

It writes config and skills for these coding agents. Thanks to the teams building
each one and keeping their config formats documented:

- **[Claude Code](https://github.com/anthropics/claude-code)** (Anthropic) — plugin marketplace + skills dir.
- **[Codex](https://github.com/openai/codex)** (OpenAI) — `AGENTS.md` + skills dir.
- **[Cursor](https://www.cursor.com)** — `.cursor/rules/*.mdc`.
- **[Windsurf / Devin](https://docs.devin.ai/desktop/cascade/memories)** — `.devin/rules/`, legacy `.windsurf/rules/`, and `AGENTS.md`.
- **[GitHub Copilot](https://github.com/features/copilot)** — `.github/copilot-instructions.md`.
- **[Aider](https://github.com/Aider-AI/aider)** — `--read` / `AGENTS.md`.
- **Antigravity** and any other `AGENTS.md` / `SKILL.md` agent — generic path.

### Skills & components the pack installs

| Component | What it installs | Credit |
|---|---|---|
| `rails` | Always-on guardrails in your context file | Ideas popularized by **[Andrej Karpathy](https://github.com/karpathy)**; canonical skill by **[Forrest Chang](https://github.com/forrestchang)** — [`andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills) (MIT) |
| `caveman` | On-demand terse-output skill | **[Julius Brussee](https://github.com/JuliusBrussee)** — [`caveman`](https://github.com/JuliusBrussee/caveman) (MIT) |
| `design` | On-demand UI-quality skill | Original to this pack (MIT) |
| `command-hygiene` | On-demand low-noise-shell skill | Original to this pack (MIT); a pure-skill stand-in for rtk |
| `stop-slop` | On-demand prose-cleanup skill (fetched as-is) | **[Hardik Pandya](https://hvpandya.com)** — [`hardikpandya/stop-slop`](https://github.com/hardikpandya/stop-slop) (MIT) |
| `matt-pocock` | Engineering skill set (fetched as-is) | **[Matt Pocock](https://github.com/mattpocock)** — [`mattpocock/skills`](https://github.com/mattpocock/skills) (MIT) |
| `rtk` | Opt-in shell-output compression binary | **[rtk-ai](https://github.com/rtk-ai/rtk)** — RTK "Rust Token Killer" (Apache-2.0); fetched from upstream, never bundled |

Thank you to **Andrej Karpathy**, **Forrest Chang (forrestchang)**, **Julius
Brussee (JuliusBrussee)**, **Hardik Pandya (hardikpandya)**, **Matt Pocock
(mattpocock)**, the **rtk-ai** team, and the maintainers of every agent above.
This pack is glue around your work — all credit for the underlying ideas and
tools is yours. If you maintain one of these and want the attribution worded
differently, open an issue.
