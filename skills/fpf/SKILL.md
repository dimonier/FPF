---
name: fpf
description: First Principles Framework - structured reasoning for auditable thinking, evidence chains, audit trail, systematic problem-solving, or holonic composition. Use when the task requires reasoning, first-principles decomposition, or FPF terms (holon, role, episteme, Bounded Context, signature, assurance). Skip when the user asks for quick code-only fixes, single-file syntax/typo/import only, or work in domains unrelated to systems/knowledge/organisation.
priority: high
auto_load: true
---

# FPF Skill

FPF is a first-principles pattern language for systems, epistemes, and collective thinking: generative patterns with assurance (evidence, formality, audit trail) and open-ended evolution (creativity, abductive loop, explore–exploit).

## When to use / When to skip

- **Use when:** The task requires first-principles decomposition, evidence chains, audit trail, or uses FPF terms (holon, role, episteme, Bounded Context, signature, assurance). The user asks "how does FPF…", "what is [FPF concept]…", or for systematic reasoning on engineering, research, or management.
- **Skip when:** The user asks for quick code-only fixes, single-file syntax/typo/import only, or work in domains unrelated to systems/knowledge/organisation. No need to load indexes for one-off questions that do not reference FPF.


## How to use this skill

**Path base:** Always use paths relative to the skill root. Skill root = directory containing this SKILL.md (e.g. from repo root, pattern path is `skills/fpf/reference/fpf-patterns/A.1.md`). Example: `reference/agent_index_queries.md`, `reference/fpf-patterns/A.1.md`.

**Entry point (pick exactly one):**
- User gave a pattern ID (e.g. A.1, B.3.4) → agent_index_patterns.md
- User asked "how…", "what is…", "how do I…" (natural language) → agent_index_queries.md
- User used a domain term (holon, evidence, role, aggregation, …) → agent_index_keywords.md

Do not open a second index until you have ID(s) and need to resolve Builds on.

**Quick flow:** Identify task → pick one index (queries / keywords / patterns) → get pattern ID(s) → resolve Builds on → load `reference/fpf-patterns/<ID>.md` in batches of 5–8 → answer.

1. **Identify** the user’s task or question (concept, keyword, or natural-language query).
2. **Choose one index first** (load only one; use other indexes only to resolve dependencies or related IDs). When using agent_index_patterns, search for the target ID(s) and their Builds on rows; you do not need to load the entire index if the file is large.
   - **Known pattern ID** → [reference/agent_index_patterns.md](reference/agent_index_patterns.md) (find ID, read Builds on), then load pattern bodies.
   - **Natural-language question / "How do I…"** → [reference/agent_index_queries.md](reference/agent_index_queries.md), match by topic, get ID(s); if needed, check agent_index_patterns for Builds on.
   - **Domain term / keyword** (e.g. holon, evidence, role, aggregation) → [reference/agent_index_keywords.md](reference/agent_index_keywords.md), get ID(s); if needed, check agent_index_patterns for Builds on.
3. **Resolve dependencies:** In agent_index_patterns, column **Builds on** lists pattern IDs that must be loaded before this one. In Builds on: expand ranges (e.g. C.17–C.19 → C.17, C.18, C.19). Entries like "Part C (CHR)" or "Kind-CAL (C.3)" are not file names — resolve them to concrete IDs in agent_index_patterns and load those files. Algorithm: (1) Collect target ID(s) and all IDs from Builds on; (2) Expand ranges; (3) Recursively add Builds on for each ID; (4) Order topologically (dependents after dependencies); (5) Load in batches of 5–8 files. If the dependency set is large (e.g. >10), load kernel patterns (Builds on = —) and the target pattern first; load others only if the answer requires them. 
4. **Load pattern bodies** from `reference/fpf-patterns/<ID>.md` (e.g. `reference/fpf-patterns/A.1.md`). Load in batches of 5–8 files (prefer 5 when context is limited, 8 when the answer needs the full dependency chain). If a pattern file is missing, state which ID is missing, and answer from the index (title, Builds on) and Core Terminology only; do not invent pattern content.
5. **Optional:** For high-level context (roles Engineer/Researcher/Manager, creativity vs assurance, OWA/CWA), load [reference/intro_preface_non-normative.md](reference/intro_preface_non-normative.md) only when the task involves framing, epistemology, or explaining FPF to someone; skip for narrow pattern lookups.

