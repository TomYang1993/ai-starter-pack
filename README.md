# AI Starter Pack

A one-step setup for coding-agent tools like `caveman`, `codegraph`, and more.
Works with almost any agentic tool.

## Install

Clone the repo.

When you already have this repo open, trust the repo, then type or say in your desired AI tool:

> "Read `skills/ai-starter-pack/SKILL.md` from this repo and set up my coding environment."

If initiating outside this repo, replace the relative path with the actual path, or just trust your agent to find this folder.

Then follow the agent's flow for necessary permissions and feedback.

Install **the pack** once per tool. The pack then installs individual components
(`caveman`, optional CodeGraph, etc.) for you.

You may be used to other install methods for optimized tool usage and easier flow. See
[`INSTALL.md`](INSTALL.md) for host-specific install paths.

## Update

When you are in this repo, pull the latest, and just `type` or `say` in your desired AI tool:

> "Read `skills/ai-starter-pack/SKILL.md` from this repo and update ai-starter-pack."

The agent should load the pack if needed, check what AI Starter Pack manages,
update the unchanged parts, and ask before touching anything you edited yourself.

This is the most general way to update.

You may be used to other update methods.

## Supported Tools

[Claude Code](https://code.claude.com/docs/en/overview)

[Codex](https://developers.openai.com/codex)

[Kilo Code](https://kilo.ai/)

[Cursor](https://cursor.com/)

[Devin Desktop / Windsurf](https://devin.ai/desktop)

[GitHub Copilot](https://github.com/features/copilot)

[Google Antigravity](https://antigravity.google/)

And more.

## Credits & Thanks

| Component | Adds | Credit | GitHub stars |
|---|---|---|---:|
| `caveman` | A terse mode for shorter replies and fewer wasted tokens. | **[Julius Brussee](https://github.com/JuliusBrussee)** — [`caveman`](https://github.com/JuliusBrussee/caveman) (MIT) | 74.8k |
| `stop-slop` | A writing cleanup skill that removes obvious AI tells from prose. | **[Hardik Pandya](https://hvpandya.com)** — [`stop-slop`](https://github.com/hardikpandya/stop-slop) (MIT) | 11.5k |
| `matt-pocock` | A practical engineering skill set: TDD, debugging, planning, architecture, and more. | **[Matt Pocock](https://github.com/mattpocock)** — [`skills`](https://github.com/mattpocock/skills) (MIT) | 137k |
| `rtk` | An optional binary that compresses shell output before it reaches the model. | **[rtk-ai](https://github.com/rtk-ai/rtk)** — RTK "Rust Token Killer" (Apache-2.0); fetched from upstream, never bundled | 64k |
| `codegraph` | An optional local CLI/MCP code knowledge graph for faster codebase exploration. | **[Colby McHenry](https://github.com/colbymchenry)** — [`codegraph`](https://github.com/colbymchenry/codegraph) (MIT); fetched from upstream, never bundled | 52.2k |

Stars are rounded snapshots from GitHub, checked 2026-06-20.

This repo is glue around you guys' work, all credit is yours.
If you maintain one of these and want the attribution worded
differently, open an issue.


## License

see [`LICENSE`](LICENSE). Third-party components keep their original licenses and
credits. The pack records notices under `skills/ai-starter-pack/NOTICE.md`.
