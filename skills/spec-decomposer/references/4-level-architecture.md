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

**Purpose**: AI-centric navigation hub with decision logic

**Content**:
- Pattern selection logic (decision tree)
- Core workflow (if applicable)
- Domain navigation hub (with "Load when..." guidance)
- Starter patterns (for first-time usage)
- Critical disciplines (cross-cutting concerns)

**Loaded on skill trigger** - when Claude determines skill is relevant.

**Structure**:
```markdown
# [Skill Name]

## Pattern Selection Logic

Choose path based on your task:
1. First-time user → [Starter Patterns](#starter-patterns)
2. Specific domain → [Navigation Hub](#navigation-hub)
3. Cross-cutting concern → [Critical Disciplines](#critical-disciplines)

## Core Workflow
[Essential steps that always apply]

## Navigation Hub

**Choose domain based on what you need:**

- **Domain A** ([index](content-dir/domain-a/index.md))
  - **Load when:** [specific usage scenario]
  - **Starters:** A.1, A.2
  - **Complements:** Domain B (for X)

## Starter Patterns

1. **A.1** - Foundation concept: why/when
2. **A.2** - Core distinction: why/when

## Critical Disciplines

- **Evidence chains:** Always link claims to evidence (A.10)
- **Boundary discipline:** Respect context boundaries (A.6)
```

**Constraint**: Keep under 500 lines / 50KB. If approaching limit, move detailed content to Level 3.

See [navigation-architecture.md](navigation-architecture.md) for detailed SKILL.md structure patterns.

## Level 3: Domain Indexes

**Location**: `{skill}/{content-dir}/{domain}/index.md`

**Purpose**: Navigation hub + pattern catalog for specific domain

**Content**:
- Brief domain description (1-2 sentences)
- When to Load guidance (decision criteria)
- Starter Patterns (entry points)
- Core Pattern Clusters (conceptual groupings)
- Related Domains (cross-domain integration)
- Pattern table (auto-generated from source metadata)

**Structure**:
```markdown
# [Domain Name]

Brief description.

## When to Load This Domain

**Load [domain] when you need to:**
- [Specific scenario 1]
- [Specific scenario 2]

## Starter Patterns (Read First)

- **A.1** - Pattern Name: brief why/when
- **A.2** - Pattern Name: brief why/when

## Core Pattern Clusters

**Cluster Name (A.1-A.5):**
- A.1 - Brief description
- A.2 - Brief description

## Related Domains

**Use together with:**
- **domain-b** - for [use case] (patterns X, Y)

## Patterns

| Pattern | Title | Status | Keywords & Queries | Dependencies | Size |
|---------|-------|--------|--------------------|--------------|------|
| [A.1](A.1_file.md) | Title | Stable | *Keywords:* x... | **Builds on:** A.0 | 25 KB |
```

**Maintenance**:
- Navigation sections (When to Load, Starters, Clusters, Related) are **manually authored**
- Pattern table is **auto-generated** from source spec metadata
- Generation scripts should **preserve navigation** while regenerating table

**Constraint**: Keep under 200 lines / 20KB. This is navigation, not content.

See [navigation-architecture.md](navigation-architecture.md) for detailed domain index patterns and generation script examples.

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
