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

## Install

Install the pack once in the tool you use most, then say
**"set up my coding environment"** and pick components from the menu.

**Claude Code** (recommended path):

```text
/plugin marketplace add TomYang1993/ai-starter-pack
/plugin install ai-starter-pack@ai-starter-pack
```

**Every other tool** — copy the skill into the place that tool loads from:

| Tool | One-step install |
|---|---|
| **Codex / Antigravity** | `cp -r skills/ai-starter-pack ~/.agents/skills/` — reads root `AGENTS.md` |
| **Cursor** | copy `.cursor/rules/ai-starter-pack.mdc` + `skills/ai-starter-pack/` into the project |
| **Windsurf / Devin** | add a `.devin/rules/` bootstrap + copy `skills/ai-starter-pack/` |
| **GitHub Copilot** | bootstrap in `.github/copilot-instructions.md` + copy `skills/ai-starter-pack/` |
| **Aider** | `aider --read skills/ai-starter-pack/SKILL.md` |
| **Any other agent** | copy `skills/ai-starter-pack/`, point the agent at `SKILL.md` |

Then, in that tool:

> "set up my coding environment"

The pack detects your host, shows the component menu, runs dedup checks, and
writes only what you pick. Full per-tool commands (global vs project scope,
manual copies, plugin manifests) live in **[INSTALL.md](INSTALL.md)**.

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

## Credits & Thanks

| Component | What it installs | Credit |
|---|---|---|
| `rails` | Always-on guardrails in your context file | Ideas popularized by **[Andrej Karpathy](https://github.com/karpathy)**; canonical skill by **[Forrest Chang](https://github.com/forrestchang)** — [`andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills) (MIT) |
| `caveman` | On-demand terse-output skill | **[Julius Brussee](https://github.com/JuliusBrussee)** — [`caveman`](https://github.com/JuliusBrussee/caveman) (MIT) |
| `design` | On-demand UI-quality skill | Original to this pack (MIT) |
| `command-hygiene` | On-demand low-noise-shell skill | Original to this pack (MIT); a pure-skill stand-in for rtk |
| `stop-slop` | On-demand prose-cleanup skill (fetched as-is) | **[Hardik Pandya](https://hvpandya.com)** — [`hardikpandya/stop-slop`](https://github.com/hardikpandya/stop-slop) (MIT) |
| `matt-pocock` | Engineering skill set (fetched as-is) | **[Matt Pocock](https://github.com/mattpocock)** — [`mattpocock/skills`](https://github.com/mattpocock/skills) (MIT) |
| `rtk` | Opt-in shell-output compression binary | **[rtk-ai](https://github.com/rtk-ai/rtk)** — RTK "Rust Token Killer" (Apache-2.0); fetched from upstream, never bundled |

This pack is glue around your work, all credit is yours.
If you maintain one of these and want the attribution worded
differently, open an issue.
