---
name: fpf
description: First Principles Framework - structured reasoning skill for any task requiring auditable thinking, evidence chains, systematic problem-solving, or holonic composition. Use FPF patterns to guide reasoning on engineering, research, and management tasks.
priority: high
auto_load: true
---

# FPF Thinking Skill

FPF is an "Operating System for Thought" - a rigorous architecture for thinking that ensures auditable reasoning, evidence-based decisions, and clear distinction between plans and execution.

## Paths and how to load patterns

- **Base path**: Paths written as `references/...` are relative to the directory that contains this SKILL.md (the **skill root**). When the skill is loaded from the project (e.g. repo FPF), skill root is `skills/fpf`. When loaded globally, skill root is the skill folder. Use the same base for all `references/` links.
- **Loading patterns**: To find pattern IDs quickly, use one of:
  - [Agent index: query → pattern ID](references/agent_index_queries.md) — match natural-language questions to pattern IDs.
  - [Agent index: keyword → pattern IDs](references/agent_index_keywords.md) — match task vocabulary to keywords.
  - [FPF pattern index (ID, Title, Dependencies)](references/agent_index_patterns.md) — browse by ID or title; load order via Builds on.
  Then read the pattern body from `references/fpf-patterns/<ID>.md` (e.g. `references/fpf-patterns/A.1.md`). **Batch** multiple pattern files in one step when loading several.

## Start Here

**Agent Entry**

- [FPF specification preface](references/intro_preface_non-normative.md)
- [FPF Table Of Contents](references/intro_table_of_content.md) — full index: pattern IDs, Keywords & Search Queries, Dependencies.
- For fast lookup: [keyword index](references/agent_index_keywords.md) | [query index](references/agent_index_queries.md) | [pattern index (ID, Title, Builds on)](references/agent_index_patterns.md).

**При первом применении скилла**

1. Прочитать этот SKILL.md полностью (включая Pattern Selection Logic и Critical Disciplines).
2. По запросу пользователя определить тип задачи по таблице Pattern Selection Logic выше.
3. Выбрать 3–5 паттернов: по индексам (keyword/query) или по Table of Content; при необходимости уточнить зависимости в ToC.
4. Загрузить выбранные `references/fpf-patterns/<ID>.md` одним батчем.
5. Строить рассуждение и план, ссылаясь на загруженные паттерны по ID; при необходимости подгружать ещё.

## Pattern Selection Logic

**Start here to find the right patterns for your task:**

**Modeling & Design:**
- System modeling → **foundations** (A.1 Entity/Holon, A.2 Roles) → **transformation** (A.15 Role-Method-Work)
- Interface design → **signature** (A.6 Signature Stack, A.6.5 Slot Discipline)
- Boundary definition → **signature** (A.6.B Boundary Norms, A.6.C Contract Unpacking)

**Analysis & Evaluation:**
- Reliability/trust evaluation → **trust-evidence** (B.3 F-G-R Calculus, C.2.2 Reliability)
- Evidence validation → **trust-evidence** (A.10 Evidence Graph, B.3.4 Evidence Decay)
- Metric design → **architheories** (C.16 Measurement, A.18 CSLC)

**Problem-Solving:**
- Creative ideation → **reasoning** (B.5.2 Abductive Loop, C.17 Creativity-CHR)
- Systematic reasoning → **reasoning** (B.5 Canonical Reasoning Cycle)
- Conflict resolution → **ethics** (D.5 Bias-Audit)

**Composition & Integration:**
- Combining parts → **aggregation** (B.1 Gamma Operator, B.2 Meta-Holon Transition)
- Cross-domain mapping → **unification** (F.9 Bridges, F.7 Concept-Set Table)
- Method composition → **aggregation** (B.1.5 Γ_method)

**Process & Execution:**
- Task planning → **transformation** (A.15.2 WorkPlan, A.3.2 MethodDescription)
- Work execution → **transformation** (A.15.1 Work, A.3 Transformer Quartet)
- State modeling → **foundations** (A.2.5 RoleStateGraph, A.19 CharacteristicSpace)

