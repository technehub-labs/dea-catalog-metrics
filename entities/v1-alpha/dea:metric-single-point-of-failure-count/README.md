# dea:metric-single-point-of-failure-count

Candidate Performance Metric record for **Single Point of Failure Count** (SPOF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-single-point-of-failure-count`
- **Name:** Single Point of Failure Count
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SPOF

## 2. Definition

Single Point of Failure Count (SPOF) measures exposure to adverse outcomes in the Business Resilience & Continuity domain. It is defined as Identified Unremediated Single Points of Failure; the result is stated in count (items per period). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the number of components - systems, suppliers, sites, people, network paths - whose failure alone halts a critical service. It is the tersest architectural risk metric, and its trendline tells whether resilience is being engineered in or documented over. Counting honesty depends on criticality scoping, and SPOFs discovered only in incidents suggest the inventory is stale. Read with supplier continuity assurance coverage and key-person dependency ratio.

## Formula

```
Identified Unremediated Single Points of Failure
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_resilience_continuity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1412 (batch 5)
