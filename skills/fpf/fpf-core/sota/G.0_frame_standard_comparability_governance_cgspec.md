## G.0 - Frame Standard & Comparability Governance (CG‑Spec)

**Tag:** Architectural pattern (foundational Standard; constrains G.1–G.5)
**Stage:** *design‑time* (establishes comparison legality & evidence minima; constrains run‑time gates)
**Primary hooks:** **USM / Scope (G)** (A.2.6), **Design–Run split** (A.4), **Evidence carriers** (A.10), **Assurance F–G–R with Γ‑fold** (B.1, B.3), **Change rationale** (B.4), **MM‑CHR discipline** (A.17–A.19/C.16), **Creativity‑CHR** (C.17), **NQD‑CAL** (C.18), **E/E‑LOG** (C.19), **Method‑SoS‑LOG** (C.23), **Bounded Contexts & Bridges + CL** (F.1–F.3, F.9), **Concept‑Sets** (F.7), **Mint/Reuse** (F.8), **RSCR** (F.15), **Lifecycle/Deprecations** (F.13–F.14), **UTS & Naming** (F.17–F.18), **No tool lock‑in** (E.5.1–E.5.3), **Lexical rules** (E.10), **GateCrossing visibility hooks** (E.18; GateChecks **A.21**; Bridge+UTS **A.27**; BridgeCard **F.9**).

Comparability Governance is the design‑time standard that fixes, for a given `CG‑Frame`, **what comparisons and aggregations are lawful**, under which declared **normalization/UNM** assumptions and **evidence minima**, so that run‑time publication and selection remain auditable. CG constrains run‑time gate checks (E.TGA/E.18) by supplying the referenced `CG‑Spec` artifacts and pinned editions; CG itself is not an admissibility mechanism.

**Didactic subtitle:** “Design‑time rules for safe, auditable comparison.”

### G.0:1 - Intent (informative)

Provide a **single, normative Standard** for a **CG‑Frame** that (a) names *what may be compared or aggregated*, (b) defines **lawful ScaleComplianceProfile (SCP) and aggregators** over CHR‑typed data, and (c) sets **minimal evidence** and **trust folding** rules so that all downstream generation (G.1), harvesting (G.2), measurement authoring (G.3), calculus (G.4), and dispatch/selection (G.5) operate **safely, comparably, and in‑scope**.

### G.0:2 - Problem frame (informative)

A team is extending FPF with a **CG‑Frame** (e.g., *Creativity*, *Decision*, *Architecture trade‑offs*). G.1–G.5 reference **CG‑Spec** for lawful comparison, but absent a clear Standard, projects drift into hidden cardinalization, ad‑hoc thresholds, and opaque evidence minima. **G.0** authors and publishes that Standard.

### G.0:3 - Problem (informative)

Recurring pains without a frame‑level spec:

* **Undefined comparison set.** Teams compare quantities without a declared **Characteristic/SCP** basis.
* **Illicit arithmetic.** Ordinals get averaged; units are mixed; polarity flips are implicit.
* **Opaque evidence minima.** Numeric gates run on *whatever is at hand*, not on declared **KD‑CAL lanes** or carriers.
* **Trust blur.** Cross‑Context reuse lacks **CL penalties** and Γ‑fold rules; selection **R_eff** is not auditable.
* **Inconsistent scope.** Global claims leak; boundaries and *describedEntity* are not attached to names.

### G.0:4 - Forces (informative)

* **Pluralism vs. comparability.** Rival Traditions must co‑exist while enabling lawful comparison.
* **Expressiveness vs. safety.** Rich **SCP profiles** and aggregators vs. **MM‑CHR** legality.
* **Locality vs. portability.** Context‑local semantics with explicit **Bridges + CL** when crossing.
* **Assurance vs. agility.** Minimal evidence gates that are strong enough to matter, light enough to adopt.
* **Design‑time vs. run‑time.** Keep Standards and thresholds **design‑time**; run‑time only *uses* them.

### G.0:5 - Solution — **The CG‑Spec Standard**

A **notation‑independent** object, published to **UTS**, that fixes *what is comparable, how, and under which evidence and trust minima*.

For top‑level disciplines, CG‑Spec is restricted to comparability, tolerances, and aggregation surfaces where sufficient basis exists (KD‑CAL lanes, Worked Examples, Γ‑fold reliability). CG‑Spec MUST NOT introduce “universal” cross‑Tradition scoring; run‑time choice belongs to the G.5 selector under CHR/CAL legality.

