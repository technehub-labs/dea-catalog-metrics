OpenDEAM Metric — Strategic CR and ADR Roadmap

We will be treating Metric as a dedicated metamodel development initiative, not just a collection of Metric entities.

The objective should be to establish a complete, governed measurement capability within OpenDEAM: one that can describe what an enterprise measures, how it measures it, what results it obtains, how those results are interpreted, and how they inform enterprise decisions.

There is already a foundation to build upon. In particular, the earlier CR-10J work established Metric as a reusable semantic object with attributes including definition, unit, calculation, source, baseline and target. The CR-10 Outcome concept also incorporated metric, baseline, expected outcome, target, unit, confidence, timeframe and evidence.

We should preserve that work, not create a competing measurement model.

1. Strategic positioning

First, I would establish five architectural principles.

Principle	Architectural position
Metric is foundational	A reusable, first-class metamodel entity.
Measurement is distinct	A Metric defines what and how to measure; Measurement represents the execution or application of that definition.
Results are distinct	An Observation captures the resulting value and its context.
Interpretation is distinct	Assessment interprets observations against targets, thresholds, criteria and expectations.
Measurement is cross-domain	Metrics can be associated with virtually any relevant OpenDEAM entity.

The distinction between these concepts is important because OpenDEAM is intended to become a semantic foundation, enterprise knowledge graph, runtime services platform and decision-intelligence interface.

Consequently, Metric must support both descriptive architecture and operational intelligence.

2. Repository and organizational ownership

We should respect the existing OpenDEAM authority boundaries.

Repository / authority	Responsibility
dea-metamodel	Canonical Metric, Measurement, Observation and related entity definitions, relationships and constraints.
dea-architecture-framework	Positioning and allocation of measurement concepts within the OpenDEAM architecture.
dea-governance	Governance, ownership, identity, lifecycle, conformance and change control.
New Metric catalog repository	Canonical Metric instances and reusable Metric definitions.
Future measurement data repository/service	Measurement executions, observations and historical results, subject to runtime architecture decisions.

An important distinction: the metamodel owns the semantics; catalogs own reusable instances; runtime services own execution and operational measurement data.

We should not prematurely put all measurement records into the Metric catalog.

3. Proposed CR programme

I propose twelve Change Requests, organized into six phases. The identifiers below are proposed initiative-level identifiers, not assertions that these records already exist in the repository.

Metric development programme

* Phase 1 — Semantic foundation
    CR-MET-001–002
    Establish the Metric concept, boundaries, semantics and relationship to existing OpenDEAM concepts.
* Phase 2 — Measurement architecture
    CR-MET-003–004
    Establish Measurement, Observation and the measurement execution lifecycle.
* Phase 3 — Measurement semantics
    CR-MET-005–006
    Establish units, formulas, targets, baselines, thresholds and interpretation.
* Phase 4 — Enterprise integration
    CR-MET-007–008
    Integrate measurement with enterprise architecture, performance, capabilities, processes, strategy and maturity.
* Phase 5 — Catalog and governance
    CR-MET-009–010
    Establish the Metric catalog, documentation standards, identity, lifecycle and conformance.
* Phase 6 — Runtime and intelligence
    CR-MET-011–012
    Enable measurement provenance, temporal analysis, aggregation, analytics and decision intelligence.

Phase 1 — Semantic foundation

CR-MET-001: Establish the Canonical Metric Entity

Objective: Formalize Metric as a first-class OpenDEAM metamodel entity.

Scope:

* Canonical identity and naming.
* Definition and description.
* Measurement purpose and intended use.
* Subject or phenomenon being measured.
* Measurement unit.
* Calculation or determination method.
* Measurement source.
* Measurement frequency.
* Applicability and scope.
* Ownership and stewardship.
* Lifecycle and versioning.
* Relationship to existing Metric definitions, particularly CR-10J.

Deliverable: Canonical Metric entity specification and schema.

CR-MET-002: Establish Metric Classification and Taxonomy

Objective: Provide a consistent classification system for metrics across enterprise domains.

Proposed classification dimensions:

Classification	Examples
Measurement subject	Organization, capability, process, service, technology
Measurement purpose	Performance, efficiency, effectiveness, quality, risk
Measurement perspective	Financial, customer, operational, organizational, technical
Measurement orientation	Leading, lagging, diagnostic
Measurement scope	Enterprise, domain, business unit, process
Measurement nature	Quantitative, qualitative, composite

An important distinction is that these are classification dimensions, not necessarily separate subclasses of Metric.

Phase 2 — Measurement architecture

CR-MET-003: Establish Measurement and Observation Entities

Objective: Separate metric definitions from their actual application and results.

Establish:

