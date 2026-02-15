# Agent index: Query → Pattern ID

Use this file for fast pattern lookup by natural-language question. Canonical metadata and dependencies: [intro_table_of_content.md](intro_table_of_content.md). Pattern bodies: `fpf-patterns/<ID>.md`.

## How to use

1. Match the user's question or your internal question to a query below (by similarity).
2. Use the pattern ID to load `fpf-patterns/<ID>.md`; load multiple IDs in one batch when relevant.
3. For dependencies and related patterns, check the Table of Content.

## Query → Pattern ID

| Query (representative) | Pattern ID |
|------------------------|------------|
| How does FPF model a system and its parts? What is a holon? | A.1 |
| What is a Bounded Context? How to define rules for a project? | A.1.1 |
| How to model responsibilities? Role vs function? | A.2 |
| How to formally assign a role? | A.2.1 |
| What is a capability in FPF? Ability vs permission? | A.2.2 |
| Promise content vs Work vs MethodDescription? SLO/SLA? | A.2.3 |
| How does an episteme serve as evidence? | A.2.4 |
| How to model the state of a role? Role State Graph? | A.2.5 |
| How to define scope of a claim or capability? What is G in F-G-R? | A.2.6 |
| Role algebra, Separation of Duties, role bundles? | A.2.7 |
| How to represent MUST/SHALL? Deontic commitment? | A.2.8 |
| How to model approvals/authorizations as Work? | A.2.9 |
| How does FPF model an action or change? Transformer quartet? | A.3 |
| What is a Method in FPF? Method vs Work? | A.3.1 |
| How to document a procedure? What is MethodDescription? | A.3.2 |
| How to model state transitions or dynamics? | A.3.3 |
| How does FPF handle plan vs reality? Systems updated? | A.4 |
| What is the architecture of FPF? New domains? | A.5 |
| What is the Signature Stack? Route boundary statements? | A.6 |
| Boundary Norm Square? Decompose gate/duty/evidence? | A.6.B |
| How to unpack contract language? Contract soup? | A.6.C |
| What is universal signature block? Laws vs implementations? | A.6.0 |
| How to define a mechanism (USM/UNM)? Operational guards? | A.6.1 |
| Effect-free episteme morphisms? Transform descriptions? | A.6.2 |
| How to define a view without adding new claims? EpistemicViewing? | A.6.3 |
| How to change object-of-talk without losing truth? Retargeting? | A.6.4 |
| What is A.6.P? Under-specified relations, RPR? | A.6.P |
| How do I declare positions and references in relations? Slot discipline? | A.6.5 |
| What is BaseDeclarationDiscipline? SWBD? | A.6.6 |
| What is MechSuiteDescription? Suite obligations? | A.6.7 |
| How to unpack service talk? RPR-SERV? | A.6.8 |
| How to disambiguate same across contexts? Bridge? | A.6.9 |
| Signature engineering, TargetSignature vs ConstructorSignature? | A.6.S |
| How to unpack whole/part/integrity? RPR-WHOLE? | A.6.H |
| How to avoid modeling mistakes? Core distinctions? | A.7 |
| How does FPF ensure concepts are universal? | A.8 |
| How do rules compose across scales? Aggregate metrics? | A.9 |
| How are claims supported by evidence? Auditability? | A.10 |
| How does FPF avoid becoming too complex? New concepts? | A.11 |
| How to model self-healing? External transformer? | A.12 |
| How is agency modeled? Agency spectrum? | A.13 |
| How to model part-of relationships? ComponentOf, PortionOf? | A.14 |
| How do roles, methods, and work connect? Enactment? | A.15 |
| What is a Work record? Where are resource costs? | A.15.1 |
| How to model a plan or schedule? WorkPlan vs MethodDescription? | A.15.2 |
| What is SlotFillingsPlanItem? Planned slot filling? | A.15.3 |
| How to measure formality? F0-F9 levels? | A.16 |
| What is the term for a measurable property? Define a metric? | A.17 |
| What is CSLC? Comparable measurements? | A.18 |
| How to define state space? Model change over time? | A.19 |
| What is CN-frame? CN-Spec, comparability? | A.19.CN |
| What is CHRMechanismSuite? CN-Spec/CG-Spec? | A.19.CHR |
| What is UNM? Normalize coordinate values? | A.19.UNM |
| What is UINDM? How does FPF choose indicators? | A.19.UINDM |
| What is USCM? Lawful scoring? | A.19.USCM |
| What is ULSAM? Lawful aggregation, Γ-fold? | A.19.ULSAM |
| What is CPM? Compare two profiles? | A.19.CPM |
| What is SelectorMechanism? Portfolio set, thresholds? | A.19.SelectorMechanism |
| What is ConstraintValidity? Eulerian stance? | A.20 |
| What is GateProfilization? OperationalGate, GateChecks? | A.21 |
| How does FPF combine parts into a whole? Gamma operator? | B.1 |
| What is the input for Gamma? Aggregation invariants? | B.1.1 |
| How to aggregate physical systems? Conservation laws? | B.1.2 |
| How to combine knowledge artifacts? Trust propagation? | B.1.3 |
| How does FPF handle time-series? Order-sensitive composition? | B.1.4 |
| How to combine methods or workflows? | B.1.5 |
| How to calculate total cost? Resources aggregated? | B.1.6 |
| How does FPF model emergence? Meta-Holon Transition? | B.2 |
| What triggers an MHT? BOSC criteria? | B.2.1 |
| How do new systems emerge? Meta-System Transition? | B.2.2 |
| How do new theories emerge? Meta-Epistemic Transition? | B.2.3 |
| How do new capabilities emerge? Meta-Functional Transition? | B.2.4 |
| How does FPF model control systems? Supervisor-subholon? | B.2.5 |
| How is trust calculated? F-G-R model? Evidence and confidence? | B.3 |
| How are F, G, R measured? Epistemic spaces? | B.3.1 |
| Logic for validating claims? Verification vs validation? | B.3.2 |
| What are assurance levels? Artifact maturity? | B.3.3 |
| How does FPF handle outdated evidence? Epistemic debt? | B.3.4 |
| How are models grounded in evidence? CT2R-LOG? | B.3.5 |
| How do systems evolve? Canonical evolution loop? | B.4 |
| How are physical systems updated? | B.4.1 |
| How are theories refined? Knowledge evolution? | B.4.2 |
| How do workflows evolve? Method instantiation? | B.4.3 |
| How does FPF model problem-solving? Reasoning cycle? | B.5 |
| What are development stages? Explore, Shape, Evidence, Operate? | B.5.1 |
| How does FPF model creative thinking? Abductive loop? | B.5.2 |
| How to generate creative ideas? NQD in FPF? | B.5.2.1 |
| How does FPF integrate domain-specific language? Role-Projection Bridge? | B.5.3 |
| How to use CHR patterns? | B.6 |
| How to apply formal logic in FPF? | B.7 |
| How to model physical systems? Conservation laws? | C.1 |
| What is F-G-R? Evidence and trust? Scientific theory? | C.2 |
| What is an episteme? Slot graph, views? | C.2.1 |
| What is R in F-G-R? Reliability propagation? Bridge-only reuse? | C.2.2 |
| What are formality levels? Rigor of a specification? | C.2.3 |
| How does FPF handle types? What is a Kind? | C.3 |
| What is U.Kind? Model is-a relationships? | C.3.1 |
| How to define meaning of a Kind? Intent vs extent? | C.3.2 |
| How to map types between domains? KindBridge? | C.3.3 |
| How to adapt a Kind for local context? RoleMask? | C.3.4 |
| Abstraction tiers for Kinds? K0-K3? | C.3.5 |
| How to write a typed guard? Kinds and USM in gates? | C.3.A |
| How to model a process or workflow? MethodDescription? | C.4 |
| How does FPF model resource usage? Track costs? | C.5 |
| What is the base logic of FPF? Formal proofs? | C.6 |
| How to define a new measurable property? CHR pattern? | C.7 |
| How to measure autonomy? What defines an agent? | C.9 |
| How to model norms and constraints? Ethics? | C.10 |
| How does FPF model decision-making? Preferences? | C.11 |
| How are changes to kinds managed? | C.12 |
| How does FPF construct parts and wholes? Compose-CAL? | C.13 |
| How to model system-of-systems? Infrastructure? | C.14 |
| How to model a field of science? | C.15 |
| How do I define a measurement template? MM-CHR? | C.16 |
| How does FPF measure creativity? Novel idea? | C.17 |
| How does FPF support brainstorming? NQD search? | C.18 |
| How to make search scale-savvy? Scale variables? | C.18.1 |
| How to balance exploration and exploitation? E/E-LOG? | C.19 |
| Bitter Lesson Preference? General method vs heuristic? | C.19.1 |
| How to compose and assess a discipline? | C.20 |
| How to measure health of a scientific field? | C.21 |
| How does FPF type problems? TaskSignature? | C.22 |
| How is method family maturity assessed? SoS-LOG? | C.23 |
| How to sequence tool calls? Agent-Tools-CAL? | C.24 |
| How to model -ilities (availability, reliability)? Q-Bundle? | C.25 |
| Does FPF have built-in ethics? Value systems? | D.1 |
| How to apply ethics at different scales? | D.2 |
| How to model conflicts between systems? | D.3 |
| How does FPF resolve conflicts using trust? Mediation? | D.4 |
| How does FPF handle bias? Bias-Audit Cycle? Ethical assurance? | D.5 |
| What is FPF? Purpose, scope? | E.1 |
| What are the core principles? Eleven pillars? | E.2 |
| How does FPF resolve conflicting principles? Hierarchy? | E.3 |
| How are FPF documents structured? Core vs tooling? | E.4 |
| What are the main architectural constraints? Guardrails? | E.5 |
| Can I use CI/CD terms in FPF core? Lexical firewall? | E.5.1 |
| Does FPF require a specific diagram style? Notation? | E.5.2 |
| What are dependency rules between artifact families? | E.5.3 |
| How does FPF handle bias? Ethics review? | E.5.4 |
| How is the spec structured for learning? On-Ramp? | E.6 |
| How are patterns explained? Archetypes? | E.7 |
| How to write a new FPF pattern? Style guide? | E.8 |
| How are changes to FPF managed? DRR? | E.9 |
| What is the complete set of FPF naming rules? LEX-BUNDLE? | E.10 |
| What do prefixes U., Γ_ mean? | E.10.P |
| What is the formal meaning of Context? | E.10.D1 |
| Description vs specification in FPF? I/D/S? | E.10.D2 |
| How does FPF ensure understandability? So What test? | E.12 |
| How does FPF ensure solutions are useful? MVE? | E.13 |
| What is the main interface for FPF users? Working model? | E.14 |
| How are FPF patterns authored and evolved? LAT? | E.15 |
| How is autonomy bounded and tested? Overrides, SoD? | E.16 |
| How to organise multiple descriptions? Viewpoints, views? | E.17.0 |
| How to define reusable viewpoint bundles? | E.17.1 |
| What are canonical engineering viewpoints? TEVB? | E.17.2 |
| How to publish morphisms? Plain/Tech/Interop/Assurance views? | E.17 |
| What is E.TGA? Gates, bridges, flows? | E.18 |
| How to review a new pattern? Refresh stale patterns? PQG/PCP? | E.19 |
| How to introduce a new mechanism? MIP? | E.20 |
| How does FPF handle ambiguity? Local meaning? | F.0.1, F.1 |
| How to extract terminology? Lexical unit? | F.2 |
| How to group similar terms? SenseCell? | F.3 |
| How to define a role? Role Description? Role states? | F.4 |
| What are naming rules for roles and U.Types? | F.5 |
| What is the process for assigning a role? Six steps? | F.6 |
| How do I create a concept-set table? Compare concepts? | F.7 |
| When should I create a new U.Type? Avoid type explosion? | F.8 |
| How do I bridge concepts across contexts? Alignment? | F.9 |
| How to map status (evidence, standard, requirement)? | F.10 |
| How to align method and work across domains? Method quartet? | F.11 |
| How to bind SLO to actual work? Service acceptance? | F.12 |
| How to manage terminology changes? Deprecation? | F.13 |
| How to prevent too many roles and statuses? | F.14 |
| How is unification validated? SCR/RSCR tests? | F.15 |
| What is the format for a worked example? | F.16 |
| What is the output of unification? UTS? | F.17 |
| What is the formal naming protocol? Name Card? | F.18 |
| How to universalize Part G? RSCR triggers? | G.Core |
| What is CG-Spec? Lawful comparison and aggregation? | G.0 |
| How to author a CG-Frame generator kit? Six-card chassis? | G.1 |
| How does FPF harvest and synthesize SoTA? SoTA Pack? | G.2 |
| How do I author CHR packs for a CG-Frame? CSLC lawful? | G.3 |
| How to author CAL operators and acceptance clauses? | G.4 |
| How does FPF dispatch among MethodFamilies? Portfolios? | G.5 |
| How does FPF trace claims to evidence? EvidenceGraph? | G.6 |
| How to calibrate cross-Tradition bridges? BCT? | G.7 |
| How to package SoS-LOG rules? Maturity ladder? | G.8 |
| What is a parity run? Reproducible benchmark? | G.9 |
| How does FPF ship a SoTA pack? SoTA-Pack(Core)? | G.10 |
| How does FPF keep SoTA packs up-to-date? Refresh, RSCR? | G.11 |
| How to build DHC dashboards? Lawful telemetry? | G.12 |
| How does FPF integrate external indexes? Interop? | G.13 |
