# AI Starter Pack — Agent Bootstrap

This file is the entry point for agents that auto-read `AGENTS.md` (Codex, Windsurf, Aider, and others).

When the user says "set up my coding environment", "bootstrap my agent", "install my starter pack", or starts in a fresh repo and wants their usual defaults:

**Load and execute the skill at `skills/ai-starter-pack/SKILL.md`** — it contains the full install menu, dedup logic, and per-component write instructions. All paths inside that file are relative to its own directory.

> If `skills/ai-starter-pack/SKILL.md` is not present (e.g. you cloned the repo without submodules, or are reading this from a project that only copied this bootstrap), fetch the skill from:
> `https://github.com/TomYang1993/ai-starter-pack/tree/main/skills/ai-starter-pack`

Do not install anything until reading that file — it defines what goes where for your specific host.
