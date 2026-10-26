# dea:metric-process-safety-incidents-chemicals

Candidate Performance Metric record for **Process Safety Incidents (Chemicals)** (PSIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-safety-incidents-chemicals`
- **Name:** Process Safety Incidents (Chemicals)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PSIC

## 2. Definition

Process Safety Incidents (Chemicals) (PSIC) measures exposure to adverse outcomes in the Chemicals domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Tier 1 and Tier 2 Process Safety Events per Period; the result is stated in count (items per period). It should be driven down, since lower readings signal healthier performance. In Chemicals, it is a recognized element of the standard performance toolkit.

## 3. Context

Process safety incidents in chemicals count loss-of-containment events, fires, and explosions - the catastrophic-risk failures distinct from slips and falls, and the industry metric that carries the weight of Bhopal's legacy. Chemical process safety incidents follow the well-documented degradation pattern: normal operating procedures drift, safety systems get bypassed for production, and near-miss reporting fades, well before an event occurs. The count is low-frequency by nature, so year-over-year trend is statistically noisy for a single site - multi-year and multi-site aggregation is the honest read. Read with mechanical integrity program completion, safety instrumented system testing compliance, management-of-change execution, and near-miss reporting rates as leading indicators.

## Formula

```
Tier 1 and Tier 2 Process Safety Events per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 898 (batch 3)
