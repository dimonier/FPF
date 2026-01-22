# Navigation Architecture for Decomposed Skills

Best practices for structuring SKILL.md and index.md files based on AI agent navigation patterns.

## Core Principle: AI-Centric Navigation

Navigation should optimize for **AI agent decision-making**, not human documentation browsing.

**Key differences from human docs:**
- **Decision trees** over table of contents
- **"Load when..."** guidance over descriptions
- **Progressive disclosure** over comprehensive overviews
- **Single point of entry** over multiple parallel entry points

## Level 2: SKILL.md Structure

The root skill file is an **AI navigation hub** with decision logic.

### Essential Components

1. **Pattern Selection Logic** (decision tree)
2. **Core Workflow** (when applicable)
3. **Navigation Hub** (domain selector)
4. **Starter Patterns** (first-time usage)
5. **Critical Disciplines** (cross-cutting concerns)

### Example: SKILL.md Template

```markdown
---
name: skill-name
description: Concise trigger description for skill discovery
---

# Skill Name

Brief 1-2 sentence overview.

## Pattern Selection Logic

Choose path based on your task:

1. **First-time user** → Read [Starter Patterns](#starter-patterns)
2. **Specific domain known** → Jump to [Navigation Hub](#navigation-hub)
3. **Cross-cutting concern** → Check [Critical Disciplines](#critical-disciplines)
4. **Complex multi-domain task** → Start with Domain A, then integrate Domain B

## Core Workflow

For typical usage:

1. Identify your task type
2. Load relevant domain index
3. Select specific patterns
4. Apply with evidence

## Navigation Hub

**Choose domain based on what you need:**

- **Domain A** ([index](content-dir/domain-a/index.md))
  - **Load when:** [specific usage scenario]
  - **Starters:** A.1, A.2, A.7
  - **Complements:** Domain B (for X), Domain C (for Y)

- **Domain B** ([index](content-dir/domain-b/index.md))
  - **Load when:** [specific usage scenario]
  - **Starters:** B.1, B.3
  - **Complements:** Domain A (for X)

## Starter Patterns (First-Time Users)

Essential patterns for initial skill usage:

1. **A.1** - Foundation concept: why/when
2. **A.2** - Core distinction: why/when
3. **B.1** - Key workflow: why/when

## Critical Disciplines

Cross-cutting concerns that apply throughout:

- **Evidence chains:** Always link claims to evidence (A.10)
- **Boundary discipline:** Respect context boundaries (A.6)
- **Role clarity:** Distinguish identity from function (A.2)
```

### Size Management

**If SKILL.md approaches 50KB:**

1. **Keep**: Pattern Selection Logic, Navigation Hub (domain table only)
2. **Move to references/principles.md**: Detailed cross-cutting concerns
3. **Move to domain indexes**: Starter pattern details
4. **Remove**: Verbose descriptions, examples, duplicate navigation

**NEVER split SKILL.md** - it must remain single point of entry.

## Level 3: Master Index (Optional)

For large skills with 8+ domains, consider a master index at `content-dir/index.md`.

### When to Create

- **Create** if: 10+ domains, complex interdependencies
- **Skip** if: Few domains, SKILL.md navigation sufficient

### Structure

```markdown
# Content Library Index

Progressive disclosure navigation for [N] patterns across [M] domains.

## Quick Domain Selection

**Choose domain based on your task:**

**Core domains (most frequently needed):**
- **System modeling** → [foundations](#foundations) (entities, roles)
- **Task execution** → [transformation](#transformation) (methods, work)

**Specialized domains:**
- **Interface design** → [signature](#signature) (boundaries, contracts)
- **Composition** → [aggregation](#aggregation) (Gamma operator)

## Domains

### foundations

**32 patterns** | [index](foundations/index.md)

Core ontological concepts: holons, entities, roles, characteristics.

**Load when:** modeling entities, defining roles, measuring characteristics

**Starters:** A.1 (Holon), A.2 (Roles), A.7 (Distinctions)

**Complements:** transformation (for execution), signature (for boundaries)

---

### transformation

**10 patterns** | [index](transformation/index.md)

[Same structure as above]

---

**Total: [N] patterns across [M] domains**
```

### Maintenance Policy

**Manual maintenance only** - generation scripts should:
- Generate this file only if it doesn't exist
- Never overwrite existing content
- Update via manual editing when structure changes

Rationale: Master indexes require editorial judgment about domain relationships and descriptions.

## Level 3: Domain Indexes

Each domain's `index.md` serves as both **navigation hub** and **pattern catalog**.

### Standard Structure

```markdown
# Domain Name

Brief 1-2 sentence domain description.

## When to Load This Domain

**Load [domain] when you need to:**
- [Specific scenario 1]
- [Specific scenario 2]
- [Specific scenario 3]

## Starter Patterns (Read First)

Essential patterns for domain usage:

- **A.1** - Pattern Name: brief why/when (1 line)
- **A.2** - Pattern Name: brief why/when (1 line)

## Core Pattern Clusters

**Cluster Name (A.1-A.5):**
- A.1 - Brief description
- A.2 - Brief description
- A.3 - Brief description

**Cluster Name (A.6-A.10):**
- A.6 - Brief description
- A.10 - Brief description

## Related Domains

**Use together with:**
- **domain-b** - for [specific use case] (patterns X, Y)
- **domain-c** - to [specific action] (patterns Z)

## Patterns

| Pattern | Title | Status | Keywords & Search Queries | Dependencies | Size |
|---------|-------|--------|---------------------------|--------------|------|
| [A.1](A.1_file.md) | Title | Stable | *Keywords:* x, y *Queries:* "Q?" | **Builds on:** A.0 | 25 KB |
```

