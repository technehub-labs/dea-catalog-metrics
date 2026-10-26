# dea:metric-architecture-roadmap-realization

Candidate Performance Metric record for **Architecture Roadmap Realization** (ARR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-architecture-roadmap-realization`
- **Name:** Architecture Roadmap Realization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ARR

## 2. Definition

Within Enterprise Architecture, Architecture Roadmap Realization (ARR) is used to gauge conformance to standards, plans, or obligations. Its calculation is Roadmap Milestones Delivered / Milestones Planned, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures delivery of committed architecture roadmap milestones - capability launches, migrations, retirements - against plan and value. It keeps architecture from becoming a slides-only discipline, and gives the CIO an execution scorecard beyond project counts. Beware milestone definitions drifting to declare success, and realization measured on the roadmap that was last edited to match reality. Read with technical debt remediation rate and legacy system migration progress.

## Formula

```
Roadmap Milestones Delivered / Milestones Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** enterprise_architecture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1352 (batch 5)
