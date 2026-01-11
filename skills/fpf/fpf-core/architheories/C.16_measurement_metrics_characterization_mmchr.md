## C.16 - Measurement & Metrics Characterization (MM‑CHR)

### C.16:1 - Intent (Normative)

**Name.** *Measurement & Metrics Characterization (MM‑CHR).* This is user-oriented name: in user‑facing narrative we say ‘metrics’; in Tech register we speak `U.DHCMethodRef`/`U.Measure`.
**Intent.** Provide a **transdisciplinary substrate for measurement** that any architheory can rely on: a small, stable set of intensional constructs and relations—**`U.DHCMethodRef`**, **`U.Measure`**, **`U.Unit`**, **`U.EvidenceStub`**—disciplined by **CSLC** (*Characteristic / Scale / Level / Coordinate*) so that every recorded value is **interpretable** and **comparable** across CG‑frames (physics lab time‑of‑flight, figure‑skating judging, architectural modularity, etc.). **C.16** does **not** re‑define **Characteristic** (A.17) nor the CSLC kernel Standard (A.18); instead, it **exports** the measurement substrate that *binds* an architheory’s metric notions to **one Characteristic and one Scale** and frames a **conceptual link to evidence**. This characterization is **notation‑neutral**, **tool‑agnostic**, and **open‑ended** (no “lifecycle” narrative; evolution proceeds via **RSG** moves with checklists). 

**Outcomes.**
(1) A uniform way for architheories to *declare* what is measured and *read* what has been measured; (2) explicit **Characteristic anchoring** and **Scale typing** per CSLC; (3) principled **comparability** and **polarity** (declared at the template level); (4) **traceability** via conceptual evidence stubs; (5) seamless alignment with cross‑domain quantity notions (ISO 80000, ISO/IEC 25024, QUDT, SOSA/SSN, Verspoor) through Unification rows (Part F). 

### C.16:2 - Scope & Status (Normative)

**Scope.** **C.16** specifies the **measurement substrate** for FPF architheories: the roles of `U.DHCMethodRef`, `U.Measure`, `U.Unit`, `U.EvidenceStub`; their **CSLC discipline**; the notions of **Scale type**, **polarity**, **comparability**, and **evidence sufficiency** at the level of *conceptual conditions*. It **exports** these constructs for all architheories (KD‑CAL, Arch‑CAL, etc.) without prescribing domain formulae or procedures. 

**Status.** **Normative architheory.** C.16 **depends on** A.17 (canonical **Characteristic**) and A.18 (minimal **CSLC** in Kernel). Where C.16 cites external CG‑frames, the stance is through **Part F** rows and **Bridges** (with CL and loss notes), not by vocabulary import. 

**Out of scope.** No computational recipes, no workflow prescriptions, no governance/process guidance. C.16 concerns **objects of thought** (intensions) and their **validity conditions**, not records or tooling. (Implementation guidance, if any, belongs outside Part C.)


### C.16:3 - Problem & Context (Informative)

#### C.16:3.1 - The problem C.16 solves

Across architheories, people say “score”, “metric”, “rating”, “property”. Without a shared substrate, numbers drift: *42 of what? on which scale? comparable to whom?* C.16 eliminates drift by requiring every metric notion to **bind** to **one** Characteristic and **one** Scale, and by **separating** intensional anchors from descriptions and ScoringMethods. The result is **portable meaning**: a measure is always readable as a **Coordinate on a declared Scale of a named Characteristic**, with a principled path to evidence. 

#### C.16:3.2 - Context and prior art

* **Kernel canon.** A.17 makes **Characteristic** the sole canonical anchor for measurability; A.18 fixes **CSLC** as the minimal sufficiency for interpretability. C.16 relies on both.
* **Cross‑domain alignment.** The MM‑CHR family already maps FPF U.Types to **ISO 80000‑1 (Quantity)**, **ISO/IEC 25024 (Data‑quality Characteristic)**, **QUDT (QuantityKind/QuantityValue)**, **W3C SOSA/SSN (Observable/Observed/Result)**, and domain “feature/metric” usage (Verspoor, TF Metrics). C.16 uses these rows **as Bridges** (Part F), preserving local senses and documenting losses.  
* **Open‑ended evolution.** FPF replaces “lifecycle” with **Reachable‑States Graph (RSG)**: movement is along **certified states** with checklists; measurement work adopts the same open‑endedness (re‑entry allowed when distinctions change). C.16 uses RSG to frame **readiness** and **revision** of metric notions conceptually (no processes implied).