* Measurement: the execution or application of a Metric.
* Observation: the recorded result.
* Observation timestamp and reporting period.
* Observed value and unit.
* Subject reference.
* Evidence and provenance.
* Measurement context.
* Quality and confidence indicators.

The relationship should support multiple observations for one Metric across different subjects and periods.

CR-MET-004: Establish Measurement Lifecycle and Execution Semantics

Objective: Define how measurement happens within OpenDEAM.

Cover:

* Measurement initiation.
* Collection and extraction.
* Calculation and transformation.
* Validation.
* Recording.
* Publication.
* Reconciliation.
* Correction and supersession.
* Measurement failures and exceptions.

This CR should also distinguish automated, system-generated, human-recorded and externally supplied measurements.

Phase 3 — Measurement semantics

CR-MET-005: Establish Measurement Units, Formulas and Aggregation Semantics

Objective: Ensure that measurements are mathematically meaningful and comparable.

Cover:

* Units and dimensions.
* Unit conversion.
* Formula definitions.
* Numerators and denominators.
* Aggregation methods.
* Measurement precision.
* Rounding rules.
* Normalization.
* Composite metrics.
* Ratios, percentages, rates and indices.
* Additive versus non-additive metrics.

For example, averaging individual customer satisfaction scores is not necessarily equivalent to calculating a weighted enterprise satisfaction score.

The metamodel must preserve that distinction.

CR-MET-006: Establish Baseline, Target, Threshold and Performance Interpretation

Objective: Define how metric results are evaluated.

This should explicitly investigate whether the following should be first-class entities or contextualized supporting objects:

* Baseline.
* Target.
* Threshold.
* Benchmark.
* Expected value.
* Tolerance.
* Performance range.
* Variance.
* Direction of improvement.
* Assessment criteria.

We should avoid embedding all these concepts directly into Metric as static attributes.

A Metric can have different targets, baselines and thresholds depending on its subject, organizational scope, reporting period and strategic context.

For example, an 8% employee turnover target might be appropriate for one organizational context but inappropriate for another.

Phase 4 — Enterprise integration

CR-MET-007: Establish Metric-to-Enterprise Entity Relationships

Objective: Make Metric usable throughout the OpenDEAM semantic architecture.

Explicitly establish relationships with:

* Strategic objectives.
* Business capabilities.
* Business functions.
* Business processes (including Activities, and Tasks).
* Value streams.
* Organizational units.
* Products and services.
* Information systems.
* Information system components.
* Data entities.
* Risks and controls.
* Organizational pillars.
* DMM dimensions and maturity assessments.

This CR should define relationship directionality, cardinality, semantics and constraints.

CR-MET-008: Establish KPI, KRI and Performance Indicator Semantics

Objective: Differentiate general metrics from metrics designated for specific management purposes.

The CR should investigate:

Concept	Purpose
Metric	General measurement definition
KPI	Key performance indicator
KRI	Key risk indicator
KCI	Key control indicator
SLA indicator	Service-level performance
Operational indicator	Operational performance
Leading indicator	Signals potential future outcomes
Lagging indicator	Records achieved outcomes

My initial recommendation is that KPI, KRI and KCI should be modeled as governed metric classifications or specializations only where their semantics genuinely justify it, rather than automatically creating independent entity types.

Phase 5 — Catalog and governance

CR-MET-009: Establish the DEA Metric Catalog Repository

Objective: Establish the authoritative catalog for reusable Metric definitions.

The new repository should follow the existing DEA catalog conventions.

Expected repository assets:

* Repository README.
* Catalog scope and positioning.
* Metric classification taxonomy.
* Metric entity templates.
* Metric definition documentation.
* Canonical identifiers.
* Entity metadata.
* Relationship declarations.
* Examples and reference implementations.
* Validation and conformance rules.
* Contribution and lifecycle guidance.

CR-MET-010: Establish Metric Governance, Quality and Conformance

Objective: Ensure that Metric definitions and observations are trustworthy and maintainable.

Cover:

* Metric ownership and stewardship.
* Definition approval.
* Versioning and deprecation.
* Duplicate detection.
* Semantic consistency.
* Measurement quality.
* Data quality.
* Provenance.
* Evidence requirements.
* Conformance validation.
* Governance responsibilities.
* Change management.

This should align with the existing DEA governance authority and its canonical entity and relationship contracts.

Phase 6 — Runtime and intelligence

CR-MET-011: Establish Metric Temporal, Provenance and Measurement History

Objective: Enable longitudinal measurement and traceability.

Cover:

* Effective dates.
* Observation timestamps.
* Reporting periods.
* Historical values.
* Corrections and supersession.
* Source lineage.
* Calculation lineage.
* Version-specific metric definitions.
* Historical baseline and target changes.
* Reproducibility.

