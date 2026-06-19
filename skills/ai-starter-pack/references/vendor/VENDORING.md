# Vendoring the canonical upstream files (optional)

The default install uses this pack's own MIT payloads in `references/payloads/`. They cover
the same ground with no third-party obligation. Use this path only if the user
specifically wants the original, widely-used upstream files — forrestchang's
Karpathy guidelines or JuliusBrussee's caveman.

Both upstreams are MIT, which permits copying and redistribution **on one
condition: keep their license notice with the copied file**. Do this carefully —
skipping attribution is what turns a permitted copy into a violation.

## Procedure

For each entry in `sources.json` the user wants:

1. **Pick and pin a commit.** Fetch the repo, choose a specific reviewed commit
   SHA, and record it in the `commit` field (replace `PIN_ME`). Never track a
   moving branch like `main` for content that lands in an always-loaded context
   file — a compromised upstream would inject into every session.
2. **Read the actual LICENSE** in the repo at that commit. Confirm it is MIT and
   capture the copyright line (e.g. `Copyright (c) <year> <author>`). Trust the
   repo's own LICENSE file, not secondhand reports.
3. **Copy the content file** (`CLAUDE.md` or `SKILL.md`) to the matching install
   target, exactly as the default flow would — but keep the upstream's content,
   not the pack's. Add the pack's source-marker / context-file markers so dedup
   still works.
4. **Copy the notice.** Write the upstream's MIT text and original copyright line
   to `LICENSES/<component>-upstream-MIT.txt`. Keep their copyright line intact —
   do not replace it with yours.
5. **Record provenance** in `NOTICE.md`: component, repo, commit SHA, retrieval
   date.

## Watch for forks

There are several near-identical Karpathy repos (forrestchang is the original;
others are forks that may differ or re-license). Vendor from the repo named in
`sources.json` and pin its commit, so you don't accidentally copy a fork.

## Refreshing later

To update a vendored file: re-fetch at a new commit, diff against the installed
copy, show the user the diff, and replace only on approval. Never auto-update.
