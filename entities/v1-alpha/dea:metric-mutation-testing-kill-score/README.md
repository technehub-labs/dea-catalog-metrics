# dea:metric-mutation-testing-kill-score

Candidate Performance Metric record for **Mutation Testing Kill Score** (MTKS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mutation-testing-kill-score`
- **Name:** Mutation Testing Kill Score
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MTKS

## 2. Definition

Mutation Testing Kill Score (MTKS) captures the quality of outputs and outcomes for organizations tracking software testing & quality engineering. The formula is Mutants Killed by Test Suite / Mutants Introduced - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the proportion of deliberately injected code faults that existing tests actually catch. It is the most honest test of your tests: high line coverage with a low kill score means suites assert little of substance. Full mutation runs are computationally expensive, so coverage is often sampled and read directionally. Read with test automation coverage.

## Formula

```
Mutants Killed by Test Suite / Mutants Introduced
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_testing_quality_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2720 (batch 7)