## Core Workflow (B.5 Canonical Reasoning Cycle)

For every task:

1. **OBSERVE**: Understand request → identify task type above
2. **SEARCH**: Pick pattern IDs via [keyword index](references/agent_index_keywords.md), [query index](references/agent_index_queries.md), [pattern index](references/agent_index_patterns.md), or [Table of Content](references/intro_table_of_content.md) (for full metadata)
3. **LOAD**: Read pattern file `references/fpf-patterns/<ID>.md` for each ID (e.g. `A.1.md`, `B.5.md`). Batch multiple reads in one step when loading several patterns.
4. **PLAN**: Reference pattern IDs in reasoning (MethodDescription)
5. **EXECUTE**: Deploy plan (Work), maintain strict Object≠Description distinction (A.7)
6. **AUDIT**: Log evidence chains (A.10), reference source patterns

**Agent workflow checklist**

| Step | Check |
|------|--------|
| OBSERVE | Task type identified from Pattern Selection Logic (modeling / analysis / problem-solving / composition / process)? |
| SEARCH | Pattern IDs chosen from index or ToC; dependencies checked in ToC if needed? |
| LOAD | Pattern files read in batch; Starter (A.1, A.7, A.10) included when relevant? |
| PLAN | Reasoning cites pattern IDs; MethodDescription vs Work distinction clear? |
| EXECUTE | Object≠Description (A.7); Role≠Work; no category errors? |
| AUDIT | Claims linked to evidence; source patterns referenced? |

## Navigation Hub

**Layout:**

- **Discovery (lightweight):** [keyword → IDs](references/agent_index_keywords.md), [query → ID](references/agent_index_queries.md), [pattern index (ID, Title, Builds on)](references/agent_index_patterns.md). Use for fast lookup.
- **[Table of Content](references/intro_table_of_content.md)** — canonical index: pattern IDs, titles, **Keywords & Search Queries**, **Dependencies**. Use when you need full metadata or dependency graph.
- **Pattern bodies** live in `references/fpf-patterns/<ID>.md` (e.g. `A.1.md`, `B.3.md`).

Domain groupings (foundations, transformation, reasoning, trust-evidence, aggregation, signature, architheories, constitution, unification, ethics, sota) appear in the Table of Content. Find patterns by keyword/query or by section; open the corresponding `<ID>.md` for the full pattern body.

## Starter Patterns

**Must-read for any FPF usage:**
- **A.1** - Holonic Foundation (entity composition)
- **A.7** - Strict Distinction (avoid category errors: Object≠Description, Role≠Work)
- **A.10** - Evidence Graph (traceability)

**Most common by domain** (see [pattern index](references/agent_index_patterns.md) or [Table of Content](references/intro_table_of_content.md)):
- foundations: A.1, A.2, A.7
- transformation: A.3, A.15, A.15.1 (Work)
- reasoning: B.5, B.5.2 (Abduction)
- trust-evidence: B.3, A.10
- aggregation: B.1, B.2
- signature: A.6, A.6.5

## Critical Disciplines

**Always apply:**
- **Strict Distinction (A.7)**: Object ≠ Description ≠ Carrier; Role ≠ Work; Method ≠ MethodDescription
- **Evidence chains (A.10)**: Every claim needs evidence reference
- **Scope discipline (A.2.6)**: Explicit context boundaries
- **Role-Method-Work alignment (A.15)**: Clear separation of intent, plan, execution

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

### Search keywords

For **keyword lookup** use [agent_index_keywords.md](references/agent_index_keywords.md). For **question-style lookup** use [agent_index_queries.md](references/agent_index_queries.md). Methodology terms that map to patterns include:

```
holon, system, episteme, role, method, work, trust, evidence,
transformer, reliability, aggregation, assurance, reasoning,
budget, context, deduction, induction, abduction, formality,
evolution, agent
```

**Important:** Do not search for task-topic words (e.g. "AI agents", "web search"). FPF is a methodology, not a knowledge base about your task topic.
