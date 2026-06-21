# NOTICE

## This pack's own content

The installer glue and documentation are original work, licensed MIT
(`LICENSES/ai-starter-pack-MIT.txt`). The pack currently does not ship any
ASP-authored installable skills.

## Collected upstream skill originals

The pack does not ship rewritten summaries of well-known community skills. When
chosen, these components are fetched from upstream at a pinned commit and
installed verbatim with their license/notice files (see
`references/vendor/VENDORING.md` and `references/vendor/sources.json`).

- `caveman` — Julius Brussee, [`JuliusBrussee/caveman`](https://github.com/JuliusBrussee/caveman)
  (MIT). Terse-output skill.
- `stop-slop` — Hardik Pandya, [`hardikpandya/stop-slop`](https://github.com/hardikpandya/stop-slop)
  (MIT, Copyright (c) 2025 Hardik Pandya). Removes AI writing tells from prose.
- `matt-pocock` — Matt Pocock, [`mattpocock/skills`](https://github.com/mattpocock/skills)
  (MIT, Copyright (c) 2026 Matt Pocock). Collection of production engineering skills.

## Optional upstream tools

These components are not bundled in this repo. When chosen, the pack follows the
upstream install path for the current host and scope.

- `rtk` — rtk-ai, [`rtk-ai/rtk`](https://github.com/rtk-ai/rtk)
  (Apache-2.0). Optional shell-output compression binary and per-host hook setup.
- `codegraph` — Colby McHenry, [`colbymchenry/codegraph`](https://github.com/colbymchenry/codegraph)
  (MIT). Optional local CLI/MCP code knowledge graph.
- `ponytail` — Dietrich Gebert, [`DietrichGebert/ponytail`](https://github.com/DietrichGebert/ponytail)
  (MIT). Optional upstream plugin/ruleset for reducing over-building.

## Installed upstream files

When `references/vendor/VENDORING.md` installs upstream originals, record each
here:

| Component | Repo | Commit | Retrieved | License file |
|---|---|---|---|---|
| _(none vendored by default)_ | | | | |

`rtk`, `codegraph`, and `ponytail` are never bundled by this pack, so their
files, binaries, hooks, and project indexes are not redistributed here.
