# dea:metric-architecture-decision-record-coverage

Candidate Performance Metric record for **Architecture Decision Record Coverage** (ADRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-architecture-decision-record-coverage`
- **Name:** Architecture Decision Record Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ADRC

## 2. Definition

Architecture Decision Record Coverage (ADRC) captures conformance to standards, plans, or obligations for organizations tracking software architecture & technical design. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Material Decisions with ADRs / Material Decisions; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of significant architecture decisions captured as records (context, options, rationale, consequences). ADRs are the institutional memory of software architecture: without them, the reasoning behind structural choices departs with the people who made them, and future decisions re-litigate or contradict settled wisdom unknowingly. Coverage should be judged by decision significance weighting, not raw counts. Read with decision-review cadence in architecture governance.

## Formula

```
Material Decisions with ADRs / Material Decisions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2620 (batch 7)
