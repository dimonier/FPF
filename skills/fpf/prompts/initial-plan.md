# FPF Initial Execution Plan

This template defines the standard execution plan for any task.
The plan is loaded at task start and evolves during execution.

## Steps

1. **Detect language** (phase: DECOMPOSE)
   - Identify user's language from request
   - Expected: Language code (en, ru, etc.)

2. **FPF Analysis** (phase: DECOMPOSE)
   - Map request to FPF concepts (Holons, BoundedContexts, Roles, Method, Work)
   - Navigate to relevant domain index:
     - Understanding entities? → `fpf-core/foundations/index.md`
     - Planning/execution? → `fpf-core/transformation/index.md`
     - Problem-solving? → `fpf-core/reasoning/index.md`
     - Evaluating claims? → `fpf-core/trust-evidence/index.md`
     - Combining parts? → `fpf-core/aggregation/index.md`
   - Load specific patterns from domain as needed
   - Expected: FPF mapping and pattern IDs (B.5, A.10, etc.)

3. **Execute task** (phase: EXECUTE, expandable: true)
   - Placeholder - will be expanded after decomposition
   - Expected: Task-specific actions