### C.16:4 - Forces (Informative)

**F1 — Interpretability first.** A value detached from its Characteristic/Scale is meaningless; CSLC supplies minimum context.
**F2 — Transdisciplinarity.** Physics, architecture, curation, sport judging—*one* substrate must cover all while respecting scale types and polarity.
**F3 — Intension vs description.** Confusing the **Characteristic** (intensional object) with its rubric or exemplar text (descriptions) corrupts claims; C.16 keeps them distinct.
**F4 — Comparability without coercion.** Ordinal ≠ interval; ratio admits unit change, ordinal does not; polarity matters for “better/worse”. C.16 encodes these **as conceptual constraints**, not formulas.
**F5 — Evidence sufficiency.** A measure should be *checkable in principle*; evidence is a **conceptual link** (not storage advice).
**F6 — Lexical discipline.** One canon in normative register; narrative labels are didactic only (Part E). C.16 reuses E.10’s **register mapping**.


### C.16:5 - Solution Outline (Normative)

**S1 — Exported objects.** C.16 **exports** four intensional constructs to be used by any architheory:

1. **`U.DHCMethodRef`** — the *binding* of **one `U.Characteristic`** to **one Scale form**, with declared **polarity** and a conceptual **compatibility claim** (what counts as “same‑scale” for comparison). It is an *intensional specification*, not a record layout.
2. **`U.Measure`** — an *assertion* that a **subject** occupies a **Coordinate** (or **Level**, if discrete) on that Scale; the measure **references** its template and carries a **conceptual pointer to evidence** (`U.EvidenceStub`).
3. **`U.Unit`** — the *unit kind* associated with the Scale where applicable (physical quantities, normalized “points”, “stars”, “%”); unit coherence is part of comparability conditions.
4. **`U.EvidenceStub`** — a *conceptual locator* of grounds for the asserted value (type, identifier, brief summary, optional integrity notion); sufficiency criteria are **conceptual** (see §9, later).

**S2 — Comparability stance.** C.16 states **conceptual comparability** conditions: *same Characteristic*, *compatible Scale type and parameters*, *unit coherence* for interval/ratio; **no** forced coercions for nominal/ordinal; any score‑producing ScoringMethod **must be monotone** w\.r.t. template polarity. (Details: §7–§8 in later parts.)

**S3 — Evidence stance.** A measure that, by its template, **requires** evidence, is **inadmissible** without a meaningful `U.EvidenceStub`. C.16 defines **what it means conceptually** for evidence to “connect” the subject, the Characteristic, and its symbolic description; mechanisms are out of scope. (Details: §9 in later parts.)

**S4 — RSG framing (open‑endedness).** Readiness, calibration, and revision of metric notions are expressed as **RSG node moves with checklists** (e.g., “characteristic anchored”, “Scale typed”, “Unit coherent”, “ScoringMethod declared”), allowing **re‑entry** when distinctions change; there is no terminal “lifecycle”. (Details: §10, later.)


#### C.16:5.1 - Lexical Discipline & Registers (Normative)

