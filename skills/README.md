# FPF Agent Skill

## What is This?

This repository contains the [First Principles Framework](https://github.com/ailev/FPF) refactored as an AI agent skill with progressive pattern loading and domain-based navigation.

Instead of loading the entire FPF specification at once, AI agents can search and load only relevant patterns on demand.

## How to Use This Skill

### Prerequisites

- Python 3.10+ (for tool functions)
- AI coding assistant that supports skills/tools (Cursor, Cloude Code, Aider, Continue, etc.)
- Git (to clone this repository)

### Installation and usage

1. Clone or download `skill/fpf` folder and its contents.
2. Put `fpf` folder into `skills` folder of your IDE / CLI Code tool:
  - Cursor: `~/.cursor/skills`
  - Cloude Code: `~/.claude/skills/`
  - Other IDE: check documentation on where skills are located
3. Ask agent to use the skill during task execution.

### Verification

Ask you agent "Use fpf skill and do /your task go here/".

The agent should confirm that they found and use FPF, and start operating FPF terminology and patterns.

## Repository Structure

```
skills/fpf/
├── SKILL.md                          # Skill manifest (AI navigation hub)
├── references/                       # Reference materials
│   ├── fpf-patterns/                 # 169 patterns split by domain
│   │   ├── index.md                  # Master index with domain navigation
│   │   ├── foundations/              # 32 patterns: entities, roles, identity
│   │   ├── transformation/           # 10 patterns: planning, work execution
│   │   ├── reasoning/                # 5 patterns: problem-solving, abduction
│   │   ├── trust-evidence/           # 9 patterns: reliability, evidence chains
│   │   ├── aggregation/              # 13 patterns: composition, emergence
│   │   ├── signature/                # 15 patterns: interfaces, boundaries
│   │   ├── architheories/            # 20 patterns: specialized calculi
│   │   ├── constitution/             # 30 patterns: FPF governance, authoring
│   │   ├── unification/              # 19 patterns: cross-domain bridges
│   │   ├── ethics/                   # 1 pattern: ethical considerations
│   │   └── sota/                     # 15 patterns: benchmarks, best practices
│   └── prompts/                      # 9 workflow and principle guides
│       ├── index.md                  # Prompts documentation
│       ├── workflow.md               # Canonical workflow guide
│       ├── initial-plan.md           # Initial planning template
│       ├── principles.md             # Core principles guide
│       ├── characterisation.md       # Characterization workflow
│       ├── keywords.md               # Keyword extraction guide
│       ├── naming.md                 # Naming conventions
│       ├── p2w.md                    # Plan-to-work transformation
│       ├── sota.md                   # State-of-the-art integration
│       └── uts.md                    # Unified term sheet guide
└── scripts/                          # Automation and maintenance tools
    ├── index.md                      # Scripts documentation
    ├── fpf_tools.py                  # Search & load functions
    └── split_fpf_spec.py             # Specification splitting & regeneration
```

## Agent Workflow

AI agents using this skill follow the canonical reasoning cycle:

1. **OBSERVE** → Understand the user's request
2. **NAVIGATE** → Use SKILL.md decision tree to select relevant domain
3. **SEARCH** → Use `fpf_search_index` to find patterns (optional, for keyword search)
4. **LOAD** → Read domain/pattern indexes from `references/fpf-patterns/` and load specific pattern details
5. **PLAN** → Create MethodDescription based on loaded patterns
6. **EXECUTE** → Implement the plan (actual work)
7. **AUDIT** → Record Work with evidence

See [SKILL.md](skills/fpf/SKILL.md) for complete usage guidelines and navigation patterns.

## Maintenance Workflow

For maintaining and updating the FPF skill structure:

1. **Edit source**: Update `FPF-Spec.md` (patterns, TOC metadata)
2. **Regenerate files**: Run `uv run skills/fpf/scripts/split_fpf_spec.py`
3. **Review changes**: Pattern tables updated, navigation sections preserved
4. **Enhance navigation**: Manually update domain `references/fpf-patterns/<domain>/index.md` navigation sections if needed
5. **Commit**: Version control the changes

See [scripts/index.md](skills/fpf/scripts/index.md) for detailed automation workflow and best practices.

## Quick Domain Reference


| Domain         | Patterns | Use when...                                      |
| -------------- | -------- | ------------------------------------------------ |
| foundations    | 32       | understanding entities, roles, distinctions      |
| transformation | 10       | planning tasks, executing work                   |
| reasoning      | 5        | problem-solving, hypothesis generation           |
| trust-evidence | 9        | evaluating claims, checking reliability          |
| aggregation    | 13       | combining parts, understanding emergence         |
| signature      | 15       | designing interfaces, defining boundaries        |
| architheories  | 20       | domain-specific modeling, specialized calculi    |
| constitution   | 30       | understanding FPF rules, authoring patterns      |
| unification    | 19       | integrating across domains, building bridges     |
| ethics         | 1        | ethical considerations, conflict resolution      |
| sota           | 15       | benchmarking, discipline-specific best practices |


**Total**: 169 patterns

## Difference from Original


| Original FPF                   | This Branch                         |
| ------------------------------ | ----------------------------------- |
| Single 4MB file (50,000 lines) | 169 separate pattern files          |
| Load entire spec to LLM        | Progressive loading via navigation  |
| Requires RAG infrastructure    | Uses file access + progressive disclosure |
| Monolithic specification       | Domain-organized pattern library    |
| For LLM context                | For AI agent skill system           |