#### G.0:5.1 - CG‑Spec - Data Model (normative)

```
CG‑Spec :=
⟨ UTS.id, Edition, Context, Purpose, Audience,
  Scope := USM.ScopeSlice(G) ⊕ Boundary{TaskKinds, ObjectKinds},
  describedEntity := ⟨GroundingHolon, ReferencePlane ∈ {world|concept|episteme}⟩,
  WorldRegime? ∈ {prep|live}, // refines ReferencePlane=world; affects acceptance/telemetry; introduces no new planes
  ReferenceMap := minimal map{term/id → UTS|CHR|G.2} (stabilizes naming & describedEntity),

  ComparatorSet := [ComparatorSpec…],                 // finite, explicit
    // MUST NOT encode illegal scalarisation of partial orders;
    // lawful forms include: ParetoDominance, Lexicographic over typed traits,
    // medoid/median on ordinals; WeightedSum only on interval/ratio with unit alignment (CSLC‑proven)
  Characteristics := [CHR.Characteristic.id…],        // must exist in G.3 pack

  SCP := map Characteristic.id → ⟨
    ScaleTypes, Polarity ∈ {↑|↓|=}, Unit alignment rules,
    CoordinatePolicy?, GuardMacros ⊇ {UNIT_CHECK, ORD_COMPARE_ONLY, FRESHNESS_CHECK, PLANE_NOTE, PHI_CL_MONOTONE(policy_id), METRIC_EDITION_REF(id)?},
    AggregationSpecs
  ⟩,

  MinimalEvidence := map Characteristic.id → ⟨
    KD‑CAL lanes ⊆ {TA,LA,VA}, Carriers ⊆ A.10,
    Sample/Replication minima, Freshness/HalfLife (PathSlice window), ReferencePlane,
    Bridge allowances (CL thresholds, CL^plane policy id), I/D/S layer exposed to SCR fields,
    FailureBehavior ∈ {abstain | degrade.order | sandbox},
    UnknownHandling := tri‑state {pass|degrade|abstain} with explicit binding to Acceptance (no silent `unknown→0` coercion)
  ⟩,

  Γ‑fold := ⟨default:=weakest‑link | override(proof_refs, monotonicity, boundary)⟩,
  CL‑Routing := map Bridge.CL → penalty on R_eff only (F invariant),
  Φ := ⟨ Φ(CL) MUST be monotone, bounded (R_eff ≥ 0), and table‑backed; optional Φ_plane for {world|concept|episteme} crossings (unaffected by WorldRegime) ⟩,
  AcceptanceStubs := [AcceptanceClause template…],    // templates only; **context‑local thresholds live in CAL.Acceptance (G.4)**
  
  E/E‑LOG Guard := ⟨explore↔exploit budgets, probe accounting, NQD constraints⟩,
  Illumination := ⟨
    Q_refs ⊆ Characteristics, D_refs ⊆ Characteristics,
    QD_score := definition (typed), ArchiveRef := U.DescriptorMapRef (Tech; d≥2),
    InsertionPolicy, Edition := ⟨DHCMethodRef.edition, DistanceDefRef.edition⟩,
    DominanceDefault := exclude, PromotionPolicy? := lens/policy‑id
  ⟩, // IlluminationSummary is a report‑only telemetry summary over Diversity_P (coverage/QD‑score) and informs exploration; not part of dominance unless PromotionPolicy (lens/policy‑id) is named

 RSCR := testset{
    illegal_op_refusals,
    unit/scale checks,
    freshness windows,
    partial‑order scalarisation refusals,
    threshold semantics,
    CL→R_eff routing,
    refuse degrade.order on unit mismatches (MM‑CHR)
 },

  Naming := UTS Name Cards (required fields per F.17/F.18) with **Unified Tech** and **Plain** labels, Concept‑Set linkage, Bridge loss/fit notes, and lifecycle,
  Lifecycle := ⟨owner, DRR link, refresh cadence, decay/aging, deprecation + lexical continuity⟩,
  Provenance := ⟨carrier types, SoTA pack refs (G.2), DRR/SCR linkage⟩
⟩
```

