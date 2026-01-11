# Operational Prompts

After decomposing a specification into a skill structure, consider adding operational prompts to guide skill usage.

## When Needed

Add `prompts/` folder when:
- Skill has complex multi-step workflows
- Content requires specific usage patterns
- Agent needs guidance on navigation strategy
- Key concepts need quick reference summary

Skip prompts when:
- Skill is simple/single-purpose
- SKILL.md already provides sufficient guidance
- Content is self-explanatory

## Prompts Folder Structure

```
skill-name/
├── SKILL.md
├── {content}/
└── prompts/           # Optional
    ├── workflow.md    # Mandatory workflow steps
    ├── principles.md  # Key concepts quick reference
    ├── keywords.md    # Navigation/search guidance
    └── templates/     # Reusable templates (optional)
```

## Prompt Types

### workflow.md

Step-by-step process for using the skill on any task.

**Structure:**
```markdown
# [Skill] Workflow

## Step 1: [Name]
- What to do
- Expected output

## Step 2: [Name]
...
```

**Example** (from FPF):
```markdown
## Step 1: FPF DECOMPOSITION
Map user request to FPF concepts:
- Holon: What is the whole being discussed?
- BoundedContext: What domain gives meaning to terms?
- Method vs Work: Planning or execution?

## Step 2: FPF REASONING
Navigate to relevant domain, load patterns, apply analysis.
```

### principles.md

Quick reference for essential concepts. NOT full content - just reminders with paths to full content.

**Structure:**
```markdown
# Core Principles

## [Concept Name]
**Domain**: [domain] | **Path**: `path/to/full/content.md`

[2-3 sentence summary]
```

**Key rule**: Include paths to full content so agent can load details when needed.

### keywords.md

Navigation guidance - how to find content efficiently.

**Structure:**
```markdown
# Navigation Guide

## Preferred: Domain-Based Navigation

| Need | Domain | Index Path |
|------|--------|------------|
| [use case] | [domain] | `path/to/index.md` |

## Alternative: Keyword Search

Use with search tools when domain unclear:
[list of valid keywords]
```

## Writing Guidelines

1. **Keep prompts concise** - they're loaded frequently
2. **Include paths** - always link to full content
3. **Focus on HOW** - prompts explain usage, not content
4. **Update with structure** - if domains change, update prompts

## Example: FPF Prompts

FPF skill uses prompts for:

| Prompt | Purpose |
|--------|---------|
| `workflow.md` | 4-step mandatory process (decompose, reason, execute, translate) |
| `principles.md` | Quick reference for A.7, A.10, B.3, B.5 with file paths |
| `keywords.md` | Domain navigation table + search keywords |
| `initial-plan.md` | Task execution template |

Total prompts size: ~3KB (minimal context cost).