### Navigation Sections (Manual)

The four navigation sections are **manually authored** and **preserved across regenerations**:

1. **When to Load This Domain** - Decision logic for domain selection
2. **Starter Patterns** - First patterns to read for domain understanding
3. **Core Pattern Clusters** - Logical groupings with brief descriptions
4. **Related Domains** - Cross-domain integration guidance

**These sections are editorial** - they require understanding usage patterns, not just spec structure.

### Pattern Table (Auto-Generated)

The `## Patterns` table is **auto-generated from source spec metadata**:

- Pattern ID & link
- Title
- Status (Stable/Draft/etc.)
- Keywords & Search Queries (from TOC)
- Dependencies (from TOC)
- File size

**Never manually edit the pattern table** - it's regenerated on each script run.

## Generation Script Pattern

Scripts should implement **navigation preservation**:

```python
def parse_existing_navigation(index_path: Path) -> str:
    """Extract everything before ## Patterns section."""
    if not index_path.exists():
        return ""
    
    content = index_path.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    # Find "## Patterns" or "## All Patterns" header
    for i, line in enumerate(lines):
        if line.strip() in ['## Patterns', '## All Patterns']:
            # Return everything before this section
            return '\n'.join(lines[:i])
    
    return ""  # No pattern section found

def generate_domain_index(domain: str, patterns: list):
    """Generate domain index preserving navigation."""
    index_path = OUTPUT_DIR / domain / "index.md"
    
    # Extract existing navigation
    navigation = parse_existing_navigation(index_path)
    
    if navigation:
        # Preserve existing navigation
        content = navigation + "\n\n## Patterns\n\n"
    else:
        # Generate minimal header for new domains
        content = f"""# {domain.title()}

Brief description.

**Load when**: [usage scenario]

## Patterns

"""
    
    # Append regenerated pattern table
    content += generate_pattern_table(patterns)
    
    index_path.write_text(content, encoding='utf-8')
```

### Why Preserve Navigation?

1. **Editorial judgment required** - "When to Load" and "Starters" need usage understanding
2. **Interdependencies are semantic** - Can't auto-detect from spec structure
3. **Clusters are conceptual** - Grouping by meaning, not structure
4. **Manual work is valuable** - Don't discard human curation

### Why Regenerate Tables?

1. **Metadata changes** - Status, keywords, dependencies update in source spec
2. **New patterns added** - Auto-appear in table without manual editing
3. **Size tracking** - File sizes recalculated on each run
4. **Consistency** - Uniform formatting across all domains

## AI Agent Best Practices

### Single Point of Entry

**Good**: All domain links in SKILL.md navigation hub
**Bad**: Domain indexes link to each other in mesh topology

Why: Agent needs clear entry hierarchy, not exploration maze.

### Decision-Oriented Guidance

**Good**: "Load foundations when modeling entity structure"
**Bad**: "Foundations contains patterns about entities"

Why: Agent needs decision criteria, not descriptions.

### Progressive Disclosure

**Good**: SKILL.md → domain index → pattern file
**Bad**: SKILL.md includes pattern summaries → pattern file

Why: Load detail only when needed, minimize context usage.

### Avoid Redundancy

**Good**: Pattern listed once in domain index
**Bad**: Pattern listed in domain index AND master index AND SKILL.md

Why: Redundancy wastes context, creates maintenance burden.

## Size Budgets by Level

| File | Max Size | Content Type |
|------|----------|--------------|
| SKILL.md | 50KB / ~500 lines | Navigation + decision logic |
| content-dir/index.md | 50KB / ~500 lines | Domain directory (if needed) |
| domain/index.md | 20KB / ~200 lines | Navigation + pattern table |
| pattern files | 50KB | Full pattern content |

**If domain index exceeds 20KB:**
- Check navigation sections - keep concise
- Check pattern table - consider sub-domains
- Don't add examples or verbose descriptions

## Anti-Patterns

### ❌ Human Documentation Structure

```markdown
# Domain

## Overview
[3 paragraphs of background]

## Key Concepts
[Detailed definitions]

## Patterns
[Flat list]
```

Why bad: Agent doesn't need background, needs decision guidance.

### ❌ Redundant Navigation

```markdown
# SKILL.md
- Domain A: foundations for X, contains A.1, A.2...
- Domain B: workflows for Y, contains B.1, B.2...

# domain-a/index.md
- Domain A covers X
- Related to Domain B for Y...
```

Why bad: Same info repeated, wastes context.

### ❌ Cross-Linked Mesh

```markdown
# domain-a/index.md
Related: [Domain B](../domain-b/index.md)

# domain-b/index.md  
Related: [Domain A](../domain-a/index.md)
```

Why bad: Creates navigation loops, unclear entry point.

### ✅ Correct Hierarchy

```markdown
# SKILL.md (entry point)
- Domain A: Load when [scenario]
- Domain B: Load when [scenario]

# domain-a/index.md
Related Domains: domain-b - for [specific use case]

# domain-b/index.md
Related Domains: domain-a - for [specific use case]
```

Why good: Clear hierarchy, one-way references from hub, semantic relationships.
