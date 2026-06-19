# rtk (optional binary — opt-in only)

`rtk` ("Rust Token Killer") is a CLI proxy that rewrites verbose shell commands
into compact output *before the model sees it*. Unlike the other components it is
a compiled binary, not a skill — a skill can't intercept its own tool output
after the fact. So this is real infrastructure: it must be downloaded, placed on
PATH, and registered as a host hook.

Install it only when the user explicitly asks. It is **not** bundled with this
pack; it is fetched from upstream at install time, so the user runs the same
code they'd get installing it themselves. Narrate every command you run — the
user should watch the install happen, not trust an opaque one-liner.

## Preconditions

- Confirm the user wants rtk (it modifies PATH and the host's hook config).
- If an older AI Starter Pack install has `asp-command-hygiene`, note that rtk
  supersedes it and offer to remove that legacy skill after rtk is verified
  working.

## Step 1 — find a fetch primitive (detect and degrade)

Do not assume `curl` exists. Probe in order, use the first available:

1. `curl --version`  → use curl.
2. `wget --version`  → use wget.
3. The agent's own web-fetch / download tool, if the host exposes one.
4. None available → stop. Tell the user the two manual options:
   the official one-line installer from the rtk repo, or downloading the release
   binary for their OS/arch by hand. Do not fake the install.

## Step 2 — install the binary

Prefer the project's official installer (it handles OS/arch detection, PATH, and
chmod in one step); fall back to a release-binary download if a fetch primitive
is present but you're avoiding piped execution. Show the user the exact command
first. After install, verify:

```
rtk --version
```

If this fails, the most common cause is a name collision: there is an unrelated
`rtk` (a Rust type toolkit) on crates.io. If the wrong one landed, reinstall from
the rtk-ai project's git source specifically, then re-verify.

## Step 3 — register the host hook

rtk rewrites Bash commands via the host's pre-tool hook. Use the host detected in
the main install (step 1 of `SKILL.md`):

| Host | Init command |
|---|---|
| Claude Code | `rtk init -g` |
| Codex | `rtk init -g --codex` |
| Antigravity | `rtk init --agent antigravity` |
| Other | check `rtk init --help` for the agent flag |

Use the global (`-g`) form for a global scope, the plain form for project scope,
matching the user's chosen `SCOPE`.

## Step 4 — restart and verify

The hook loads when the host restarts. Tell the user to restart their tool, then
confirm a command gets rewritten (e.g. `git status` becomes the compact form).
Report success, or the exact error if it didn't take.

## Caveats to relay

- rtk only compresses **Bash tool** output. Host-native read/grep/glob tools
  bypass it.
- It compresses output tokens, not the model's reasoning.
- It's a fast-moving community binary — worth re-checking the hook still works
  after the host updates its tool API.
