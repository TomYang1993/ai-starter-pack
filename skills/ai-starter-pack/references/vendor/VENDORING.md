# Installing upstream-original components

Collected third-party components must be installed from their upstream originals,
not from ASP-authored summaries. Use this procedure for every entry in
`sources.json`.

`sources.json` is an identity registry and file-location hint. It is not the
source of truth for install commands. The upstream README/docs are the source of
truth at install and update time.

Local repository checkouts are caches only. Use them to identify remotes or
inspect existing user state, but do not treat their files as current upstream
authority. Do not `git pull`, overwrite, or delete a local checkout unless the
user explicitly asks for that repository maintenance.

Licenses vary by upstream. Read the actual LICENSE/NOTICE files before copying
anything. Keep the required notices with the installed files; skipping
attribution is what turns permitted reuse into a violation.

## Procedure

For each entry in `sources.json` the user wants:

1. **Fetch the upstream README first.** Read the current README/docs from the
   repo URL in `sources.json`. Follow upstream's current install instructions
   when they exist.
2. **Treat local checkouts as stale until proven fresh.** If a local clone of
   the upstream repo exists, inspect its remote only as a hint. Before using any
   file from it, perform a non-destructive freshness check such as `git fetch`
   plus comparing local `HEAD` with the upstream default branch. If the checkout
   is stale, unverifiable, dirty, or on an unexpected remote, ignore it and fetch
   current upstream docs/payload directly.
3. **Use upstream installers with the chosen scope.** If upstream recommends the
   `skills` CLI (`npx skills add ...`), prefer that command over manual copying
   and let the CLI choose agent-specific paths. For pure skills,
   agent-side/defaults setup means installing into the active agent's own skill
   area by default: pass `-g/--global` or choose Global if that is the upstream
   flag/prompt for agent-side placement. For project-level setup, omit
   `-g/--global` and choose Project if the CLI asks. Add `-a <agent>` only when
   the active host is clear and the flag is needed to avoid an agent-selection
   prompt. Do not apply this pure-skill agent-side default to optional tools
   such as `rtk`, CodeGraph, or Ponytail; follow their adapters instead.
4. **Use local hints only after reading upstream.** The `file`, `extra_files`,
   and `commit` fields in `sources.json` are last-reviewed hints for locating
   payload files. They are not a reason to ignore newer upstream README
   instructions.
5. **Fetch the smallest payload.** If upstream requires copying files, fetch only
   the listed skill file/folder(s) and required references, plus LICENSE/NOTICE.
   Do not clone the whole repo unless the README makes that unavoidable.
6. **Read the actual LICENSE/NOTICE** from upstream. Confirm the license still
   matches `sources.json`; if it changed, stop and ask before installing.
7. **Copy upstream content as-is.** Keep the upstream's content, not the pack's.
   Add the pack's source-marker or ASP metadata near the copied content so dedup
   still works.
8. **Copy the notice.** Write the upstream license text and any required notice
   text to `LICENSES/<component>-upstream-LICENSE.txt`. Keep their copyright
   lines intact — do not replace them with yours.
9. **Record provenance in the installed target**, not this repo's static
   `NOTICE.md`: component, repo, source URL or resolved commit SHA if available,
   retrieval date, and adjacent license file.

## Refreshing later

To update an upstream component: fetch the upstream README again, resolve the
current install/payload path, diff against the installed copy, show the user the
diff, and replace only on approval. If a local upstream checkout is stale, report
it as stale and ignore it; do not pull or delete it unless the user asks. Never
auto-update user-edited content.
