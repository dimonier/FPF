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
├── references/                       # Reference materials
│   ├── index.md                      # Links to intro docs and Table of Content
│   ├── intro_table_of_content.md     # Main navigation index (Keywords & Search Queries, pattern IDs)
│   ├── intro_preface_non-normative.md
│   ├── intro_first_principles_framework_fpf_core_conceptual_specification.md
│   ├── fpf-patterns/                 # Pattern bodies (flat folder)
│   │   ├── A.1.md, A.2.md, …         # One file per pattern ID (e.g. A.1.md, B.5.md)
│   │   └── index.md                  # Optional table; primary navigation is intro_table_of_content.md
└── scripts/                          # Optional automation (e.g. split_fpf_spec.py)
    ├── fpf_tools.py                  # Optional: search/read helpers (e.g. for pydantic-ai)
    └── …
```

- **Navigation**: Use [references/intro_table_of_content.md](skills/fpf/references/intro_table_of_content.md) to find pattern IDs (Keywords & Search Queries, titles, dependencies). Then read the pattern body from `references/fpf-patterns/<ID>.md`.
- **Paths**: All paths are relative to the skill root. When the skill is used as a project skill, use paths from the repo root (e.g. `skills/fpf/references/...`).

## Agent Workflow

Agents using this skill follow the canonical reasoning cycle:

1. **OBSERVE** → Understand the user's request
2. **NAVIGATE** → Use SKILL.md to identify task type and likely domains
3. **SEARCH** → Read `references/intro_table_of_content.md`; use Keywords & Search Queries or section titles to pick pattern IDs
4. **LOAD** → Read `references/fpf-patterns/<ID>.md` for each ID (batch multiple reads in one step when loading several patterns)
5. **PLAN** → Build a MethodDescription from the loaded patterns
6. **EXECUTE** → Do the work, keeping strict Object≠Description distinction (A.7)
7. **AUDIT** → Record Work with evidence and cite source patterns

See [SKILL.md](skills/fpf/SKILL.md) for full navigation and discipline rules.

## Maintenance Workflow

For maintaining and updating the FPF skill structure:

1. **Edit source**: Update the spec source (e.g. FPF-Spec or decomposed files).
2. **Regenerate if needed**: Run any scripts that regenerate pattern files or index (e.g. `split_fpf_spec.py` if present).
3. **Commit**: Version control the changes.

See [scripts/index.md](skills/fpf/scripts/index.md) if present for automation details.

## Quick Domain Reference

Domains in the Table of Content (intro_table_of_content.md) group patterns by semantic area:

| Domain         | Use when...                                      |
| -------------- | ------------------------------------------------- |
| foundations    | understanding entities, roles, distinctions       |
| transformation | planning tasks, executing work                   |
| reasoning      | problem-solving, hypothesis generation            |
| trust-evidence | evaluating claims, checking reliability          |
| aggregation    | combining parts, understanding emergence         |
| signature      | designing interfaces, defining boundaries         |
| architheories  | domain-specific modeling, specialized calculi     |
| constitution   | understanding FPF rules, authoring patterns      |
| unification    | integrating across domains, building bridges      |
| ethics         | ethical considerations, conflict resolution      |
| sota           | benchmarking, discipline-specific best practices |

## Difference from Original FPF

| Original FPF                   | This skill                               |
| ------------------------------ | ----------------------------------------- |
| Single large spec file         | Many pattern files in `fpf-patterns/*.md` |
| Load entire spec into context  | Progressive loading via Table of Content  |
| May need RAG or custom tools   | File reading only (intro_table_of_content + &lt;ID&gt;.md) |
| Monolithic specification       | Domain-organized index + flat pattern dir |
| For LLM context                | For AI agent skill (Cursor, etc.)         |
