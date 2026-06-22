# NOTICE

AI Starter Pack's own installer glue and documentation are MIT licensed. See the
repo root `LICENSE` and `LICENSES/ai-starter-pack-MIT.txt`.

This repo does not bundle third-party installable skills, tools, binaries,
plugins, hooks, project indexes, or rewritten summaries. It points agents to the
upstream projects listed in `README.md` and `references/vendor/sources.json`, and
the installer follows each upstream README/docs at install time.

When an installation copies upstream files into a user's tool or project, that
installed copy must preserve the upstream license/notice files and attribution
required by that upstream project. Install-time provenance belongs in the
installed target's ASP metadata or adjacent license file, not in this repo's
static notice.
