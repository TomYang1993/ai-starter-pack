# AI Starter Pack

A one-step setup for a coding agent's essential setup. Works with almost any agentic tools out there.

The pack is **self-installing**: the agent reading it uses its own file tools to
place the right files where your host expects them. The installer itself is just
files, but selected third-party components are fetched from their upstream repos
at a pinned commit so the original authors' work stays intact.

## Install

Install **the pack** once per tool. The pack then installs individual components
(`andrej-karpathy-skills`, `caveman`, `impeccable`, etc.) for you.

Just `type` or `say` the following in your selected tool:

> "Read `skills/ai-starter-pack/SKILL.md` from this repo and set up my coding environment."

If initiating outside this repo, replace the relative path with the actual path, or just trust your agent to find this folder.

Then follow the agent's flow for necessary permissions and feedback.

## Updates

After you pull a newer AI Starter Pack, just `type` or `say`:

> "update ai-starter-pack"

The agent should load the pack if needed, check what AI Starter Pack manages,
update the unchanged parts, and ask before touching anything you edited yourself.
No separate enable step is required once the pack is installed in that tool.
If the agent cannot find the pack, use the explicit path form:

> "Read `skills/ai-starter-pack/SKILL.md` from this repo and update ai-starter-pack."

For manual install paths, optional components, and the full update rules, see
[`INSTALL.md`](INSTALL.md) and `skills/ai-starter-pack/references/update.md`.

## Credits & Thanks

| Component | Adds | Credit | GitHub stars |
|---|---|---|---:|
| `andrej-karpathy-skills` | Practical coding-agent guardrails: think first, keep changes small, verify the work. | **[Forrest Chang](https://github.com/forrestchang)** — [`andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills) (MIT), based on guidance from **[Andrej Karpathy](https://github.com/karpathy)** | 179k |
| `caveman` | A terse mode for shorter replies and fewer wasted tokens. | **[Julius Brussee](https://github.com/JuliusBrussee)** — [`caveman`](https://github.com/JuliusBrussee/caveman) (MIT) | 74.8k |
| `impeccable` | A frontend/UI design helper for critique, polish, and better product taste. | **[Paul Bakaus](https://github.com/pbakaus)** — [`impeccable`](https://github.com/pbakaus/impeccable) (Apache-2.0) | 39.6k |
| `stop-slop` | A writing cleanup skill that removes obvious AI tells from prose. | **[Hardik Pandya](https://hvpandya.com)** — [`stop-slop`](https://github.com/hardikpandya/stop-slop) (MIT) | 11.5k |
| `matt-pocock` | A practical engineering skill set: TDD, debugging, planning, architecture, and more. | **[Matt Pocock](https://github.com/mattpocock)** — [`skills`](https://github.com/mattpocock/skills) (MIT) | 137k |
| `rtk` | An optional binary that compresses shell output before it reaches the model. | **[rtk-ai](https://github.com/rtk-ai/rtk)** — RTK "Rust Token Killer" (Apache-2.0); fetched from upstream, never bundled | 64k |

Stars are rounded snapshots from GitHub, checked 2026-06-20.

This repo is glue around you guys' work, all credit is yours.
If you maintain one of these and want the attribution worded
differently, open an issue.
