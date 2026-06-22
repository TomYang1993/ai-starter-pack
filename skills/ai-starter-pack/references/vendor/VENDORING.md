# Installing upstream-original components

Collected third-party components must be installed from their upstream originals,
not from ASP-authored summaries. Use this procedure for every entry in
`sources.json`.

`sources.json` is an identity registry and file-location hint. It is not the
source of truth for install commands. The upstream README/docs are the source of
truth at install and update time.

Licenses vary by upstream. Read the actual LICENSE/NOTICE files before copying
anything. Keep the required notices with the installed files; skipping
attribution is what turns permitted reuse into a violation.

## Procedure

For each entry in `sources.json` the user wants:

1. **Fetch the upstream README first.** Read the current README/docs from the
   repo URL in `sources.json`. Follow upstream's current install instructions
   when they exist.
2. **Use local hints only after reading upstream.** The `file`, `extra_files`,
   and `commit` fields in `sources.json` are last-reviewed hints for locating
   payload files. They are not a reason to ignore newer upstream README
   instructions.
3. **Fetch the smallest payload.** If upstream requires copying files, fetch only
   the listed skill file/folder(s) and required references, plus LICENSE/NOTICE.
   Do not clone the whole repo unless the README makes that unavoidable.
4. **Read the actual LICENSE/NOTICE** from upstream. Confirm the license still
   matches `sources.json`; if it changed, stop and ask before installing.
5. **Copy upstream content as-is.** Keep the upstream's content, not the pack's.
   Add the pack's source-marker or ASP metadata near the copied content so dedup
   still works.
6. **Copy the notice.** Write the upstream license text and any required notice
   text to `LICENSES/<component>-upstream-LICENSE.txt`. Keep their copyright
   lines intact — do not replace them with yours.
7. **Record provenance in the installed target**, not this repo's static
   `NOTICE.md`: component, repo, source URL or resolved commit SHA if available,
   retrieval date, and adjacent license file.

## Refreshing later

To update an upstream component: fetch the upstream README again, resolve the
current install/payload path, diff against the installed copy, show the user the
diff, and replace only on approval. Never auto-update user-edited content.
