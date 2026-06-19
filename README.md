# AI Starter Pack

A one-step setup for a coding agent's everyday defaults. Works across Claude
Code, Codex, Antigravity, and any agent that reads `SKILL.md` / `AGENTS.md`.

The pack is **self-installing**: the agent reading it uses its own file tools to
place the right files where your host expects them. No npm, curl, or toolchain
needed for the default install — the only capability required is "an agent that
can write a file." You install *the pack* once; the pack installs the components
for you, conversationally. There is no per-component manual step.

## What's in it

| Component | Type | Default | What it does |
|---|---|---|---|
| `rails` | always-on | ✅ | Guardrails: surface assumptions, stay minimal, surgical edits, verify success |
| `caveman` | on-demand | optional | Terse output — fewer tokens, same accuracy |
| `design` | on-demand | optional | Intentional, non-templated UI work |
| `command-hygiene` | on-demand | optional | Quiet, low-noise shell commands (pure-skill rtk stand-in) |
| `rtk` | binary | opt-in | Real deterministic shell-output compression (fetched, not bundled) |

`rails` install into your always-loaded context file (`CLAUDE.md` / `AGENTS.md`)
so they apply every session. The on-demand skills load only when their topic
comes up. `rtk` is infrastructure and only installs if you ask.

## Install & use

See [INSTALL.md](INSTALL.md) for the exact commands. The short version:

1. Install the pack with one command (or one paste) in the tool you use most.
2. Say: **"set up my coding environment"**
3. Pick components from the menu. The pack writes only what you choose.

Because the pack is just an agent writing files, once it's loaded in one tool it
can populate another tool's directories too — install once, then say "also set
up my Codex environment" and it cascades.

## Repo layout

```
ai-starter-pack/
├── README.md                      # this file
├── INSTALL.md                     # how to install in each tool
├── LICENSE                        # MIT (this pack's original content)
├── .claude-plugin/                # Claude Code plugin marketplace manifests
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

## Provenance

Default payloads are original MIT content (`skills/ai-starter-pack/LICENSES/`,
`skills/ai-starter-pack/NOTICE.md`). They express well-known, freely-usable ideas
in their own words, so the default install carries no third-party obligation. If
you want the canonical upstream files (forrestchang's Karpathy guidelines,
JuliusBrussee's caveman) instead, `references/vendor/VENDORING.md` installs them
at a pinned commit with correct attribution.

This is a personal-tooling convenience, not legal advice; if you publish it,
glance at each upstream's real LICENSE first.