**Example:** User asks "How does FPF model creative thinking?" → Open agent_index_queries.md → match "How does FPF model creative thinking? Abductive loop?" → ID **B.5.2**. In agent_index_patterns, B.5.2 builds on B.5. Load `reference/fpf-patterns/B.5.md`, `reference/fpf-patterns/B.5.2.md` (add B.5.2.1, C.17, C.18, C.19 only if the answer needs them). Answer from the loaded patterns and Core Terminology.

Do not load all 204 patterns at once; load on demand via the indexes and dependency order.

If the user asks only for a definition of a term that appears in the Core Terminology tables below (e.g. "What is a holon?", "What is Bounded Context?"), answer from the table only; do not load index or pattern files. For reasoning steps, examples, cross-references, or dependency-aware answers, load the pattern(s) via the indexes.

## Core Terminology

Essential FPF terms for decomposition and reasoning.

### Ontological Core (Part A)

| Term | Pattern | Definition |
|------|---------|------------|
| **Holon** | A.1 | Entity that is simultaneously a whole AND a part. Everything in FPF is a holon. |
| **BoundedContext** | A.1.1 | Semantic frame where terms have meaning. Meaning is LOCAL to context. |
| **System** | A.1 | Physical/digital entity that can bear roles and execute work. |
| **Role** | A.2 | A mask/identity that a System wears. Role != behavior. |
| **RoleAssignment** | A.2.1 | Links a System to a Role within a BoundedContext. |
| **MethodDescription** | A.3.2 | Design-time recipe (plan/algorithm/SOP). Lives in T^D (design-time). NOT execution. |
| **Method** | A.3.1 | Instantiated MethodDescription ready for execution. |
| **Work** | A.15.1 | Run-time occurrence. Actual execution that happened. Dated, consumes resources. IMMUTABLE. |
| **Transformer** | A.12 | Agent that takes input and produces output. External = tool. Reflexive = self-modification. |
| **Episteme** | A.0 | Knowledge artifact with carriers (files, models, beliefs). |

### Core Principles (Part A)

| Principle | Pattern | Definition |
|-----------|---------|------------|
| **Strict Distinction** | A.7 | Map != Territory. Never confuse plan with execution. MethodDescription != Work. |
| **Evidence Graph** | A.10 | All claims need auditable evidence chains. Cite sources. |
| **Ontological Parsimony** | A.11 | Do not multiply entities beyond necessity. |
| **Cross-Scale Consistency** | A.9 | Rules apply at all scales (micro to macro). |

### Reasoning (Part B)

| Term | Pattern | Definition |
|------|---------|------------|
| **Aggregation (Gamma)** | B.1 | How parts combine into wholes. Multiple types: Gamma_sys, Gamma_epist, Gamma_work. |
| **Trust Calculus (F-G-R)** | B.3 | Formality (how rigorous), Granularity/Scope (how broad), Reliability (how trustworthy). |
| **Evidence Decay** | B.3.4 | Evidence loses reliability over time. Epistemic debt accumulates. |
| **Canonical Evolution Loop** | B.4 | OBSERVE -> REFINE -> DEPLOY -> AUDIT cycle. |
| **Canonical Reasoning Cycle** | B.5 | Abduction (hypothesis) -> Deduction (predict) -> Induction (test). |
| **Abduction** | B.5.2 | Generate hypotheses from observations. Creative inference. |
| **Deduction** | B.5 | Derive conclusions from premises. Logical necessity. |
| **Induction** | B.5 | Generalize from specific cases. Probabilistic. |

## Checklist (before answering, verify)

- Input type is determined (question / keyword / pattern ID).
- One starting index was chosen; extra indexes were not loaded.
- Dependencies were resolved; if the set was large, only needed patterns or kernel + target were loaded.
- All file paths are relative to the skill root (e.g. `reference/fpf-patterns/A.1.md`).
