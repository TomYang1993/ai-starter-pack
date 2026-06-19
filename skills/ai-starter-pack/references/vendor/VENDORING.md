# Installing upstream-original components

Collected third-party components must be installed from their upstream originals,
not from ASP-authored summaries. Use this procedure for every entry in
`sources.json`.

Licenses vary by upstream. Read the actual LICENSE/NOTICE files at the pinned
commit before copying anything. Keep the required notices with the installed
files; skipping attribution is what turns permitted reuse into a violation.

## Procedure

For each entry in `sources.json` the user wants:

1. **Pick and pin a commit.** Fetch the repo, choose a specific reviewed commit
   SHA, and record it in the install report. Entries with
   `"commit": "PIN_AT_INSTALL"` intentionally require this install-time
   resolution. Never track a moving branch like `main` for content that lands in
   an always-loaded context file — a compromised upstream would inject into every
   session.
2. **Read the actual LICENSE/NOTICE** in the repo at that commit. Confirm the
   license matches `sources.json`; update `sources.json` if upstream changed.
   Trust the repo's own files, not secondhand reports.
3. **Copy the listed upstream files** to the matching install target, exactly as
   the default flow would — but keep the upstream's content, not the pack's.
   Add the pack's source-marker / context-file markers around or near the copied
   content so dedup still works.
4. **Copy the notice.** Write the upstream license text and any required notice
   text to `LICENSES/<component>-upstream-LICENSE.txt`. Keep their copyright
   lines intact — do not replace them with yours.
5. **Record provenance** in `NOTICE.md`: component, repo, commit SHA, retrieval
   date.

## Watch for forks

There are several near-identical Karpathy repos (forrestchang is the original;
others are forks that may differ or re-license). Vendor from the repo named in
`sources.json` and pin its commit, so you don't accidentally copy a fork.

## Refreshing later

To update an upstream component: re-fetch at a new commit, diff against the
installed copy, show the user the diff, and replace only on approval. Never
auto-update.
