# Update policy

Use this file when the user asks to update AI Starter Pack, update installed
components, or reconcile a project after the starter-pack repo changed.

## Principle

Update by ownership, not by filename. The pack only changes files it owns and
only when the installed content still matches what the pack previously wrote.
User edits, user-updated upstream skills, and user-added skills are preserved by
default.

## Installed metadata

Every installed component should include a small metadata block.

For skill/rule folders, put the metadata immediately after frontmatter when the
format allows it:

```md
<!-- ai-starter-pack
component: caveman
managed: true
upstream_repo: https://github.com/JuliusBrussee/caveman
installed_commit: <commit>
content_sha256: <sha256-of-installed-upstream-content>
installed_at: <YYYY-MM-DD>
-->
```

For legacy installs that only have `# source: ai-starter-pack <component> ...`,
treat them as managed but with unknown hash. Show a diff and ask before
replacing.

## Source registry

Read `references/vendor/sources.json` for component identity, repo, file-path
hints, license expectations, and last-reviewed reference commits. Do not treat
that registry as the install authority. For installs and updates, fetch the
upstream README/docs for the selected component or tool first and follow the
current upstream instructions.

## Classify Each Installed Item

| State | How to recognize it | Default action |
|---|---|---|
| Managed + unchanged | ASP metadata exists and `content_sha256` matches current installed content | Update to the current upstream README-resolved content, after showing a concise summary |
| Managed + edited | ASP metadata exists but `content_sha256` does not match | Skip and ask: keep yours / replace / show diff |
| Managed legacy | ASP marker exists but no hash is recorded | Show diff and ask before replacing |
| Unmanaged duplicate | Same upstream skill appears without ASP metadata | Skip and ask before installing another copy |
| User-added unrelated | No ASP metadata and no component-name collision | Leave alone; mention only in list mode |
| Removed by user | ASP metadata missing where state says it was previously installed | Do not reinstall unless the user asks to add it |

## Update Flow

1. Detect host and scope using `references/dedup.md`.
2. Read `references/vendor/sources.json` for repo identity and hints.
3. Scan installed ASP markers and installed skill/rule folders.
4. Classify each installed component with the table above.
5. For each managed unchanged component:
   - Fetch the upstream README/docs for that component or tool from the remote
     upstream repo, not from a local checkout.
   - Resolve the current upstream install or payload path from upstream docs.
   - Compare installed metadata (`installed_commit`, source URL, or content hash)
     to the current upstream-resolved source when possible.
   - If equal, report already current.
   - If different, fetch the current payload files needed for the selected
     component, show a concise diff summary, then update the managed
     block/folder and metadata on approval.
6. For managed edited, managed legacy, and unmanaged duplicates:
   - Do not overwrite.
   - Report the finding and ask before replacing or merging.
7. For user-added unrelated skills:
   - Do nothing.
   - Do not remove, update, rename, or reformat them.
8. For removed components:
   - Respect the removal.
   - Reinstall only when the user explicitly asks to add that component.

## Component Notes

- `matt-pocock`: this is a skill set. Track each installed sub-skill separately
  when possible. If the user installed only some sub-skills, update only those.
- `rtk`: treat as a binary/tool install, not a skill. Check version/hook status
  first. Fetch upstream README only when install/update/repair is needed, and ask
  before changing PATH, hooks, or shell configuration.
- `codegraph`: treat as a CLI/MCP/project-index install, not a skill. Check
  `codegraph --version`, host MCP setup, and project `.codegraph/` status first.
  Fetch upstream README only when install/update/repair/indexing is needed, and
  ask before changing PATH, MCP config, agent permissions, or rebuilding indexes.
- `ponytail`: treat as an upstream plugin/ruleset install, not an ASP-authored
  skill. Check only the current host's Ponytail plugin, extension, hooks,
  commands, or instruction-rule copy first. Fetch upstream README only when
  install/update/repair is needed, and ask before reinstalling, trusting hooks,
  changing modes, or replacing rule files.

## Reporting

Use a compact report:

- Updated: component, old source/commit/hash, new source/commit/hash.
- Skipped as user-edited: component and path.
- Skipped as unmanaged duplicate: component and path.
- Already current: component.
- Needs confirmation: exact choice needed.

Never describe user-added unrelated skills as stale, broken, or managed by this
pack.
