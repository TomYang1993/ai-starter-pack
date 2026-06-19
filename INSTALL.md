# Installing the AI Starter Pack

You install **the pack** once per tool you care about (often just your main one).
The pack then installs the individual components for you — you don't install
rails / caveman / design one by one.

Replace `YOUR_GH` below with your GitHub namespace after you push this repo
(e.g. `tom/ai-starter-pack`).

## Step 0 — publish the repo

Push this folder to a public GitHub repo named `ai-starter-pack`. Nothing to
rearrange — the layout is already install-ready.

## Step 1 — install the pack (pick the channel for your tool)

### A. Skills CLI — cross-tool, no per-tool config

```bash
npx skills add YOUR_GH/ai-starter-pack --skill ai-starter-pack --agent claude-code
npx skills add YOUR_GH/ai-starter-pack --skill ai-starter-pack --agent codex
npx skills add YOUR_GH/ai-starter-pack --skill ai-starter-pack --agent antigravity
```

This copies the whole `skills/ai-starter-pack/` folder (SKILL.md + references)
into the tool's skills directory.

### B. Claude Code plugin marketplace — Claude Code only

```text
/plugin marketplace add YOUR_GH/ai-starter-pack
/plugin install ai-starter-pack@ai-starter-pack
```

The manifests in `.claude-plugin/` drive this. Plugin specs change fast — if the
install command errors, check the current Claude Code plugin docs and adjust
`.claude-plugin/marketplace.json` / `plugin.json` to match. Channels A and C
don't depend on the plugin spec.

### C. No toolchain — manual copy

Copy `skills/ai-starter-pack/` into your tool's skills folder:

```bash
# Claude Code (global)
cp -r skills/ai-starter-pack ~/.claude/skills/ai-starter-pack
# Codex (global)
cp -r skills/ai-starter-pack ~/.codex/skills/ai-starter-pack
# Antigravity / generic (global)
cp -r skills/ai-starter-pack ~/.agents/skills/ai-starter-pack
```

Project-local installs work too — use the project's `.claude/skills/`,
`.codex/skills/`, or `.agents/skills/` instead.

## Step 2 — use it

In any tool where the pack is loaded, say:

> set up my coding environment

The pack detects your host, shows the component menu, runs the dedup checks, and
writes only what you pick. Other phrases that trigger it: "bootstrap my agent",
"install my starter pack", "configure this project".

## Step 3 — manage it later

- **list** — "what's in my starter pack here?"
- **add one** — "add caveman to this project"
- **update** — "update my starter pack" (diffs before replacing)
- **remove** — "remove the design skill"
- **rtk** — "install rtk" (opt-in; fetches the binary, patches your host hook)

## Self-propagation

Once any agent has the pack loaded, it can set up *other* tools by writing into
their directories. Install once in your main tool, then:

> also set up my Codex environment

and it populates `~/.codex/...`, pack included — no second manual install.

## Notes worth checking before relying on it

- The skills-dir paths per host (`references/dedup.md`) use common conventions;
  verify against your actual Codex / Antigravity installs, as those move.
- `rtk init` flags (`references/optional/rtk.md`) should be checked against rtk's
  current README — it's a fast-moving binary.