This is essential for meaningful enterprise performance and transformation analysis.

CR-MET-012: Establish Measurement Analytics and Decision Intelligence Integration

Objective: Enable OpenDEAM to use measurement information for enterprise intelligence.

Cover:

* Metric aggregation across organizational boundaries.
* Performance trends.
* Variance and deviation analysis.
* Correlation and causal analysis.
* Forecasting.
* Scenario comparison.
* Simulation inputs and outputs.
* Outcome tracking.
* Decision evidence.
* AI-assisted metric interpretation.

This should extend the earlier CR-10 scenario and decision-intelligence foundation rather than duplicate it.

4. Proposed Architecture Decision Records

The CRs define what needs to be built. ADRs establish the architectural decisions that constrain how it should be built.

I recommend a dedicated Metric ADR series, cross-referenced with the existing OpenDEAM ADR register.

ADR	Proposed title	Decision to resolve
ADR-MET-001	Metric as a First-Class Entity	Canonical semantic positioning
ADR-MET-002	Metric vs Measurement vs Observation	Separation of definitions, execution and results
ADR-MET-003	Metric Classification Architecture	Taxonomy versus entity specialization
ADR-MET-004	Measurement Subject and Context	How metrics reference what they measure
ADR-MET-005	Measurement Unit and Dimensionality	Units, dimensions and conversions
ADR-MET-006	Formula and Calculation Semantics	Formula representation and reproducibility
ADR-MET-007	Baseline, Target and Threshold Architecture	Independent entities versus contextual objects
ADR-MET-008	KPI, KRI and KCI Representation	Classification versus specialization
ADR-MET-009	Metric Relationship Architecture	Cross-domain semantic relationships
ADR-MET-010	Measurement Evidence and Provenance	Evidence, source lineage and trust
ADR-MET-011	Temporal Measurement Architecture	Historical and effective-time semantics
ADR-MET-012	Measurement Quality and Confidence	Quality, validity and confidence models
ADR-MET-013	Composite Metrics and Aggregation	Mathematical and semantic aggregation
ADR-MET-014	Metric Governance and Lifecycle	Ownership, versioning and deprecation
ADR-MET-015	Runtime Measurement Architecture	Collection, execution and publication
ADR-MET-016	Metric Analytics and Decision Intelligence	Analytical and decision integration

These should be actual decision records, with context, options considered, decision, rationale, consequences, status and supersession references.

5. OpenDEAM organizational and repository establishment

There is an additional dimension I would not leave until the end: establishing the organizational and technical ownership of the Metric capability.

We should treat this as a proper OpenDEAM domain capability, not merely another catalog.

I recommend the following ownership model:

OpenDEAM organizational architecture

OpenDEAM Architecture Authority

Positioning, architectural alignment and cross-domain consistency

Metamodel Authority

Canonical semantics, entity definitions, relationships and schemas.

Metric Domain Stewardship

Metric taxonomy, definition standards, classification and semantic quality.

Catalog Stewardship

Reusable metric definitions, instances and documentation.

Runtime and Intelligence

Measurement execution, observations, analytics and intelligence services.

DEA Governance Authority

Identity, lifecycle, conformance, change control and organizational accountability

I would not necessarily establish a separate organizational unit immediately. The first CR should determine whether Metric Domain Stewardship is a formal OpenDEAM organizational role, working group or delegated responsibility.

Proposed repository establishment

Repository	Purpose
dea-metamodel	Canonical Metric-related metamodel
dea-architecture-framework	Architecture allocation and integration
dea-governance	Governance and conformance
dea-catalog-metrics	Reusable Metric definitions
Future measurement runtime repository	Operational measurement and observation services

The Metric catalog should be established only after its canonical entity contract is sufficiently stable.

6. CI/CD and automated conformance

The new Metric capability should participate in the existing repository automation rather than introduce a parallel tooling ecosystem.

The CRs should progressively establish:

* Schema validation for Metric definitions.
* Canonical identity validation.
* Required metadata validation.
* Classification validation.
* Relationship integrity checks.
* Unit and formula validation.
* Documentation completeness checks.
* Duplicate and semantic consistency checks.
* Cross-repository reference validation.
* Versioning and lifecycle checks.
* Catalog conformance reporting.
* Automated publication of validated registry artifacts.

The output should integrate with existing metamodel registry generation, including relationship registry outputs.

Importantly, runtime observation validation should be distinguishable from static catalog validation. They have different operational requirements.

7. Recommended ADR-to-CR execution dependencies

The following sequence avoids making implementation decisions before the underlying semantics are agreed.

Stage	ADRs	CRs
Foundation	001–004	001–002
Measurement model	005–006	003–005
Interpretation	007–008	006
Integration	009	007–008
Catalog and governance	010, 012, 014	009–010
Runtime and intelligence	011, 013, 015–016	011–012

