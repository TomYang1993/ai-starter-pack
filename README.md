# AI Starter Pack

A one-step setup for a coding agent's everyday defaults. Works best in agents
with first-class `SKILL.md` support (Claude Code and Codex) and also bootstraps
rule/instruction-based tools such as Cursor, Windsurf/Devin, GitHub Copilot,
Aider, Antigravity, Kilo Code, and other `AGENTS.md` readers.

The pack is **self-installing**: the agent reading it uses its own file tools to
place the right files where your host expects them. The installer itself is just
files, but selected third-party components are fetched from their upstream repos
at a pinned commit so the original authors' work stays intact. You install *the
pack* once; the pack installs the components for you, conversationally.

## Install

Install **the pack** once per tool. The pack then installs individual components
(`andrej-karpathy-skills`, `caveman`, `impeccable`, etc.) for you, so there are
no per-component manual steps.

> "Read `skills/ai-starter-pack/SKILL.md` from this repo and set up my coding environment."

The agent detects your host, shows the component menu, runs the safety checks,
and writes the selected files. For manual install commands, host-specific setup,
and agent-readable fallbacks, see [`INSTALL.md`](INSTALL.md).

After installing, the only prompt you need is:

> "set up my coding environment"

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

The component registry lives in
`skills/ai-starter-pack/references/vendor/sources.json`. It records each
upstream repo, license, install path, and reviewed commit used for installs.

## Repo layout

```
ai-starter-pack/
├── README.md                      # overview, quick start, updates
├── INSTALL.md                     # manual and host-specific install paths
├── AGENTS.md                      # root bootstrap for Codex / Kilo Code / Aider / generic
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
            ├── update.md          # managed/user-edited update policy
            ├── optional/          # rtk opt-in install flow
            └── vendor/            # upstream-original source registry
```

## Updates

After pulling a newer AI Starter Pack, say:

> "update my environment"

The pack updates only AI Starter Pack-managed components that still match what it
previously installed. If you edited a managed skill, updated an upstream skill
yourself, added your own skills, or removed a component, the pack leaves that
work alone unless you explicitly approve replacement or reinstall.

For manual install paths, optional components, and the full update rules, see
[`INSTALL.md`](INSTALL.md) and `skills/ai-starter-pack/references/update.md`.

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
