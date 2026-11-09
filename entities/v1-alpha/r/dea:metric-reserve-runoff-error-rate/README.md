# dea:metric-reserve-runoff-error-rate

Candidate Performance Metric record for **Reserve Runoff Error Rate** (RRER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reserve-runoff-error-rate`
- **Name:** Reserve Runoff Error Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRER

## 2. Definition

Reserve Runoff Error Rate (RRER) addresses the quality of outputs and outcomes and is a fixture of actuarial & reserving reporting. It is defined as Absolute Reserve Error at Runtime / Original Reserve; the result is stated in percent (%). In Insurance, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the error in estimates as loss cohorts run off to ultimate, tracking deviation magnitude and direction over the development cycle. It is the precision companion to reserve development ratio, exposing systematic bias that ratios can mask in aggregate. Watch for error asymmetry across economic cycles, since soft-market years mask adverse bias. Read with IBNR accuracy ratio and loss trend estimation error.

## Formula

```
RRER = Absolute Reserve Error at Runtime / Original Reserve
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1531 (batch 6)
