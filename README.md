# AI Starter Pack

A one-step setup for your AI coding environment, including `caveman`, `ponytail`, `codegraph`, and more.
Works with almost any agentic tool.

## Install

No clone needed. Type or say this in your desired AI tool:

> "Read https://github.com/TomYang1993/ai-starter-pack and set up my coding environment. Start from `skills/ai-starter-pack/SKILL.md`."

Then follow the agent's flow for necessary permissions and feedback.

For persistent installs, marketplace/plugin installs, or local auditing, see
[`INSTALL.md`](INSTALL.md).

## Update

Type or say this in your desired AI tool:

> "Read https://github.com/TomYang1993/ai-starter-pack and update my coding environment. Start from `skills/ai-starter-pack/SKILL.md`."

The agent should load the pack if needed, check what AI Starter Pack manages, update the unchanged parts, and ask before touching anything you edited yourself.

## Supported Tools

These are the agent/tool combinations we have tested so far. Other tools may
work through the same skill standards, but they are not listed here until tested.

- [Claude Code](https://code.claude.com/docs/en/overview) — tested with Opus 4.8 xhigh.
- [Codex](https://developers.openai.com/codex) — tested with GPT 5.5 xhigh.
- OpenCode — tested with DeepSeek v4 flash.

## Credits & Thanks

| Component | Adds | Credit | GitHub stars |
|---|---|---|---:|
| `caveman` | A terse mode for shorter replies and fewer wasted tokens. | **[Julius Brussee](https://github.com/JuliusBrussee)** — [`caveman`](https://github.com/JuliusBrussee/caveman) (MIT) | 75.4k |
| `stop-slop` | A writing cleanup skill that removes obvious AI tells from prose. | **[Hardik Pandya](https://hvpandya.com)** — [`stop-slop`](https://github.com/hardikpandya/stop-slop) (MIT) | 11.7k |
| `matt-pocock` | A practical engineering skill set: TDD, debugging, planning, architecture, and more. | **[Matt Pocock](https://github.com/mattpocock)** — [`skills`](https://github.com/mattpocock/skills) (MIT) | 139k |
| `rtk` | An optional binary that compresses shell output before it reaches the model. | **[rtk-ai](https://github.com/rtk-ai/rtk)** — RTK "Rust Token Killer" (Apache-2.0); fetched from upstream, never bundled | 64.4k |
| `codegraph` | An optional local CLI/MCP code knowledge graph for faster codebase exploration. | **[Colby McHenry](https://github.com/colbymchenry)** — [`codegraph`](https://github.com/colbymchenry/codegraph) (MIT); fetched from upstream, never bundled | 52.5k |
| `ponytail` | An optional plugin/ruleset that pushes agents toward the smallest sufficient implementation. | **[Dietrich Gebert](https://github.com/DietrichGebert)** — [`ponytail`](https://github.com/DietrichGebert/ponytail) (MIT); installed from upstream, never bundled | 45k |

Stars are rounded snapshots from GitHub, checked 2026-06-21.

This repo is glue around you guys' work, all credit is yours.
If you maintain one of these and want the attribution worded
differently, open an issue.


## License

see [`LICENSE`](LICENSE). Third-party components keep their original licenses and
credits. See `skills/ai-starter-pack/NOTICE.md` for the pack's notice policy.
