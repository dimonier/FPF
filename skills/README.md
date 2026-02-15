# FPF Agent Skill

## What is This?

This repository contains the [First Principles Framework](https://github.com/ailev/FPF) refactored as an AI agent skill with progressive pattern loading and domain-based navigation.

Instead of loading the entire FPF specification at once, AI agents read the Table of Content and load only relevant pattern files on demand. No special tools are required—only standard file reading (e.g. read `intro_table_of_content.md`, then `fpf-patterns/<ID>.md`).

## How to Use This Skill

### Prerequisites

- An AI assistant that can read files (Cursor, Claude Code, Aider, Continue, etc.)
- Git (to clone this repository)

### Installation and usage

1. Clone or download the `skills/fpf` folder and its contents.
2. Put the `fpf` folder into the `skills` folder of your IDE or CLI tool:
   - Cursor: `~/.cursor/skills` or project `skills/`
   - Claude Code: `~/.claude/skills/`
   - Other IDE: check documentation for skill location
3. Ask the agent to use the FPF skill when doing your task.

### Verification

Ask the agent: "Use the FPF skill and do /your task/."

The agent should confirm use of FPF and apply FPF terminology and patterns (e.g. Holon, MethodDescription vs Work, Evidence Graph).

## Repository Structure

```
skills/fpf/
├── SKILL.md                          # Skill manifest (AI navigation hub)
└── reference/                        # Reference materials
    ├── agent_index_patterns.md
    ├── agent_index_queries.md
    ├── agent_index_keywords.md
    ├── intro_preface_non-normative.md
    └── fpf-patterns/                 # Pattern bodies (flat folder)
        └── A.1.md, A.2.md, …         # One file per pattern ID (e.g. A.1.md, B.5.md)
```

- **Navigation**: Use `reference/agent_index_queries.md`, `reference/agent_index_keywords.md`, or `reference/agent_index_patterns.md` to find pattern IDs; then read `reference/fpf-patterns/<ID>.md`.
- **Paths**: All paths are relative to the skill root. When the skill is used as a project skill, use paths from the repo root (e.g. `skills/fpf/reference/...`).

## Difference from Original FPF

| Original FPF                   | This skill                               |
| ------------------------------ | ----------------------------------------- |
| Single large spec file         | Many pattern files in `fpf-patterns/*.md` |
| Load entire spec into context  | Progressive loading via Table of Content  |
| May need RAG or custom tools   | File reading only (intro_table_of_content + &lt;ID&gt;.md) |
| Monolithic specification       | Domain-organized index + flat pattern dir |
| For LLM context                | For AI agent skill (Cursor, etc.)         |
