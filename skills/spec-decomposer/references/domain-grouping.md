# Domain Grouping

## Principle: Semantic over Structural

Group content by **how it will be used**, not by how the source document is organized.

## Identification Process

### Step 1: List Use Cases

Before looking at document structure, list how Claude will use this knowledge:

```
- Understanding what entities are
- Planning task execution
- Evaluating claim reliability
- Combining/composing parts
- Following rules and constraints
```

### Step 2: Map Content to Use Cases

For each section/pattern/article in source:
- Ask: "When would Claude need this?"
- Assign to use-case domain

### Step 3: Validate Groupings

Check each domain:
- Does it have a coherent theme?
- Are items likely to be needed together?
- Is there clear "Load when..." guidance?

## Heuristics

### Cross-Reference Analysis

Items that frequently reference each other likely belong together:
- B.3 Trust Calculus references A.10 Evidence Graph
- Both deal with reliability -> same domain

### Dependency Chains

Items with "Builds on" / "Prerequisite for" relationships:
- Keep foundation items in same domain as dependent items
- Or clearly link domains in navigation

### Keyword Clustering

Items sharing domain-specific vocabulary:
- "F-G-R", "reliability", "evidence" -> trust-evidence domain
- "Gamma", "aggregation", "composition" -> aggregation domain

## Common Domain Patterns

### For Frameworks/Methodologies

| Domain | Typical Content |
|--------|-----------------|
| foundations | Core concepts, definitions, ontology |
| workflows | Processes, procedures, how-to |
| evaluation | Assessment, metrics, quality |
| composition | Combining, aggregating, relating |
| constraints | Rules, principles, limitations |

### For APIs/Technical Specs

| Domain | Typical Content |
|--------|-----------------|
| getting-started | Setup, authentication, basics |
| core-operations | Main functionality |
| advanced | Edge cases, optimization |
| reference | Complete API surface |
| troubleshooting | Errors, debugging |

### For Knowledge Bases

| Domain | Typical Content |
|--------|-----------------|
| concepts | Definitions, explanations |
| procedures | Step-by-step guides |
| examples | Use cases, samples |
| reference | Lookup tables, specifications |

## Anti-Patterns

### Mirroring Source Structure

**Bad**: 
```
Part A -> domain_a/
Part B -> domain_b/
Part C -> domain_c/
```

**Why**: Source chapters are for reading order, not usage patterns.

### Single Mega-Domain

**Bad**: All content in one domain with huge index

**Why**: Defeats selective loading; forces reading entire index.

### Too Many Domains

**Bad**: 20+ domains with 2-3 items each

**Why**: Navigation overhead; hard to know which domain to check.

**Target**: 5-12 domains for most specifications.

### Overlapping Domains

**Bad**: Same content could reasonably be in multiple domains

**Fix**: Choose primary domain by most common use case; add cross-references.
