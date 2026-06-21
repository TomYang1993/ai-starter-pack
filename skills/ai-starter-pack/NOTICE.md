# NOTICE

## This pack's own content

The installer glue and documentation are original work, licensed MIT
(`LICENSES/ai-starter-pack-MIT.txt`). The pack currently does not ship any
ASP-authored installable skills.

## Collected upstream originals

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
- `codegraph` — Colby McHenry, [`colbymchenry/codegraph`](https://github.com/colbymchenry/codegraph)
  (MIT). Optional local CLI/MCP code knowledge graph.

## Installed upstream files

When `references/vendor/VENDORING.md` installs upstream originals, record each
here:

| Component | Repo | Commit | Retrieved | License file |
|---|---|---|---|---|
| _(none vendored by default)_ | | | | |

`rtk` is never bundled or copied — it is fetched from upstream at install time,
so no rtk files are redistributed by this pack.

`codegraph` is never bundled or copied — it is fetched from upstream at install
time, so no CodeGraph files or project indexes are redistributed by this pack.