**Notes:**
* `Characteristics[]` are pointers—no measurement semantics live here; those are authored in **G.3**.
* `SCP` binds **what** aggregations/comparisons are lawful **for this Frame** over those characteristics (using **G.3 AggregationSpecs**).
* `MinimalEvidence` is the **gate** consumed by G.1/M4 and G.5: if not met, numeric comparisons **degrade** to safe forms or **abstain** (see **§7.13**).
* `Γ‑fold` must state monotonicity and boundary behavior if not weakest‑link; proofs/anchors go to **CAL.ProofLedger** (G.4); legality constraints summarized in **§7.5–§7.7**.
* **Legality proof.** Units/scale/polarity legality **MUST** be proven via **MM‑CHR/CSLC** before any aggregation; **no silent `unknown→0` coercion**; thresholds live **only** in Acceptance (G.4) — see **§7.7** and **§7.8**.
* `CL‑Routing` sends penalties to **R_eff only**; **F** is invariant under Bridging.
* **Illumination default.** **IlluminationSummary** is a **report‑only telemetry summary** over **Diversity_P** (coverage/QD‑score). It informs exploration/refresh and tie‑breaks; it is **not** in the dominance set unless a **PromotionPolicy (lens/policy‑id)** is named.
* **Partial orders.** Where only a partial order is lawful, **do not force total orders** in `ComparatorSet`; downstream (G.5) returns explicit non‑dominated sets.
* **Guard macros.** Recommended set includes: `UNIT_CHECK`, `ORD_COMPARE_ONLY`, `FRESHNESS_CHECK`, `PLANE_NOTE`, `PHI_CL_MONOTONE(policy_id)`.

#### G.0:5.2 - SoTAPalette

1. **SoTAPalette (I).** Intensional profile of a discipline’s Traditions and method‑families with intentions and tolerances:
* admissible TaskKinds/ObjectKinds,
* required CHR types,
* characteristic operators/proofs,
* typical CL bridges (with known loss).

2. **SoTAPaletteDescription (D).** Publication of the palette: 
* metadata of Traditions, 
* Operator & Object Inventory, 
* Bridge Matrix with CL/loss notes, 
* micro‑examples, 
* UTS drafts. 
 
This is the “SoTA Synthesis Pack” of G.2 and must be citable in G.5 decisions.

3. **SoTAPaletteSpec (S).** Minimal gates on completeness/quality of a palette: 
* coverage of Traditions/sub‑tasks, 
* minimum replications/carriers across KD‑CAL lanes (TA/LA/VA), 
* explicit CL penalties for reductions, and bans on illegal operations (e.g., ordinal ≠ mean). 
 
These gates are consumed by CG‑Spec.Acceptance and Γ‑fold where cross‑Tradition comparison/aggregation is attempted

#### G.0:5.3 - Tradition

* In this framework, **“scientific/engineering Tradition/lineage/tradition” is an epistemic kind**: **`Tradition`** (I) with its **`TraditionDescription`** (D) and **`TraditionSpec`** (S).
* The **community of people** behind a Tradition is modeled separately as an optional **`TraditionCarrier`** that _carries_ a `Tradition` but does **not** determine cross‑Tradition comparability rules.
* In the **SoTA‑palette**, entries are **`Tradition`** items (epistemic) with their D/S artifacts; the palette composes them and exposes bridges/limits. The Dispatcher (G.5) selects among these entries under CHR/CAL constraints; CG‑Spec (G.0) only governs comparability/Γ‑fold where justified.

Tradition (I): an epistemic formation (Tradition‑of‑thought, lineage) identified by its method family:
- operator set and admissible transformations,
- admissible TaskKinds/ObjectKinds,
- necessary CHR types and proof idioms,
- canonical CL bridges and stated limits,
- stance on measurement scales and allowed algebra.
(Notes: This is an epistemic kind, not a social group. See §TraditionCarrier for the social carrier.)

TraditionDescription (D): the documentary corpus of a Tradition:
- charter/lineage and key references,
- Operator & Object inventory with CHR preconditions,
- Bridge Matrix (CL) with loss and validity regions,
- Worked Examples with CHR annotations,
- UTS drafts for typical tasks,
- KD‑CAL lane coverage and replication notes,
- explicit anti‑operators / banned reductions (e.g., ordinal ≠ mean).

TraditionSpec (S): inclusion gates for a Tradition to be considered comparable/aggregable:
- minimum replication across KD‑CAL lanes (TA/LA/VA),
- declared CHR prerequisites and proof idioms,
- declared CL penalties/conditions for any cross‑Tradition bridge,
- Γ‑fold contribution rule (how evidence accumulates),
- prohibitions on illegal scale algebra.
These S‑level gates are referenced by CG‑Spec.acceptance only where aggregation/comparison is attempted; otherwise the Tradition remains descriptive.

