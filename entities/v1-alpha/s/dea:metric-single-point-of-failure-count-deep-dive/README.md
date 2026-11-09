# dea:metric-single-point-of-failure-count-deep-dive

Candidate Performance Metric record for **Single Point of Failure Count (Deep Dive)** (SPOFC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-single-point-of-failure-count-deep-dive`
- **Name:** Single Point of Failure Count (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPOFC

## 2. Definition

Single Point of Failure Count (Deep Dive) (SPOFC) addresses exposure to adverse outcomes and is a fixture of software architecture & technical design reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Architectural Single Points of Failure in Production, measured in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures components whose failure alone halts critical services - systems, dependencies, network paths, and key people. It is the tersest resilience metric in architecture reviews, and its trend reveals whether redundancy is being engineered in or documented around. Criticality-weighting matters, since an SPOF in a demo environment and one in payment processing are not the same count. Read with service dependency mapping currency and failover test evidence.

## Formula

```
SPOFC = Architectural Single Points of Failure in Production
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_architecture_technical_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2637 (batch 7)
