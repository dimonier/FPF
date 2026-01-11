---
name: fpf
description: First Principles Framework - structured reasoning skill for any task requiring auditable thinking, evidence chains, systematic problem-solving, or holonic composition. Use FPF patterns to guide reasoning on engineering, research, and management tasks.
priority: high
auto_load: true
---

# FPF Thinking Skill

FPF is an "Operating System for Thought" - a rigorous architecture for thinking that ensures auditable reasoning, clear distinction between plans and execution, and structured knowledge access.

## Core Workflow (B.5 Canonical Reasoning Cycle)

For every task, follow this cycle:

1. **OBSERVE**: Understand the user's request
2. **SEARCH**: Use `fpf_search_index` to find relevant patterns
3. **LOAD**: Use `fpf_read_pattern` to load specific pattern details
4. **PLAN**: Create MethodDescription based on loaded patterns
5. **EXECUTE**: Deploy the plan (actual work)
6. **AUDIT**: Ensure Work record is logged with evidence

## Available Tools

### fpf_search_index(keyword: str) -> str

Search for FPF patterns by keyword. Returns list of pattern IDs with titles and domains.

### fpf_read_pattern(pattern_id: str) -> str

Load full content of a specific FPF pattern.

### fpf_list_domain(domain: str) -> str

List all patterns in a specific domain. Use to explore available patterns.

## Domain Navigation

Navigate to domain indexes based on your task:

| Domain | Index | Load when... |
|--------|-------|--------------|
| Foundations | [fpf-core/foundations/index.md](fpf-core/foundations/index.md) | understanding entities, roles, distinctions |
| Transformation | [fpf-core/transformation/index.md](fpf-core/transformation/index.md) | planning tasks, executing work |
| Reasoning | [fpf-core/reasoning/index.md](fpf-core/reasoning/index.md) | problem-solving, hypothesis generation |
| Trust & Evidence | [fpf-core/trust-evidence/index.md](fpf-core/trust-evidence/index.md) | evaluating claims, reliability |
| Aggregation | [fpf-core/aggregation/index.md](fpf-core/aggregation/index.md) | combining parts, emergence |
| Signature | [fpf-core/signature/index.md](fpf-core/signature/index.md) | interface design, boundaries |
| Architheories | [fpf-core/architheories/index.md](fpf-core/architheories/index.md) | domain-specific calculi |
| Constitution | [fpf-core/constitution/index.md](fpf-core/constitution/index.md) | FPF rules and constraints |
| Unification | [fpf-core/unification/index.md](fpf-core/unification/index.md) | cross-domain integration |
| Ethics | [fpf-core/ethics/index.md](fpf-core/ethics/index.md) | ethical considerations |
| SOTA | [fpf-core/sota/index.md](fpf-core/sota/index.md) | benchmarks, discipline packs |

Full index: [fpf-core/index.md](fpf-core/index.md)

## Key Patterns (Quick Reference)

Most frequently needed patterns:

| Pattern | Domain | Use for |
|---------|--------|---------|
| A.1 | foundations | Understanding entity composition (holons) |
| A.7 | foundations | Avoiding category errors (Strict Distinction) |
| A.3 | transformation | Method/Work distinction (Transformer Quartet) |
| A.15 | transformation | Role-Method-Work alignment |
| B.5 | reasoning | Canonical reasoning cycle |
| A.10 | trust-evidence | Evidence chains (Evidence Graph) |
| B.3 | trust-evidence | Trust calculus (F-G-R) |
| B.1 | aggregation | Composition (Gamma operator) |

## Usage Guidelines

1. **Before starting any task**: Search for relevant patterns
2. **When planning**: Reference specific pattern IDs in your reasoning
3. **When uncertain**: Load domain index, then specific pattern
4. **When executing**: Distinguish clearly between what you plan vs what you do