TraditionCarrier (I): role of a social/organizational system (people, labs, consortia) that holds a Tradition. Carriers supply replication capacity and provenance but have no normative authority over cross‑Tradition aggregation rules.

Γ‑fold: an evidence/reliability fold that aggregates only along declared commensurate dimensions; includes penalties from CL bridges and lane‑mismatch factors. Γ‑fold parameters MUST be cited to KD‑CAL lanes and Worked Examples; when absent, aggregation is disallowed.

Default composition: weakest‑link; admissible overrides: {min‑k‑of‑n, harmonic, conservative Bayesian}; override requires CAL.ProofLedger refs

#### G.0:5.4 - Authoring Steps (S1–S6)

**S1 - Frame Charter (Scope & describedEntity)**
Declare **Context**, **USM scope**, *describedEntity* (`GroundingHolon`, `ReferencePlane`), TaskKinds/ObjectKinds; record boundary examples and non‑examples.

**S2 - ComparatorSet & SCP Draft**
List **which** comparisons/aggregations the Frame intends (e.g., dominance, lexicographic, Pareto, affine sums on interval/ratio with unit alignment). Bind each comparator to **G.3/AggregationSpecs** and attach **GuardMacros**; capture legality/tolerance assumptions in the CG‑Spec **ScaleComplianceProfile (SCP)**. **Do not** scalarise partial orders; for ordinals, use medoid/median; **WeightedSum is forbidden** on mixed scale types.

**S3 - Characteristics Binding**
For each comparison you intend to allow, bind the **CHR.Characteristic id** and required **Scale/Unit/Polarity**; if missing, author in **G.3** or reuse via UTS (F.8). For any numeric encoding of ordinals, publish **CoordinatePolicy** with non‑entitlements.

**S4 - Minimal Evidence Gates**
Per characteristic, declare **KD‑CAL lanes** (TA/LA/VA), required **carriers** (A.10), freshness/half‑life, and **Bridge/CL allowances**. Define **failure behavior**: **degrade to order‑only**, **sandbox**, or **abstain**.

For unit mismatches specify **sandbox (quarantine) or refuse**; **degrade.order is not permitted for unit mismatches under MM‑CHR**.

MinimalEvidence MUST name **CHR.Characteristics** used by Acceptance/Flows and the **TaskSignature fields** they constrain (by id), so **G.5** can gate **before** selection.

**S5 - Γ‑fold & CL Routing**
Set default **Γ‑fold** for trust aggregation and the **CL penalty** table. Document proofs or references if overriding weakest‑link.

**S6 - Publication & Tests**
Mint **UTS** Name Cards with twin labels; attach **loss notes** for Bridges. Register **RSCR** tests: (i) refuse illegal ops (e.g., mean on ordinal), (ii) enforce unit/scale checks, (iii) verify freshness/PathSlice handling, (iv) refuse illegal scalarisation of partial orders, (v) verify **CL → R_eff** routing and **Φ(policy‑id)** publication in SCR.
Acceptance depends on (a) presence of SoTAPaletteDescription (G.2) with attached CHR/CAL evidence (G.3–G.4), and (b) justification of any aggregation via Γ‑fold (reliability fold) with explicit CL loss accounting. Where evidence is insufficient, acceptance MUST fall back to per‑Tradition reporting without cross‑Tradition aggregation.

### G.0:6 - Interfaces — minimal I/O Standard (normative)

| Interface          | Consumes                                | Produces / Constrains                                                    |
| ------------------ | --------------------------------------- | ------------------------------------------------------------------------ |
| **G.0‑1 Charter**  | CG‑Frame brief, USM scope, SoTA signals | `CG‑Spec.Scope`, `describedEntity`, `ComparatorSet`                            |
| **G.0‑2 SCP**      | G.3 CHR Pack, AggregationSpecs          | `CG‑Spec.SCP` + guard bindings                                           |
| **G.0‑3 Evidence** | SoTA carriers (G.2), KD‑CAL norms       | `CG‑Spec.MinimalEvidence`, `Γ‑fold`, `CL‑Routing`                        |
| **G.0‑4 Publish**  | All above                               | Versioned `CG‑Spec@UTS` + Name Cards, RSCR ids, Lifecycle                |
| **→ G.1**          | `CG‑Spec`                               | M1/M4 guardrails; abstain/degrade paths wired; M3/M4 scoring legality; Characteristic refs bound (F invariant) |
| **→ G.2**          | `CG‑Spec`                               | Inclusion/exclusion & Bridge/CL policy for SoTA Synthesis                |
| **→ G.3**          | `CG‑Spec`                               | Which Characteristics/Scales must exist; legality macros to expose       |
| **→ G.4**          | `CG‑Spec`                               | Acceptance templates; evidence gates; Γ‑fold/CL routing Standards        |
| **→ G.5**          | `CG‑Spec`                               | Eligibility gates; minimum **R_eff** checks; degradation/abstain policies; Illumination hooks (ArchiveRef/U.DescriptorMapRef, InsertionPolicy, Edition), publication of **Φ(CL)/Φ_plane policy‑ids** in SCR |
| **→ G.6**          | `CG‑Spec`                               | EvidenceGraph guard fields (**Φ(CL)/Φ_plane policy‑ids**, freshness windows, **PathId/PathSliceId**) made citable; selectors/audits reference PathIds (no formats mandated) |

