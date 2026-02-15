---
name: fpf
description: First Principles Framework - structured reasoning skill for any task requiring auditable thinking, evidence chains, systematic problem-solving, or holonic composition. Use FPF patterns to guide reasoning on engineering, research, and management tasks.
priority: high
auto_load: true
---

# FPF Skill

FPF is a first-principles pattern language for systems, epistemes, and collective thinking: generative patterns with assurance (evidence, formality, audit trail) and open-ended evolution (creativity, abductive loop, explore–exploit).

## How to use this skill

1. **Identify** the user’s task or question (concept, keyword, or natural-language query).
2. **Find pattern IDs** using the indexes (load only what you need):
   - By question → [reference/agent_index_queries.md](reference/agent_index_queries.md)
   - By keyword → [reference/agent_index_keywords.md](reference/agent_index_keywords.md)
   - By ID/title and dependencies → [reference/agent_index_patterns.md](reference/agent_index_patterns.md)
3. **Resolve dependencies:** In agent_index_patterns, column **Builds on** lists pattern IDs that must be loaded before this one. For pattern X, load every ID in “Builds on” (recursively if needed), then load X.
4. **Load pattern bodies** from `reference/fpf-patterns/<ID>.md` (e.g. `reference/fpf-patterns/A.1.md`). Batch multiple files when several patterns are needed.
5. **Optional:** For high-level context (roles, creativity vs assurance, OWA/CWA), load [reference/intro_preface_non-normative.md](reference/intro_preface_non-normative.md).

Do not load all 204 patterns at once; load on demand via the indexes and dependency order.