**L1 — Canon.** Use **Characteristic / Scale / Level / Coordinate / Score / Unit / ScoringMethod** in **Tech** register; their `U.*` counterparts in **Formal**; narrative labels (e.g., *axis*, *points*, *stars*) are **didactic only** at first‑mention mapped to canon (E.10). 
**L1‑bis — “metric”.** The noun *metric* is **not** a Tech‑register canonical token for measurables; use **Characteristic / Scale / Coordinate / Score / ScoringMethod**. It **may** appear in the architheory title and in the Formal names `U.DHCMethodRef` / `U.Measure`. Do not use *metric* as a synonym for **Characteristic** or **Score** in normative prose.
**L2 — Intension vs Description.** Keep **intensional objects** (`U.DHCMethodRef`, `U.Characteristic`) distinct from **descriptions** (rubrics, exemplars) and from **claims** (`U.Measure`). No collapsing of names across these layers.
**L3 — No synonym sprawl.** In normative clauses do **not** substitute *dimension/axis/property/feature* for **Characteristic**; A.17 governs canonicalization. (C.16 inherits A.17’s rename policy.)
**L4 — Bridge‑only unification.** Cross‑vocabulary sameness appears only via **F.9 Bridges** with **CL** and **loss notes**; C.16’s lexicon is the *source* side for measurement rows.
**L5 — “Metric” in registers.** In **Tech/Formal** avoid the noun *metric* as a primitive; use `U.DHCMethodRef` / `U.Measure` / **Score**. In **Plain** register *metric* MAY denote “a Template+Measure family” on first mention, with an explicit pointer to canonical terms.

#### C.16:5.2 - Relations (pointers; details later)

**To A.17 / A.18.** C.16 *uses* A.17’s canonical **Characteristic** and A.18’s **CSLC sufficiency**; it neither re‑states nor weakens them.
**To Part F.** C.16 is the **exporting architheory** behind measurement rows in UTS/Bridges (e.g., **result‑value** ↔ SOSA `Result`, ISO `QuantityValue`).
**To Arch‑CAL.** Architectural qualities (*Coupling, Cohesion, Evolvability*) become **Characteristics** measured via C.16 templates; architectural dynamics read as trajectories in **CharacteristicSpace** (A.17 context).

#### C.16:5.3 - Normative Core Model (types & Standards)

