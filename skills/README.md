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
├── SKILL.md                    # Skill manifest for AI agents
├── glossary.md                 # FPF terminology
├── fpf-core/                   # 159 patterns split by domain
│   ├── index.md                # Master index
│   ├── foundations/            # 26 patterns: entities, roles, identity
│   ├── transformation/         # 9 patterns: planning, work execution
│   ├── reasoning/              # 5 patterns: problem-solving, abduction
│   ├── trust-evidence/         # 9 patterns: reliability, evidence chains
│   ├── aggregation/            # 13 patterns: composition, emergence
│   ├── signature/              # 15 patterns: interfaces, boundaries
│   ├── architheories/          # 20 patterns: specialized calculi
│   ├── constitution/           # 28 patterns: FPF governance
│   ├── unification/            # 19 patterns: cross-domain bridges
│   ├── ethics/                 # 1 pattern: ethical considerations
│   └── sota/                   # 14 patterns: benchmarks, best practices
├── prompts/                    # Workflow and principle guides
└── scripts/                    # Python tools
    ├── fpf_tools.py            # Search & load functions
    └── split_fpf_spec.py       # Specification splitting utility
```

## Agent Workflow

AI agents using this skill have to follow the canonical reasoning cycle:

1. **OBSERVE** → Understand the user's request
2. **SEARCH** → Use `fpf_search_index` to find relevant patterns
3. **LOAD** → Use `fpf_read_pattern` to load specific pattern details
4. **PLAN** → Create MethodDescription based on loaded patterns
5. **EXECUTE** → Implement the plan (actual work)
6. **AUDIT** → Record Work with evidence

See [SKILL.md](skills/fpf/SKILL.md) for complete usage guidelines.

## Quick Domain Reference


| Domain         | Patterns | Use when...                                      |
| -------------- | -------- | ------------------------------------------------ |
| foundations    | 26       | understanding entities, roles, distinctions      |
| transformation | 9        | planning tasks, executing work                   |
| reasoning      | 5        | problem-solving, hypothesis generation           |
| trust-evidence | 9        | evaluating claims, checking reliability          |
| aggregation    | 13       | combining parts, understanding emergence         |
| signature      | 15       | designing interfaces, defining boundaries        |
| architheories  | 20       | domain-specific modeling, specialized calculi    |
| constitution   | 28       | understanding FPF rules, authoring patterns      |
| unification    | 19       | integrating across domains, building bridges     |
| ethics         | 1        | ethical considerations, conflict resolution      |
| sota           | 14       | benchmarking, discipline-specific best practices |


**Total**: 159 patterns

## Difference from Original


| Original FPF                   | This Branch                         |
| ------------------------------ | ----------------------------------- |
| Single 4MB file (50,000 lines) | 159 separate pattern files          |
| Load entire spec to LLM        | Progressive loading via tools       |
| Requires RAG infrastructure    | Uses function calling + file access |
| Monolithic specification       | Domain-organized pattern library    |
| For LLM context                | For AI agent skill system           |


## Spec Decomposer Agent Skill

This repository also includes **[Spec Decomposer](skills/spec-decomposer/SKILL.md)** - the agent skill that was developed and used to refactor the original monolithic FPF specification into the current skill format.

**What it does:**
- Transforms large unified specifications (>50KB) into agent skills with progressive disclosure
- Groups content by semantic meaning/use-case (not structural divisions)
- Implements 4-level navigation hierarchy for context efficiency
- Enforces size constraints (<50KB per file) to prevent context overflow

**How it was applied to FPF:**
1. Analyzed 4MB `FPF-Spec.md` structure and pattern semantics
2. Identified 11 semantic domains (foundations, reasoning, aggregation, etc.)
3. Mapped 159 patterns to domains by usage context
4. Generated navigational indexes with "load when..." guidance
5. Created Python implementation (`skills/fpf/scripts/split_fpf_spec.py`) for automated processing

The Spec Decomposer skill is reusable for any large documentation, framework, or knowledge base that needs conversion into AI agent skill format.

**See**: [skills/spec-decomposer/](skills/spec-decomposer/) for complete skill documentation and reference materials.