### G.0:7 - Conformance Checklist (normative)

1. **Context declared.** `CG‑Spec` is published **in** a `U.BoundedContext`; no global claims.
2. **Comparator set explicit.** Every permitted comparison/aggregation is named and typed; anything else **abstains by default**.
3. **CHR‑bound.** All compared quantities reference **CHR.Characteristic ids** with declared **Scale/Unit/Polarity**; guard macros attached.
4. **Minimal evidence published.** Per characteristic: **KD‑CAL lanes**, carriers, freshness, Bridge/CL allowances, and **failure behavior** are declared.
5. **Γ‑fold stated.** Default **weakest‑link**, or an alternative with proof obligations (monotonicity, boundary).
6. **CL penalties** routed to R_eff only; F is invariant; **publish Φ(CL)/Φ_plane policy‑ids in SCR** for any penalised claim.
7. **No illegal ops.** Ordinal **SHALL NOT** be averaged/subtracted; unit mismatches **SHALL** fail fast (MM‑CHR).
8. **Design/run split.** **AcceptanceStubs** provide templates in **G.0**; all **context‑local thresholds live only in CAL.Acceptance (G.4)**; nothing is hidden in CHR or code paths; manifests are externally inspectable.
9. **UTS‑ready.** Name Cards minted/reused with twin labels; Bridges carry **CL** and loss notes.
10. **RSCR wired.** Tests exist for refusal paths, unit/scale checks, threshold semantics, and CL→R_eff routing.
11. **Lifecycle set.** Refresh cadence and decay policy declared; deprecations follow **F.13–F.14** with lexical continuity notes.
12. **describedEntity present.** `GroundingHolon`, `ReferencePlane`, and a minimal `referenceMap` are recorded.
13. **Pre‑flight numeric gates.** Any numeric comparison/aggregation **MUST** cite a `CG‑Spec` entry with lawful **SCP/Γ‑fold** and **MinimalEvidence** satisfied; cross‑Context reuse requires **Bridge + CL** with penalties routed to **R_eff only** (never F).
14. **Partial‑order stance.** `ComparatorSet` SHALL NOT force total orders where only partial orders are lawful; **no scalarisation of partial orders**. Use Pareto/Lexicographic/medoid/median as lawful.
15. **Illumination discipline.** If Illumination is used, publish `ArchiveRef`, `InsertionPolicy`, and `Edition`; **exclude from dominance by default**; any promotion into dominance **MUST** cite a named lens/policy‑id and be recorded in provenance.
16. **Freshness/PathSlice.** Freshness windows are published and enforced; PathSlice identifiers are recorded in SCR when freshness gates influence gating/selection.
17. **GateCrossing hook exposure.** Exports **MUST** provide `Expose_CrossingHooks` inputs so GateChecks (**A.21**) can validate EvidenceGraph paths and crossings: **CrossingSurface** present/consistent (**E.18/A.27/F.9**), **LanePurity**, and **Lexical SD** (**E.10**). Any failure is **blocking** for publication.

**Guards as in C.20:**
* **CC‑G0‑Φ.** **Φ(CL)** (and **Φ\_plane**, if used) **MUST** be **monotone, bounded, table‑backed**; publish policy ids; **R\_eff ≥ 0** by construction.
* **CC‑G0‑Unknowns.** **Unknowns propagate tri‑state** {pass|degrade|abstain} to **Acceptance**; **no silent coercions**.
* **CC‑G0‑CSLC.** **Scale/Unit/Polarity legality** MUST be proven (MM‑CHR/CSLC) **before** any aggregation; **no mean on ordinals; no unit mixing**.
**Registry hooks.** Every CG‑Spec entry declares Lifecycle/DRR and **RSCR triggers for Φ‑table, SCP, Γ‑fold, Bridge edits** (parity re‑runs required).

