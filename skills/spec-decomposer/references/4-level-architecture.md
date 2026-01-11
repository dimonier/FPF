# 4-Level Progressive Disclosure Architecture

## Overview

Large specifications require multiple disclosure levels to keep context window usage efficient while maintaining navigability.

```
Level 1: Metadata (~100 words)     - Always in context
Level 2: SKILL.md body (<50KB)     - Loaded on skill trigger
Level 3: Domain indexes (<20KB)    - Loaded when exploring domain
Level 4: Individual units (<50KB)  - Loaded for specific need
```

## Level 1: Metadata

**Location**: SKILL.md YAML frontmatter

**Content**:
- `name`: Skill identifier
- `description`: Comprehensive trigger description (when to use)

**Always loaded** - Claude sees this to decide if skill is relevant.

**Example**:
```yaml
---
name: fpf
description: First Principles Framework for structured reasoning. Use for any task requiring auditable thinking, evidence chains, or systematic problem-solving.
---
```

## Level 2: SKILL.md Body

**Location**: SKILL.md markdown content (after frontmatter)

**Content**:
- Core workflow that always applies
- Essential concepts (minimal)
- Domain navigation table
- Tool documentation (if any)

**Loaded on skill trigger** - when Claude determines skill is relevant.

**Structure**:
```markdown
# [Skill Name]

## Core Workflow
[Essential steps that always apply]

## Domain Navigation

| Domain | Index | Load when... |
|--------|-------|--------------|
| foundations | fpf-core/foundations/index.md | Understanding basic concepts |
| workflows | fpf-core/workflows/index.md | Planning task execution |
```

**Constraint**: Keep under 500 lines / 50KB. If approaching limit, move content to Level 3.

## Level 3: Domain Indexes

**Location**: `{skill}/references/{domain}/index.md` or `{skill}/{content-dir}/{domain}/index.md`

**Content**:
- 1-2 sentence domain description
- Table of units with "Load when..." guidance
- Key concepts summary (optional, brief)

**Structure**:
```markdown
# [Domain Name]

Brief description of what this domain covers.

## Units

| ID | Title | Load when... |
|----|-------|--------------|
| A.1 | Holonic Foundation | Understanding entity composition |
| A.2 | Role Taxonomy | Modeling responsibilities |

## Key Concepts

- **Holon**: Whole that is also a part
- **Role**: Function vs identity distinction
```

**Constraint**: Keep under 200 lines / 20KB. This is navigation, not content.

## Level 4: Individual Units

**Location**: `{skill}/{content-dir}/{domain}/{unit_id}_{title}.md`

**Content**: Full content of single atomic unit from source specification.

**Constraint**: 
- Max 50KB per file
- If larger, create sub-index and split into sub-units

## Loading Flow

```
User query: "How do I evaluate claim reliability?"

1. L1 (always): Claude sees skill metadata, determines FPF relevant
2. L2 (trigger): Claude loads SKILL.md body, sees domain table
3. L3 (navigate): Claude loads trust-evidence/index.md, sees pattern list
4. L4 (access): Claude loads B.3_trust_calculus.md for specific content
```

## Anti-Patterns

### Loading Everything

**Bad**: SKILL.md contains all content or links to single massive reference
**Why bad**: Defeats progressive disclosure, wastes context

### Structural Mirroring

**Bad**: Domains match source document chapters
**Why bad**: Source structure != usage patterns

### Deep Nesting

**Bad**: L4 files contain links to L5 files
**Why bad**: Navigation becomes expensive, hard to track depth

### Missing "Load when..." Guidance

**Bad**: Index lists units without usage context
**Why bad**: Claude can't efficiently choose what to load