ADRs should be approved before their corresponding implementation decisions become binding. Some can be developed in parallel, but their dependencies must be respected.

8. Additional cross-cutting considerations

I would also require the programme to explicitly evaluate these issues, rather than assume they are covered by the twelve CRs.

Area	Required consideration
Semantic interoperability	Mapping to established measurement and indicator vocabularies
Data architecture	Metric definitions versus actual measurement datasets
Security	Access restrictions and sensitive measurement information
Organizational context	Organizational hierarchies and changing measurement scope
Comparability	Whether two observations are genuinely comparable
Measurement uncertainty	Confidence, estimation and uncertainty
Qualitative measurement	Non-numeric assessments and ordinal scales
Composite measures	Weighted indices and multidimensional scoring
AI readiness	Machine-readable definitions and calculation semantics
Auditability	Reconstructing how a reported value was produced

One particularly important issue is qualitative measurement. OpenDEAM must not assume that everything measurable is numeric. Maturity levels, categorical assessments and ordinal ratings also require rigorous measurement semantics.

9. Recommended programme acceptance gates

I would establish five gates before declaring the Metric capability mature.

* Gate 1 — Semantic completeness
    Metric, Measurement and Observation are unambiguously defined, with no duplication of existing concepts.
* Gate 2 — Metamodel integrity
    Entity schemas, relationships, constraints and registry generation are validated.
* Gate 3 — Catalog readiness
    A Metric catalog exists with reusable, documented and validated definitions.
* Gate 4 — Measurement readiness
    Measurement execution, observation history, provenance, quality and interpretation are demonstrable.
* Gate 5 — Enterprise intelligence readiness
    Metric information can support cross-domain analysis, performance management, scenario evaluation and decision intelligence.

10. My recommended immediate execution sequence

I would not start by generating all twelve CRs as independent implementation instructions. That risks creating overlapping definitions and unnecessary rework.

Instead:

Order	Deliverable	Priority
1	CR-MET-000 — Metric Capability Establishment and Existing Work Reconciliation	Foundation
2	ADR-MET-001–004	Architecture
3	CR-MET-001–002	Metamodel
4	ADR-MET-005–008	Measurement semantics
5	CR-MET-003–006	Measurement model
6	ADR-MET-009	Integration
7	CR-MET-007–008	Enterprise integration
8	ADR-MET-010, 012, 014	Governance
9	CR-MET-009–010	Catalog
10	ADR-MET-011, 013, 015–016	Runtime architecture
11	CR-MET-011–012	Intelligence

One particularly important first step: CR-MET-000

Before implementation, CR-MET-000 should perform a structured reconciliation of:

* Existing Metric definitions in dea-metamodel.
* The earlier CR-10J Metric specification.
* Metric references within the CR-10 Outcome model.
* Existing ADR-001–012 and their decisions.
* Existing governance requirements, including DEA-ID-000 and CR-012.
* Existing registry, schema and CI/CD conventions.
* Any existing Metric-related entities, classifications or relationships in the catalog repositories.

It should produce an explicit disposition for each discovery:

RETAIN, EXTEND, REFACTOR, CONSOLIDATE, DEPRECATE or INTRODUCE.

This prevents the new programme from inadvertently creating a second, incompatible measurement architecture.

Final architectural recommendation

Recommended direction

Establish Metric as an OpenDEAM foundational semantic capability, with a governed definition layer, an operational measurement layer, and an analytical interpretation layer.

The resulting architecture should look conceptually like this:

OpenDEAM Measurement Architecture

1. Measurement Definition Layer

Metric · Metric Classification · Unit · Formula · Measurement Method · Target · Baseline · Threshold

2. Measurement Execution Layer

Measurement · Collection · Calculation · Validation · Execution Context

3. Measurement Evidence Layer

Observation · Evidence · Provenance · Confidence · Quality · History

4. Measurement Intelligence Layer

Assessment · Performance Analysis · KPI/KRI · Benchmarking · Forecasting · Simulation · Decision Intelligence

CROSS-CUTTING THROUGH ALL FOUR LAYERS

OpenDEAM Identity · Relationships · Governance · Security · Temporal Semantics · Interoperability

This also gives us an important architectural separation: DMM can consume and interpret Metric and Observation information without owning the underlying measurement semantics. Similarly, performance management, risk management and operational intelligence can reuse the same foundation.

The ultimate objective is for OpenDEAM to have a measurement vocabulary that is independent of any single management framework, yet sufficiently expressive to support all of them.

I would make CR-MET-000 the first formal deliverable and use its findings to lock the scope and dependencies of CR-MET-001 through CR-MET-012 before implementation begins.