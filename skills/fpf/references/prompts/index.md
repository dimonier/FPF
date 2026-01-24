# FPF Prompt Templates

Ready-to-use prompt templates for common FPF tasks. Load these templates when you need structured guidance for specific use cases.

## Quick Template Selection

**Choose template based on your need:**

**Core Workflow:**
- **Need guidance on FPF process?** → [workflow.md](workflow.md) (mandatory workflow)
- **Need pattern references?** → [principles.md](principles.md) (essential patterns)
- **Need navigation help?** → [keywords.md](keywords.md) (domain/keyword guide)
- **Need task template?** → [initial-plan.md](initial-plan.md) (execution plan)

**Project Work:**
- **Starting new project?** → [characterisation.md](characterisation.md) (define metrics)
- **Need architecture map?** → [p2w.md](p2w.md) (principles to work)

**Terminology:**
- **Standardizing vocabulary?** → [uts.md](uts.md) (unified term sheets)
- **Naming problems?** → [naming.md](naming.md) (F.18 name cards)

**Advanced:**
- **Surveying discipline?** → [sota.md](sota.md) (state-of-the-art harvesting)

---

## Prompts by Category

### Workflow & Navigation (4 prompts)

**[workflow.md](workflow.md)** - Mandatory FPF Reasoning Workflow
- **Use for:** Every FPF task (step-by-step reasoning process)
- **Contains:** 4-step workflow (language detection, FPF decomposition, reasoning, translation)
- **Related patterns:** B.5 (Reasoning Cycle), A.7 (Strict Distinction), A.10 (Evidence Graph)

**[principles.md](principles.md)** - Core Pattern Quick Reference
- **Use for:** Looking up essential FPF patterns without loading full domains
- **Contains:** A.7, A.10, B.3, B.5 + additional key patterns (F.17, F.18, E.18, G.2)
- **Related domains:** foundations, trust-evidence, reasoning, unification, sota

**[keywords.md](keywords.md)** - Domain Navigation & Keyword Guide
- **Use for:** Finding domains by task type, keyword search reference
- **Contains:** Domain navigation table, core/prompt-specific keywords, task-specific shortcuts
- **Related:** All domain indexes

**[initial-plan.md](initial-plan.md)** - Standard Task Execution Template
- **Use for:** Structuring task decomposition and execution planning
- **Contains:** 4-step plan template (language, FPF analysis, template check, execution)
- **Related:** workflow.md, all task-specific prompts

### Project & Design (2 prompts)

**[characterisation.md](characterisation.md)** - Project Metrics & Indicators
- **Use for:** Converting vague ideas into measurable characteristics and decision criteria
- **Contains:** Goal, prompt template, follow-ups, related patterns (C.16, A.18, E.TGA)
- **When:** Starting projects, defining dashboards, establishing KPIs

**[p2w.md](p2w.md)** - Principles-to-Work (E.TGA) Flows
- **Use for:** Making "from principles to work" explicit, tracing decision rationale
- **Contains:** P2W prompt template, flow specification, node types (P/D/R/M/W)
- **Related patterns:** E.TGA (E.18), TEVB (E.17.2), B.4 (Evolution), A.15 (Work)

### Terminology & Naming (2 prompts)

**[uts.md](uts.md)** - Unified Term Sheet (UTS) Generation
- **Use for:** Building disciplined vocabulary, standardizing terminology across domains
- **Contains:** UTS prompt template, structure guide (Tech/Plain names, SenseCells, aliases)
- **Related patterns:** F.17 (UTS), F.18 (Naming), F.7 (Concept-Set), F.3 (Sense Clustering)

**[naming.md](naming.md)** - Name Card Development (F.18)
- **Use for:** Designing better names when existing labels are misleading
- **Contains:** Naming prompt, Name Card components, anti-patterns to avoid
- **Related patterns:** F.18 (Naming Protocol), F.17 (UTS), F.5 (Naming Discipline)

### Advanced (1 prompt)

**[sota.md](sota.md)** - SoTA Harvesting & Discipline Packs
- **Use for:** Surveying state-of-the-art, comparing methodologies, building knowledge packs
- **Contains:** SoTA prompt template, TraditionCards, OperatorCards, selector portfolio
- **Related patterns:** G.2 (SoTA Harvester), G.4 (CAL Authoring), G.0 (Frame Standard)

---

## Usage Pattern

**Typical progression:**
1. Start with [workflow.md](workflow.md) for overall process
2. Check [keywords.md](keywords.md) or [principles.md](principles.md) for navigation
3. Select task-specific template (characterisation, uts, naming, p2w, sota)
4. Adapt template to your context
5. Follow [workflow.md](workflow.md) execution steps

**Cross-references:**
- All prompts reference each other in "See Also" sections
- All prompts link to relevant FPF patterns in [../fpf-patterns/](../fpf-patterns/)
- Core terminology included in main SKILL.md

---

## Maintenance

These prompts are **reference materials** following Agent Skills spec progressive disclosure:
- Load on-demand (not bundled with main SKILL.md)
- Keep focused and concise
- Update when FPF patterns evolve
- Cross-link to maintain navigation consistency