### G.0:8 - Consequences (informative)

* **Lawful comparability.** Teams know *exactly* what can be compared/aggregated and under which evidence minima.
* **Auditable trust.** Γ‑fold and CL routing make **R_eff** computation transparent to selectors and reviewers.
* **Frictionless downstream.** G.1–G.5 consume a single spec; CHR/CAL avoid hidden thresholds; dispatch is explainable.
* **Local first, portable later.** Context‑local semantics are primary; Bridges make portability deliberate and costed.

### G.0:9 - Worked micro‑example (indicative)

CG‑Frame: R&D Portfolio Decisions
Scope: ObjectKinds={Project}, TaskKinds={SelectPortfolio}
describedEntity: ⟨GroundingHolon=R&D, ReferencePlane=world⟩

ComparatorSet = {
  ParetoDominance,
  LexicographicMin(SafetyClass),
  AffineSum(CostUSD_2025)
}

Characteristics = \[
  SafetyClass : scale=ordinal,  polarity=↑, levels={D,C,B,A,AA},
  CostUSD_2025 : scale=ratio,   polarity=↓, unit=USD_2025,
  Readiness : scale=nominal,    polarity="="
]

 SCP:
  SafetyClass   → ORD_COMPARE_ONLY; aggregator=LexiMin; coordinate=Isotonic(order‑only) // no means
  CostUSD_2025  → UNIT_CHECK; aggregator=Sum; unit_alignment=USD_2025; polarity=↓
  Readiness     → equality_only; aggregator=None; ordering via Bridge only (CL≥2 with loss note)

MinimalEvidence:
  SafetyClass  → lanes={LA}, carriers={test_reports}, freshness≤18mo,
                  failure={abstain if lanes/carriers missing; refuse if mean() attempted}
   CostUSD_2025 → lanes={LA,VA}, carriers={ERP,audit}, freshness≤12mo,
                  failure={refuse if unit misaligned; sandbox if carrier missing}

  Readiness    → lanes={VA}, carriers={process_docs}, freshness≤12mo,
                  failure={abstain for ordering unless Bridge(CL≥2)}

Γ‑fold := weakest‑link across lanes
CL‑Routing: CL=2 (Marketing→Engineering) → multiplicative penalty on R_eff; F invariant

AcceptanceStubs:
  AC_SafetyGate: SafetyClass ≥ B
  AC_Budget: Σ CostUSD_2025 ≤ Envelope

RSCR:
* refuse mean(SafetyClass)
* fail on (USD + Readiness)
* verify AC_Budget on worked examples

### G.0:10 - Relations (wiring)

**Builds on:** A.4, A.10; **B.1/B.3/B.4**; **A.17–A.19/C.16**; **C.17–C.19**; **F.1–F.3/F.7–F.9/F.13–F.15/F.17–F.18**; **E.5.1–E.5.3** (no tool lock‑in); **E.10**.
**Publishes to:** G.1 (generator guards), G.2 (harvesting policy & CL), G.3 (required CHR), G.4 (acceptance/evidence), G.5 (eligibility gates).
**Constrains:** any LOG implementation via CAL/CHR legality and evidence minima.

### G.0:11 - Author’s quick checklist

1. Write the **Frame Charter** (Context, USM scope, describedEntity).
2. Enumerate the **ComparatorSet**; bind **SCP** with guard macros and AggregationSpecs.
3. Bind **Characteristics\[]** to **CHR** ids; ensure Scale/Unit/Polarity are declared (reuse or mint in UTS).
4. Publish **MinimalEvidence** per characteristic (KD‑CAL lanes, carriers, freshness, Bridge/CL allowances, failure behavior).
5. State Γ‑fold and CL‑Routing; **default Γ‑fold = weakest‑link**; if overriding, attach CAL proofs (monotonicity, boundary behavior). Record **Φ(CL)/Φ_plane** **policy ids**; penalties → **R_eff only**.
6. Publish to **UTS** with Name Cards, twin labels, Bridges (+loss notes); register **RSCR** tests.
7. Set **refresh/decay**; log changes to **DRR/SCR**; maintain lexical continuity on deprecations.

### G.0:End
