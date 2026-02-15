# Agent index: ID, Title, Builds on

Canonical list of FPF pattern IDs, titles, and load-order dependencies. Pattern bodies: `reference/fpf-patterns/<ID>.md` (relative to skill root). Keywords and queries: [agent_index_keywords.md](agent_index_keywords.md), [agent_index_queries.md](agent_index_queries.md).

## How to use

1. **Find pattern** by ID or title.
2. **Load order:** Column **Builds on** lists pattern IDs to load before this one. To use pattern X: load every ID in "Builds on" (and their dependencies recursively if needed), then load X. Body path: `reference/fpf-patterns/<ID>.md`; batch multiple files when loading several.
3. **Builds on:** "—" = no pattern dependencies (kernel or pillar-only). Entries like "Part C (CHR)" or "Kind-CAL (C.3)" are not file IDs; treat as already covered or see this index. Ranges (e.g. C.17–C.19) are expanded as comma-separated IDs.

## ID | Title | Builds on

| ID | Title | Builds on |
|----|-------|-----------|
| A.0 | Onboarding Glossary (NQD & E/E‑LOG) | E.2, A.5, C.17, C.18, C.19 |
| A.1 | Holonic Foundation: Entity → Holon | — |
| A.1.1 | U.BoundedContext: The Semantic Frame | A.1 |
| A.2 | Role Taxonomy | A.1, A.1.1 |
| A.2.1 | U.RoleAssignment: Contextual Role Assignment | A.2 |
| A.2.2 | U.Capability | A.2 |
| A.2.3 | U.PromiseContent (Promise Content) | A.2.2 |
| A.2.4 | U.EvidenceRole | A.2 |
| A.2.5 | U.RoleStateGraph: The Named State Space of a Role | A.2.1 |
| A.2.6 | Unified Scope Mechanism (USM): Context Slices & Scopes | A.1.1 |
| A.2.7 | U.RoleAlgebra: In-Context Role Relations | A.2 |
| A.2.8 | U.Commitment (Deontic Commitment Object) | A.2.1, A.2.3, A.2.6, A.7, A.15.1 |
| A.2.9 | U.SpeechAct (Communicative Work Object) | A.2.1, A.2.6, A.7, A.10, A.15.1 |
| A.3 | Transformer Constitution (Quartet) | A.2 |
| A.3.1 | U.Method | A.3 |
| A.3.2 | U.MethodDescription | A.3 |
| A.3.3 | U.Dynamics | A.19 |
| A.4 | Temporal Duality & Open-Ended Evolution Principle | — |
| A.5 | Open-Ended Kernel & Extension Layering | — |
| A.6 | Signature Stack & Boundary Discipline | E.8, A.6.0, A.6.1, A.6.3, E.17.0, E.17, A.7, F.18, E.10.D2 |
| A.6.0 | U.Signature — Universal, law‑governed declaration | — |
| A.6.1 | U.Mechanism — Law‑governed application to SubjectKind over BaseType | A.6.0, E.10.D1 |
| A.6.2 | U.EffectFreeEpistemicMorphing | A.1, A.7, A.6.0, A.6.5, E.10.D2, C.2.1 |
| A.6.3 | U.EpistemicViewing | A.6.0, A.6.2, A.6.5, A.7, E.10.D2, C.2.1, C.2 |
| A.6.4 | U.EpistemicRetargeting | A.6.2, A.1, F.9, C.2.1, C.2 |
| A.6.5 | U.RelationSlotDiscipline | A.6.0, A.1, A.7, E.8, E.10 |
| A.6.6 | U.BaseDeclarationDiscipline | A.6.0, A.6.5, A.2.6, A.2.4, A.7, E.8, E.10 |
| A.6.7 | MechSuiteDescription | E.8, A.6.1, A.6.5, E.10, E.19 |
| A.6.8 | Service Polysemy Unpacking (RPR-SERV) | A.6.P, A.6.B, A.6.5, A.2.3, A.2.8, A.2.9, A.15, E.10, F.17, F.18 |
| A.6.9 | U.CrossContextSamenessDisambiguation (RPR-XCTX) | A.6.P, F.9, E.10.D1, A.7 |
| A.6.B | Boundary Norm Square | E.8, A.6.0, A.6.1, A.6.3, E.17.0, E.17, A.7, F.18, E.10.D2 |
| A.6.C | Contract Unpacking for Boundaries | A.6, A.6.B, A.6.8, A.7, A.2.3, A.2.8, A.2.9, E.10, E.17 |
| A.6.H | Wholeness Language Unpacking (RPR-WHOLE) | A.6.P, A.6.5, A.7 |
| A.6.P | U.RelationalPrecisionRestorationSuite (RPR) | A.6, A.6.B, A.6.S, A.6.0, A.6.5, E.8, E.10, F.18 |
| A.6.S | U.SignatureEngineeringPair | A.6.0, A.6.2, A.6.3, A.6.4, A.6.5, A.6.6, A.6.B, A.3, A.7, A.12, C.2.1, E.17, E.10 |
| A.7 | Strict Distinction (Clarity Lattice) | A.1, A.2, A.3 |
| A.8 | Universal Core (C-1) | — |
| A.9 | Cross-Scale Consistency (C-3) | A.1, A.8 |
| A.10 | Evidence Graph Referring (C-4) | A.1 |
| A.11 | Ontological Parsimony (C-5) | — |
| A.12 | External Transformer & Reflexive Split | A.3 |
| A.13 | The Agential Role & Agency Spectrum | A.2 |
| A.14 | Advanced Mereology: Components, Portions, Aspects & Phases | A.1 |
| A.15 | Role–Method–Work Alignment (Contextual Enactment) | A.2, A.3, A.4 |
| A.15.1 | U.Work: The Record of Occurrence | A.15 |
| A.15.2 | U.WorkPlan: The Schedule of Intent | A.15 |
| A.15.3 | SlotFillingsPlanItem | A.15.2, A.6.5, E.10.D1, E.17, E.18, E.19 |
| A.16 | Formality–Openness Ladder (FOL) | A.1 |
| A.17 | A.CHR-NORM — Canonical Characteristic | — |
| A.18 | A.CSLC-KERNEL — Minimal CSLC in Kernel | A.17 |
| A.19 | A.CHR-SPACE — CharacteristicSpace & Dynamics hook | A.17, A.18, A.2.5 |
| A.19.CN | CN-frame (comparability & normalization) | A.19 |
| A.19.CHR | CHRMechanismSuite | A.6.7, A.15.3, A.6.1, A.6.5, A.19, G.0, E.18, E.10, E.19 |
| A.19.CPM | Unified Comparison Mechanism (CPM) | A.19.CN, A.6.1, A.6.5, A.19.CHR, G.0, A.18 |
| A.19.SelectorMechanism | Unified Selection Kernel (SelectorMechanism) | A.6.1, A.6.5, A.19.CHR, A.19.CN, G.0, G.5, C.22 |
| A.19.UINDM | Unified Indicatorization Mechanism (UINDM) | A.19.CN, A.6.1, A.6.5, A.19.CHR |
| A.19.ULSAM | Unified Lawful Scale Aggregation Mechanism (ULSAM) | A.19.CN, G.0, A.18, A.6.1, A.6.5, A.19.CHR, B.3 |
| A.19.UNM | Unified Normalization Mechanism (UNM) | A.19.CN, A.6.1, A.6.5, A.19.CHR, A.17, A.18, C.16, G.0, E.18, E.20, F.18 |
| A.19.USCM | Unified Scoring Mechanism (USCM) | A.19.CN, A.6.1, A.6.5, A.19.CHR, G.0, A.18, C.16 |
| A.20 | U.Flow.ConstraintValidity — Eulerian | E.18 |
| A.21 | GateProfilization: OperationalGate(profile) (GateFit core) | E.18, E.17, A.7 |
| B.1 | Universal Algebra of Aggregation (Γ) | A.1, A.9 |
| B.1.1 | Dependency Graph & Proofs | B.1 |
| B.1.2 | System-specific Aggregation Γ_sys | B.1, A.1, C.1 |
| B.1.3 | Γ_epist — Knowledge-Specific Aggregation | B.1, A.1, C.2 |
| B.1.4 | Contextual & Temporal Aggregation (Γ_ctx & Γ_time) | B.1 |
| B.1.5 | Γ_method — Order-Sensitive Method Composition | B.1, B.1.4, A.3.1 |
| B.1.6 | Γ_work — Work as Spent Resource | B.1, A.15.1, C.5 |
| B.2 | Meta-Holon Transition (MHT) | B.1, A.1 |
| B.2.1 | BOSC Triggers | B.2 |
| B.2.2 | Meta-System Transition (MST) | B.2, B.2.1, A.1 |
| B.2.3 | Meta-Epistemic Transition (MET) | B.2, B.2.1, A.1 |
| B.2.4 | Meta-Functional Transition (MFT) | B.2, B.2.1, A.3.1 |
| B.2.5 | Supervisor–Subholon Feedback Loop | B.2, A.1 |
| B.3 | Trust & Assurance Calculus (F–G–R with Congruence) | A.10 |
| B.3.1 | Components & Epistemic Spaces | B.3 |
| B.3.2 | Evidence & Validation Logic (LOG-use) | B.3, C.6 |
| B.3.3 | Assurance Subtypes & Levels | B.3 |
| B.3.4 | Evidence Decay & Epistemic Debt | B.3 |
| B.3.5 | CT2R-LOG — Working-Model Relations & Grounding | B.3, E.14, C.13 |
| B.4 | Canonical Evolution Loop | A.4, A.12 |
| B.4.1 | System Instantiation | B.4, A.1 |
| B.4.2 | Knowledge Instantiation | B.4, A.1 |
| B.4.3 | Method Instantiation | B.4, A.3.1 |
| B.5 | Canonical Reasoning Cycle | A.10 |
| B.5.1 | Explore → Shape → Evidence → Operate | B.5 |
| B.5.2 | Abductive Loop | B.5 |
| B.5.2.1 | Creative Abduction with NQD | B.5.2, C.17, C.18, C.19 |
| B.5.3 | Role-Projection Bridge | A.2, C.3 |
| B.6 | Characterisation Families (CHR-use) | Part C (CHR) |
| B.7 | Common Logic Suite (LOG-use) | Part C (LOG-CAL) |
| C.1 | Sys-CAL | A.1, A.14 |
| C.2 | KD-CAL (Epistemic holon composition) | A.1, A.10, B.3 |
| C.2.1 | U.Episteme — Epistemes and their slot graph | C.2, A.1, A.6.5, E.10.D2 |
| C.2.2 | Reliability R in the F–G–R triad | C.2, A.2.6, C.2.3, B.3, B.1.3, C.3, F.9 |
| C.2.3 | Unified Formality Characteristic F | C.2 |
| C.3 | Kind-CAL — Kinds, Intent/Extent, and Typed Reasoning | A.1, A.2.6 |
| C.3.1 | U.Kind & U.SubkindOf (Core) | A.1, A.2.6 |
| C.3.2 | KindSignature (+F) & Extension/MemberOf | C.3.1 |
| C.3.3 | KindBridge & CL^k | C.3.1, C.3.2, A.2.6, C.2.2 |
| C.3.4 | RoleMask | C.3.1, C.3.2 |
| C.3.5 | KindAT (K0…K3) | C.3.1 |
| C.3.A | Typed Guard Macros for Kinds + USM (Annex) | C.3.*, A.2.6 |
| C.4 | Method-CAL | A.3, A.15 |
| C.5 | Resrc-CAL | A.15.1 |
| C.6 | LOG-CAL – Core Logic Calculus | Kind-CAL (C.3) |
| C.7 | CHR-CAL – Characterisation Kit | A.17, A.18 |
| C.9 | Agency-CHR | CHR-CAL (C.7), A.13 |
| C.10 | Norm-CAL | A.10 |
| C.11 | Decsn-CAL | A.13 |
| C.12 | ADR-Kind-CAL | Kind-CAL, E.9 |
| C.13 | Compose-CAL — Constructional Mereology | A.14 |
| C.14 | M-Sys-CAL | C.1, B.2.2 |
| C.15 | M-KD-CAL | C.2, B.2.3 |
| C.16 | MM-CHR — Measurement & Metrics Characterization | A.17, A.18 |
| C.17 | Creativity-CHR | C.7, C.16 |
| C.18 | NQD-CAL — Open-Ended Search Calculus | C.2 |
| C.18.1 | SLL — Scaling-Law Lens Binding | C.16, C.17, C.18 |
| C.19 | E/E-LOG — Explore–Exploit Governor | C.11 |
| C.19.1 | BLP — Bitter-Lesson Preference | C.19, C.24 |
| C.20 | Discipline-CAL | C.2, G.0, Part F |
| C.21 | Discipline-CHR — Field Health & Structure | C.16, C.2, A.2.6, B.3 |
| C.22 | Problem-CHR — Problem Typing & TaskSignature | C.16, G.5, G.0 |
| C.23 | Method-SoS-LOG | G.5, G.4, C.22, B.3 |
| C.24 | C.Agent-Tools-CAL | C.5, C.18, C.19, B.3 |
| C.25 | Q-Bundle — Structured Quality Bundles | A.2.6, A.6.1, C.16 |
| D.1 | Axiological Neutrality Principle | E.2 |
| D.2 | Multi-Scale Ethics Framework | D.1, A.9 |
| D.2.1 | Local-Agent Ethics | D.2 |
| D.2.2 | Group-Ethics Standards | D.2 |
| D.2.3 | Ecosystem Stewardship | D.2 |
| D.2.4 | Planetary-Scale Precaution | D.2 |
| D.3 | Holonic Conflict Topology | A.1, B.1 |
| D.3.1 | Conflict Detection Logic (LOG-use) | D.3 |
| D.3.2 | Conflict Routing Protocol | D.3 |
| D.4 | Trust-Aware Mediation Calculus | D.3, B.3 |
| D.4.1 | Fair-Share Negotiation Operator | D.4 |
| D.4.2 | Assurance-Driven Override | D.4 |
| D.5 | Bias-Audit & Ethical Assurance | E.5.4 |
| D.5.1 | Taxonomy-Guided Audit Templates | D.5 |
| D.5.2 | Assurance Metrics Roll-up | D.5, B.3 |
| E.1 | Vision & Mission: Operating System for Thought | — |
| E.2 | The Eleven Pillars | E.1 |
| E.3 | Principle Taxonomy & Precedence Model | E.2 |
| E.4 | FPF Artefact Architecture | E.1 |
| E.5 | Four Guard-Rails of FPF | E.2, E.3 |
| E.5.1 | DevOps Lexical Firewall | E.5 |
| E.5.2 | Notational Independence | E.5 |
| E.5.3 | Unidirectional Dependency | E.5 |
| E.5.4 | Cross-Disciplinary Bias Audit | E.5 |
| E.6 | Didactic Architecture of the Spec | E.2 |
| E.7 | Archetypal Grounding Principle | E.6 |
| E.8 | FPF Authoring Conventions & Style Guide | E.6, E.7 |
| E.9 | Design-Rationale Record (DRR) Method | E.2 |
| E.10 | LEX-BUNDLE: Unified Lexical Rules for FPF | A.7, E.5, F.5 |
| E.10.D1 | Lexical Discipline for Context (D.CTX) | A.7, A.4 |
| E.10.D2 | Intension–Description–Specification (I/D/S) | A.7, E.10.D1, C.2.1, C.2.3 |
| E.10.P | Conceptual Prefixes (policy & registry) | E.9 |
| E.12 | Didactic Primacy & Cognitive Ergonomics | E.2 |
| E.13 | Pragmatic Utility & Value Alignment | E.2 |
| E.14 | Human-Centric Working-Model | E.7, E.8, C.2.3 |
| E.15 | Lexical Authoring & Evolution Protocol (LEX-AUTH) | E.9, E.10, B.4, C.18, C.19, A.10, B.3, F.15 |
| E.16 | RoC-Autonomy Budget & Enforcement | E.8, E.10, C.16, F.8, E.18, A.21 |
| E.17 | Multi-View Publication Kit (MVPK) | A.7, E.10.D2, A.6.2, A.6.3, C.2.1, E.17.0, E.17.1, E.17.2, E.8, E.10 |
| E.17.0 | U.MultiViewDescribing — Viewpoints, Views & Correspondences | C.2.1, A.6.2, A.6.3, A.6.4, A.7, E.10.D1, E.10.D2 |
| E.17.1 | U.ViewpointBundleLibrary | E.17.0, C.2.1, A.6.2–A.6.4, A.7, E.7, E.10 |
| E.17.2 | TEVB — Typical Engineering Viewpoints Bundle | E.17.0, E.17.1, C.2.1, A.1, A.6.2–A.6.4, A.7, E.10.D2 |
| E.18 | Transduction Graph Architecture (E.TGA) | E.17, E.8, E.10, A.7 |
| E.19 | Pattern Quality Gates: Review & Refresh Profiles | E.8, E.10, E.9, E.15 |
| E.20 | Mechanism Introduction Protocol (MIP) | E.8, E.9, E.10, E.15, E.19 |
| F.0.1 | Contextual Lexicon Principles | A.1.1 |
| F.1 | Domain-Family Landscape Survey | E.10.D1, F.0.1, A.7 |
| F.2 | Term Harvesting & Normalisation | F.1 |
| F.3 | Intra-Context Sense Clustering | F.2 |
| F.4 | Role Description (RCS + RoleStateGraph + Checklists) | F.3, A.2.1 |
| F.5 | Naming Discipline for U.Types & Roles | F.4, E.10 |
| F.6 | Role Assignment & Enactment Cycle (Six-Step) | F.4, A.2.1, A.15 |
| F.7 | Concept-Set Table | F.3, F.9 |
| F.8 | Mint or Reuse? | F.4, F.7 |
| F.9 | Alignment & Bridge across Contexts | F.3 |
| F.10 | Status Families Mapping | F.9, B.3 |
| F.11 | Method Quartet Harmonisation | F.9, A.15 |
| F.12 | Service Acceptance–Work Evidence Link | F.9, A.2.3 |
| F.13 | Lexical Continuity & Deprecation | F.5 |
| F.14 | Anti-Explosion Control (Roles & Statuses) | F.4, F.8 |
| F.15 | SCR/RSCR Harness for Unification | F.1–F.14 |
| F.16 | Worked-Example Template (Cross-Domain) | F.1–F.12 |
| F.17 | Unified Term Sheet (UTS) | F.1–F.12 |
| F.18 | Local-First Unification Naming Protocol | F.1–F.5 |
| G.Core | Part G Core Invariants | E.8, E.10, E.19, A.6.7, A.15.3, A.19, G.0, A.19.CHR |
| G.0 | CG-Spec — Frame Standard & Comparability Governance | G.Core, A.19, A.10, A.17–A.19, C.16, A.18, B.3, Part F, E.10, E.5.2 |
| G.1 | CG-Frame-Ready Generator | G.Core, E.8, E.10, E.19, A.10, A.15.3, A.19, G.0, G.2–G.5, G.10, G.11 |
| G.2 | SoTA Harvester & Synthesis | G.Core, E.8, E.10, E.19, A.10, B.3, F.9, F.17, G.0, G.6 |
| G.3 | CHR Authoring for a CG-Frame | G.Core, G.2, G.0, A.17–A.19, A.18, C.16, A.19.CHR, A.15.3, G.6, F.17 |
| G.4 | CAL Authoring for a CG-Frame | G.Core, G.3, G.0, B.3, A.18, G.6 |
| G.5 | Multi-Method Dispatcher & MethodFamily Registry | G.Core, G.0, A.19, G.2, G.3, G.4, G.6 |
| G.6 | Evidence Graph & Provenance Ledger | G.Core, A.10, B.3, G.4, F.9, F.15, F.17, E.18, A.21, E.10, E.5.2 |
| G.7 | Cross-Tradition Bridge Calibration Kit | G.Core, G.2, F.9, F.3, F.7, B.3, G.6, E.18, A.21, E.10, C.21 |
| G.8 | SoS-LOG Bundles & Maturity Ladders | G.Core, C.23, G.4, G.6, G.5, C.22 |
| G.9 | Parity / Benchmark Harness | G.Core, G.5, G.6, G.4, F.15, E.18, A.21, E.5.2, E.10 |
| G.10 | SoTA Pack Shipping | G.Core, F.17, F.18, E.5.2, E.18, A.10, A.15.3 |
| G.11 | Telemetry-Driven Refresh & Decay Orchestrator | G.Core, G.6, G.7, G.5, G.8, G.9, G.10, B.3.4, E.18 |
| G.12 | DHC Dashboards | G.Core, C.21, G.6, G.11, A.19, G.0, F.17, F.18, E.5.2, E.10 |
| G.13 | External Interop Hooks for SoTA Discipline Packs | G.Core, G.2–G.7, G.9–G.12, A.19, A.18, G.0, F.17, E.5.2, E.18 |

**Total: 204 patterns.** Full titles and dependencies in this index.
