# NOTICE

## This pack's own content

The files in `references/payloads/` and the pack's documentation are original work,
licensed MIT (`LICENSES/ai-starter-pack-MIT.txt`). They express widely-known,
freely-usable engineering ideas in their own words and carry no third-party
obligation.

## Inspiration (not copied)

The default payloads were informed by ideas popularized in the community but do
not reproduce any third-party file:

- Behavioral-guardrail ideas popularized by Andrej Karpathy's January 2026 notes
  on LLM coding pitfalls, and Forrest Chang's `andrej-karpathy-skills` (MIT).
- Terse-output style popularized by JuliusBrussee's `caveman` (MIT).

## Fetched upstream skills (opt-in, copied as-is — not reworded)

These components have no bundled stand-in. When chosen, the pack fetches the
upstream skill at a pinned commit and installs it verbatim with its MIT notice
(see `references/vendor/VENDORING.md`). Record each under "Vendored upstream
files" below once installed.

- `stop-slop` — Hardik Pandya, [`hardikpandya/stop-slop`](https://github.com/hardikpandya/stop-slop)
  (MIT, Copyright (c) 2025 Hardik Pandya). Removes AI writing tells from prose.
- `matt-pocock` — Matt Pocock, [`mattpocock/skills`](https://github.com/mattpocock/skills)
  (MIT, Copyright (c) 2026 Matt Pocock). Collection of production engineering skills.

## Vendored upstream files (only if you ran the vendoring step)

If `references/vendor/VENDORING.md` was used to install canonical upstream files, record
each here:

| Component | Repo | Commit | Retrieved | License file |
|---|---|---|---|---|
| _(none vendored by default)_ | | | | |

`rtk` is never bundled or copied — it is fetched from upstream at install time,
so no rtk files are redistributed by this pack.