> **Position.** MM‑CHR does **not** redefine kernel terms; it **binds** them to an architheory‑level Standard that every metric must satisfy. Canonical vocabulary and CSLC duties are inherited from **A.17**/**A.18** and referenced here without duplication.
> 
> **Source of Truth** A.17/A.18 are the sole sources of truth for Canon and CSLC; C.16 **adopts by reference** and **forbids restatements** of their definitions. C.16 only **exports** `U.*` constructs, comparability stance, evidence semantics, and RSG touch‑points.

##### C.16:5.3.1 - `U.DHCMethod` — the metric definition (normative)

**Role.** An intensional **Standard** that fixes *what is measured* and *how values must be read*—without producing any values itself. It is a *Definition*, not a Measure. **References to this template in data use `U.DHCMethodRef`.**

**R‑MT‑1 (CSLC anchor).** A DHCMethod **SHALL** bind to **exactly one** `U.Characteristic` and **exactly one** **Scale‑form** admissible for that Characteristic (cf. A.18). Level is **optional** (used when the scale is enumerated); otherwise values are given directly as Coordinates.

**R‑MT‑2 (Unit).** If the scale carries units (interval/ratio), the template **SHALL** designate a **Unit** of presentation. For ordinal/nominal scales, unit may be absent or a nominal label (e.g., “stars”). (Old MM‑CHR Annex A already listed these structural elements; here we fix the conceptual obligation. )

**R‑MT‑3 (Polarity).** For any ordered scale, the template **SHALL** declare polarity (*higher‑is‑better / lower‑is‑better / target‑is‑best*), used by downstream ScoringMethods and comparisons (see §6). A **targeted** Scale **SHALL** declare at the Template: (a) the **target value**, (b) the **tolerance semantics** (e.g., symmetric band ±δ, or asymmetric bands), and (c) the **monotone fall‑off** convention outside the band. Any 𝒢 derived from a targeted Scale **MUST** be piecewise‑monotone toward the target and respect the declared tolerance semantics.

**R‑MT‑4 (Applicability).** A template **SHALL** state the **applicability frame** (what kinds of subjects it meaningfully applies to) in conceptual terms; this is a property of the definition, not of any measure.

**R‑MT‑5 (Intension vs description).** The template is an **intensional object**. Any rubric, checklist, or prose that explains it is a **Description**; they are related but not identical (E.10 discipline).

**R‑MT‑6 (Cardinality hint).** A Template **MAY** declare its intended **cardinality semantics** for a subject within a **time stance** (e.g., *latest‑only*, *at‑most‑one‑per‑day*, *time series*).
Where declared, claims outside that semantics are **inadmissible conceptually** (they must be reframed or versioned). *Purpose:* prevent silent duplicates and mixed regimes without imposing storage logic.

 **R‑MT‑7 (MAY):** “`UncertaintyPolicy` — optional conceptual guidance on how uncertainty is expressed/read (e.g., band/CI/quantile), without prescribing methods/tools.
    

##### C.16:5.3.2 - `U.Measure` — the recorded reading (normative)

**Role.** A **claim** that a subject occupies a **Coordinate** (or named **Level**) on the template’s scale, backed by a minimal pointer to its grounds.

**R‑ME‑1 (Template binding).** Every Measure **SHALL** reference exactly one DHCMethodRef; its **Value/Coordinate** must be **valid** for that template’s scale (type, range, category).

**R‑ME‑2 (Subject).** A Measure **SHALL** identify its **subject‑of‑measurement** (the bearer) unambiguously in the same Context of meaning as the template’s applicability frame.

**R‑ME‑3 (Evidence stub).** Where the template requires it, a Measure **SHALL** include an **EvidenceStub**—a conceptual pointer sufficient to support independent reasoning about the claim’s origin. (The old spec framed this as “traceability/provenance”; we keep only the **conceptual** role here. )

**R‑ME‑4 (Time stance).** A Measure **SHALL** carry a **time stance** (e.g., “as‑observed at T”, or “as‑aggregated over W”), expressed conceptually; it disambiguates the reading’s intended window without prescribing formats.

**R‑ME‑5 (Entity vs relation).** If the Characteristic is **relational**, the subject is a **tuple** (pair, k‑tuple); the wording of the claim reflects that arity and the template’s relation topology (cf. A.17).

R‑ME‑6 (MAY):** “`UncertaintyStub` — optional conceptual pointer to the adopted uncertainty estimation for this Measure, **if** required by the template.

> *Informative anchor.* The old Annex B example “Article Completeness” illustrates the split template/measure/evidence; **C.16** keeps the split but forbids storage‑level talk.

##### C.16:5.3.3 - `U.Unit` — semantics of quantities (normative)

**Role.** A conceptual marker of **quantity kind** and admissible **conversions** within that kind; not every scale requires it.

**R‑UN‑1 (Quantity kind).** Where units apply, the template **SHALL** indicate the **quantity kind** (e.g., Time, Length, Dimensionless‑Score). Units are meaningful only **within** one kind.

**R‑UN‑2 (Convertibility).** Comparisons across different units are permitted **iff** they are **convertible** by kind‑preserving transformation (ratio/interval scales); for ordinal/nominal scales, no numeric conversions exist. (Old Annex A listed conversion hints; here we assert the conceptual boundary. )

**R‑UN‑3 (Canonical labels).** `%` denotes “fraction×100”; “points” denotes dimensionless magnitudes used for scores; “stars” denotes discrete ordinal marks. These are **labels** of representation, not new characteristics.

**R‑UN‑4 (Quantity‑kind bridge).** A Template on an interval/ratio Scale **SHOULD** name the underlying **quantity kind** (e.g., ISO 80000/QUDT category) to enable safe external bridges. This does **not** import external vocabularies; it declares an alignment point.

##### C.16:5.3.4 - `U.EvidenceStub` — pointer to grounds (normative)

**Role.** A compact **tie** from a Measure to the grounds sufficient for **reasoned audit** (not a repository prescription).

**R‑EV‑1 (Minimal sufficiency).** An EvidenceStub **SHALL** carry, at minimum, a **type‑of‑ground** and an **identifier** sufficient to retrieve or reconstruct the grounds in the appropriate Context of meaning.

**R‑EV‑2 (Compositionality).** Multiple grounds may be **composed** as a finite set; composition is **commutative/associative/idempotent** at the level of stubs, enabling conceptual merge of corroborations.

**R‑EV‑3 (Soundness axiom).** A Measure **is admissible** only if at least one **auditable chain of grounds** can be stated from the bearer to the Characteristic via an appropriate Description (Object–Concept–Symbol triangle in the episteme). (The old text motivates “transparency/trust”; **C.16** states the conceptual admission rule. )

#### C.16:5.4 - Polarity, Comparability, and ScoringMethods (normative)

> **Notation.** To avoid clashes with the kernel’s global aggregation symbol, this architheory denotes a **ScoringMethod** (score‑level mapping) by **𝒢** (calligraphic 𝒢).

**R‑POL‑1 (Declared polarity).** Every ordered scale **SHALL** declare polarity at the **template**. Any **ScoringMethod** **𝒢** must be **monotone** with that polarity.

**R‑CMP‑1 (Comparability conditions).** Two readings are **directly comparable** when they share **Characteristic**, **scale type**, and **unit** (or unit is convertible within one quantity kind). Otherwise, comparability requires an explicitly declared **𝒢** on a common representation.

**R‑G𝒢‑1 (ScoringMethod disclosure).** If a metric issues a **Score**, its **ScoringMethod** **𝒢 : Coordinate → Score** **SHALL** be named with a **bounded codomain** and stated monotonicity. (The old text discussed “score ranges” and mapping; **C.16** keeps only the conceptual duty. )

**R‑G𝒢‑2 (Ordinal respect).** For ordinal inputs, **𝒢** must be **order‑preserving**; interval assumptions **MUST NOT** be smuggled in.


#### C.16:5.5 - Entity vs Relation bindings (normative clarifications)

**R‑ER‑1 (Arity preservation).** If the Characteristic is `U.EntityCharacteristic`, the subject is **one** bearer; if `U.RelationCharacteristic`, the subject is a **k‑tuple** (k ≥ 2). The Measure’s claim text **SHALL** reflect this arity.

**R‑ER‑2 (Relation scale).** Relation‑valued scales **SHALL** fix their symmetry/antisymmetry and directionality (e.g., distance symmetric; influence directional), at the **template** level.

**R‑ER‑3 (Bridge to CG‑frames).** In architectural CG‑frames, **Coupling/Cohesion** are Characteristics over **modules** (structure) or **roles** (function). Their measures are relational (**Coupling**) or unary (**Cohesion** within an element), but both live in the same MM‑CHR substrate. (Alignment hinted in the old mapping rows across contexts. )


#### C.16:5.6 - Acceptance (conceptual, RSG‑aware)

> Acceptance here is **thought‑level**. It uses the **Reachable‑States Graph (A.2.5)** pattern to organise mental checks—no “lifecycle” narratives.

**SCR‑C16‑A (Template sufficiency).** You can traverse **N1→N3** (Characteristic fixed → Scale typed → Unit coherent) for the template **without** invoking any implementation artifacts (cf. A.18 RSG alignment).

**SCR‑C16‑B (Reading sufficiency).** For a given subject, you can traverse **N4→N6** (ScoringMethod named where needed → exemplar‑anchored sense → reading established) with polarity and arity explicit.

**SCR‑C16‑C (Comparability).** When two readings are placed side‑by‑side, you can state in one breath whether they are **comparable as‑is** or only **after 𝒢**, and **why**.

**SCR‑C16‑D (Evidence adequacy).** For any required EvidenceStub, you can sketch at least one **auditable chain of grounds** from the subject to the Characteristic via a Description in the right Context.


#### C.16:5.7 Cross‑references & anchors

* **A.17 (CHR‑NORM).** Canonical **Characteristic** and Entity/Relation split; lexical rules and alias sunset.
* **A.18 (CSLC‑KERNEL).** One Characteristic + one Scale per template; Level optional; operation guard by scale type.
* **Annex C (old MM‑CHR).** Cross‑domain alignment hints for Characteristics/Observations/Quantities across ISO 80000, ISO/IEC 25024, QUDT, SOSA/SSN (used here only as conceptual witnesses).

### C.16:6 - Permitted operations by scale type (with anti‑examples)

| Scale type   | Comparisons    | Location          | Differences        | Ratios                   | Admissible summaries                                  | Typical anti‑patterns (forbidden)                                   |
| ------------ | -------------- | ----------------- | ------------------ | ------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------- |
| **Nominal**  | =, ≠           | mode, frequencies | —                  | —                        | counts, proportions                                   | averaging labels; ordering categories without a declared order      |
| **Ordinal**  | <, =, > (rank) | median, quantiles | **not meaningful** | —                        | order‑respecting summaries (median rank, percentiles) | arithmetic mean of ranks; variance on ranks; linear blends of ranks |
| **Interval** | <, =, >        | mean location     | Δ meaningful       | ratio **not** meaningful | mean, sd of **differences**, correlation              | ratio claims (“twice as hot” in °C); geometric mean                 |
| **Ratio**    | <, =, >        | mean location     | Δ meaningful       | ratios meaningful        | arithmetic/geometric means, cv, growth rates          | adding heterogeneous units; log on nonpositive values               |

**Guards.**
G‑1 (Order). On ordinal, any transform used inside 𝒢 **MUST** be **monotone**.
G‑2 (Differences). On interval/ratio, **Δ** is legitimate; on ordinal/nominal, it is **undefined**.
G‑3 (Ratios). Only ratio Scales admit **x/y** semantics; interval/ordinal/nominal do not.
G‑4 (Unit coherence). Interval/ratio arithmetic presumes compatible units (or declared conversion).
G‑5 (Target polarity). If polarity is “targeted”, comparison is via distance‑from‑target, not simple ↑/↓.

*(These rules line up with the MM‑CHR exposition of CSLC and term discipline; A.17 fixes the lexical side.)* 

### C.16:7 - Evidence Semantics (Normative)

#### C.16:7.1 - What an Evidence Stub is (and is not)

**Definition.** `U.EvidenceStub` is a **conceptual pointer** that ties a **measure** to the **grounds** sufficient for independent checking (observations, arguments, lawful transformations). It is not the run log, not the carrier, and not the intensional characteristic itself. This keeps **intension–description–specification** distinct per E.10.D2 and the Clarity Lattice.

**Rule Σ‑1.** Whether evidence is **required** is a **property of the metric template**; if required, each `U.Measure` **SHALL** include an `U.EvidenceStub`.
**Rule Σ‑2.** Evidence composition is **commutative, associative, idempotent** at the concept level (sets/multisets of grounds); combining grounds can never *reduce* what is knowable about the measure’s warrant.
**Rule Σ‑3.** *Soundness minimum:* there exists a conceptual chain linking **bearer → Characteristic → Scale/Unit → admissible method/episteme**. (No “free‑floating numbers”.)
**Rule Σ‑4.** Declared *agreement* constructs (e.g., dual readings, panels) **MUST** be appropriate to the scale type (rank concordance for ordinal; tolerances for interval/ratio).
*Anchors:* MM‑CHR units/evidence notion; Strict Distinction and the separation of objects from their descriptions/specs.


### C.16:8 - Integration with RSG & Dynamics (Normative/Clarifying)

#### C.16:8.1 - RSG (Role‑State Graph) touch‑points

MM‑CHR **supplies recognisers** used in **State Checklists**. A checklist criterion **may** refer to a measure (e.g., “Cohesion ≥ T on ordinal ladder”), but the **state itself remains intensional**; the checklist is its **description**, and a **StateAssertion** is an evidence‑backed verdict over a Window. No lifecycle language is implied; RSGs are open‑ended graphs with re‑entry edges.

**Rule RSG‑M1.** When a checklist cites a measure, it **SHALL** do so by **Characteristic + Scale semantics** (and unit if applicable), not by colloquial aliases; Tech/Formal registers apply. **Rule RSG‑M2.** Thresholds in checklists **MUST** respect the scale type (no ratio talk on interval scales; no arithmetic on ordinal ladders).

#### C.16:8.2 - Dynamics & CharacteristicSpace

`U.Dynamics.stateSpace` is a **CharacteristicSpace**—a named set of Characteristics with units/topology. MM‑CHR provides the **measurement side** of that space; architheories specify the **transition law**. Architectural or epistemic **dynamics** are then *trajectories in the declared CharacteristicSpace*. **No** procedural or storage commitments are implied.

### C.16:9 - Conformance Checklist (Normative)

> *Thought‑level acceptance conditions for authors and reviewers; they constrain meaning, not tooling.*

**CC‑MCHR‑1 - CSLC anchoring.** Each `U.DHCMethodRef` binds **exactly one** `U.Characteristic` and **exactly one** scale; each `U.Measure` carries a value valid for that scale (cf. A.18).
**CC‑MCHR‑2 - Polarity declared.** Every **ordered** scale in a template declares **polarity**; any **Score** via 𝒢 is monotone w\.r.t. that polarity.
**CC‑MCHR‑3 - Unit coherence.** Claims that compare or combine values are **grounded in unit coherence** (or declared conversions for interval/ratio).
**CC‑MCHR‑4 - Comparability honesty.** Ordered comparisons are asserted **only** when §7.2 holds; otherwise authors use qualitative/set‑level language.
**CC‑MCHR‑5 - Evidence sufficiency.** Where evidence is required by the template, the measure’s grounds are **conceptually sufficient** to retrace the claim; composition respects Σ‑laws (§8).
**CC‑MCHR‑6 - RSG alignment.** If a measure gates a **state** in an RSG, the checklist criteria **respect scale semantics** and the **intensional vs description** split. No lifecycle phrasing; use RSG open‑ended moves.
**CC‑MCHR‑7 - Dynamics awareness.** Where discussions involve change, the **CharacteristicSpace** is **named** (characteristics, units, topology) and separated from the **transition law** (architheory side).
**CC‑MCHR‑8 - Lexical guard‑rails.** Tech identifiers and headings use **Characteristic/Scale/Level/Value/Score/Unit/ScoringMethod**; aliases (axis/dimension/points/stars) appear **only** in explanatory Plain register with a first‑mention mapping to the Tech canon.

### C.16:10 - Invariants & Anti‑Patterns *(Normative unless marked “Informative”)*

#### C.16:10.1 - Invariants (N‑rules)

**N‑1 — One Characteristic + one Scale per template.**
Every `U.DHCMethodRef` binds *exactly one* **Characteristic** and *exactly one* **Scale** (its type + admissible range or level‑set). This is the CSLC sufficiency condition for interpretability.

**N‑2 — Value validity.**
A `U.Measure` holds a **Value** that is *admissible* for the template’s Scale (numeric range, categorical level); when a **Level** is used, it is among the named rungs declared for that Scale.

**N‑3 — Polarity is declared at the template.**
For ordered Scales, the template states the comparison direction (↑ better / ↓ better / target‑is‑best). Any **ScoringMethod mapping** to **Score** preserves that monotonic ordering. *(Note: we use “ScoringMethod mapping” instead of the Greek letter used elsewhere in FPF to avoid symbol conflicts.)*

**N‑4 — Unit coherence.**
Within one template there is one *primary* **Unit** of expression (or an explicit level‑set for non‑numeric Scales). Conversions are conceptually allowed only where the Scale supports meaningful arithmetic (interval/ratio); nominal/ordinal Scales are not subject to numeric conversions.

**N‑5 — Comparability guard.**
Two Measures are comparable *iff* they share the same template (hence, the same Characteristic + Scale + Unit) **or** stand in an explicit equivalence declared via the Unification suite (F‑cluster Bridges). Otherwise, comparability is not presumed.

**N‑6 — Evidence as conceptual anchoring.**
If a template requires it, each Measure includes an **EvidenceStub** that conceptually links the Value to its grounds; absence where required makes the Measure inadmissible for use. *(This is a conceptual obligation; no process mechanics are implied.)*

**N‑7 — Arity clarity.**
If the Characteristic is relational (applies to a pair/tuple), the subject of measurement is the relation itself; the reading must not be re‑described as a unary property of either participant.

**N‑8 — Open‑ended evolution; graph, not lifecycle.**
When MM‑CHR is used in change reasoning, movement happens in a **CharacteristicSpace** and along a reachable‑states graph (RSG). There is no lifecycle terminal; revisions may re‑enter earlier framing nodes as per A.17. *(Conceptual control structure only.)*


#### C.16:10.2 - Anti‑Patterns (A‑rules) — with cures

**A‑1 — Scale drift under the same template.**
*Smell:* the Scale meaning (bounds, categories) shifts while the template ID remains.
*Cure:* version the template; declare the relation in the Unification suite.

**A‑2 — Arithmetic on ordinal.**
*Smell:* averaging “stars” or ranking labels as if they were intervals.
*Cure:* either keep order‑respecting operations only, or introduce a **ScoringMethod** that defines a proper Score range.

**A‑3 — Unit soup.**
*Smell:* mixing milliseconds and seconds for the same template, or “%” and “points” for one Scale.
*Cure:* one primary Unit per template; conversions (when meaningful) are declared conceptually, not ad‑hoc.

**A‑4 — Alias leakage.**
*Smell:* “axis/dimension/point/ladder” in normative identifiers or headings.
*Cure:* use only canonical tokens in normative prose; narrative labels are allowed *solely* in Plain register with first‑mention mapping (A.17).

**A‑5 — Multi‑Characteristic stuffing.**
*Smell:* one template tries to carry a vector of Values for several Characteristics.
*Cure:* separate templates (one Characteristic each) and compose coordinates explicitly when needed.

**A‑6 — Evidence afterthought.**
*Smell:* Measures required to have grounds are introduced without an intelligible EvidenceStub.
*Cure:* treat the EvidenceStub as part of the measurement claim itself, not an accessory.

**A‑7 — Template mutation after Measures exist.**
*Smell:* retro‑editing Characteristic/Scale/Unit of an active template.
*Cure:* immutability of that triad post‑use; publish a successor template if the concept changes.

**A‑8 — Score‑of‑everything.**
*Smell:* collapsing heterogeneous Values into a single “points” Score without declared ScoringMethod and SCP.
*Cure:* retain the Value on its Scale; add an explicit ScoringMethod and SCP only when there is a justified need for a Score.

### C.16:11 - Cross‑Domain Vignettes *(Informative, transdisciplinary)*

> *Each vignette shows an CSLC‑conformant template → measure, without duplicating the A.17/A.18 glossaries.*

**V‑A (Architecture — relational property).**
Characteristic: **Coupling** (relational) between modules; Scale: ordinal {Low, Med, High}; Unit: level‑labels; Polarity: ↓ better.
Reading: subsystem pair ⟨M₁, M₂⟩ gets **Med**; **ScoringMethod** (optional) maps levels monotonically to a bounded Score for comparative dashboards.

**V‑B (Physics — interval/ratio).**
Characteristic: **ResponseTime**; Scale: ratio with non‑negative reals; Unit: seconds; Polarity: ↓ better.
Reading: subject S has **0.237 s**; comparability holds with any template that declares the same Characteristic+Scale+Unit (or an explicit equivalence).

**V‑C (Performing arts — ordinal).**
Characteristic: **EdgeControlQuality**; Scale: ordinal levels 1…5; Unit: level‑labels; Polarity: ↑ better.
Reading: performance P gets **4**; any aggregation uses a declared ScaleComplianceProfile (SCP) that respects order.

**V‑D (AI ethics — ratio).**
Characteristic: **ParityGap** (difference of positive rates); Scale: interval with symmetric bounds; Unit: percentage points; Polarity: ↓ better (0 is target).
Reading: model M on cohort C shows **3.2 pp**; evidence points conceptually to the derivation rationale (inputs, reference cohorts).

### C.16:12 - Relations & Placement *(Informative)*

**Kernel.** MM‑CHR *imports* the canonical Characteristic vocabulary and the CSLC discipline fixed by A.17 and A.18; it does not redefine them. CharacteristicSpace reasoning (for change) lives in the architheories that consume MM‑CHR readings.

**Using architheories.** KD‑CAL, Arch‑CAL and others *instantiate* templates and produce measures; MM‑CHR remains a neutral measurement substrate. Trade‑off analyses and architectural trajectories operate over coordinates that MM‑CHR makes available, not inside MM‑CHR.

**Unification (F‑cluster).** External standards (e.g., ISO 80000 quantity types; W3C SOSA/SSN observable properties; QUDT units/quantity kinds) are related via Concept‑Set rows and Bridges; MM‑CHR treats those alignments as context supplied by F‑patterns, not as local re‑definitions.

### C.16:End
