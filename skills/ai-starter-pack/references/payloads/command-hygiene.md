---
name: command-hygiene
description: Issue shell commands that return only the information needed, to avoid flooding the context with noisy output during coding sessions. Use whenever running git, tests, builds, package managers, logs, or file inspection in a terminal — quiet flags and targeted queries cut token usage on every command. A lightweight, pure-skill stand-in for the rtk binary.
---
# source: ai-starter-pack command-hygiene v1

# Command hygiene

Routine shell commands dump far more than the model needs — full git status,
every passing test, entire log files. The agent reads (and pays for) all of it.
This skill is a behavioral substitute for a true output-compressing proxy: it
can't intercept output the way a binary does, but it can stop generating noise at
the source by choosing quieter commands.

This is best-effort, not deterministic. For guaranteed compression across every
command, the `rtk` binary is the real tool — see the pack's `references/optional/rtk.md`.

## Prefer the quiet form

- **git**: `git status -s`, `git log --oneline -n 20`, `git diff --stat` before a
  full diff. Add `-q` to commits/checkouts where you don't need the chatter.
- **tests**: run only what's relevant (a path, a filter, a single file) rather
  than the whole suite. Use the runner's quiet/summary reporter, and on failure
  read the failing case — not the hundreds of passing lines.
- **builds / installers**: prefer `--quiet` / `--silent`. Pipe verbose tools
  through a filter (`| tail -n 30`, `grep -E 'error|warn'`) instead of reading
  everything.
- **logs**: `tail -n 50`, time/level filters, or grep for the symptom. Never
  `cat` a large log to scan it.
- **file inspection**: read the specific range or symbol you need, not the whole
  file, when the tool allows.

## Keep correctness

Quiet must not hide signal. When a command fails or behaves unexpectedly, widen
the output deliberately to diagnose — get the full error, then narrow again.
Brevity is the default, not a rule that suppresses the thing you actually need
to see.
