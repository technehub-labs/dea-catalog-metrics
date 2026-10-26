# dea:metric-database-lock-cycle-time

Candidate Performance Metric record for **Database Lock Cycle Time** (DBLC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-database-lock-cycle-time`
- **Name:** Database Lock Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DBLC

## 2. Definition

Database Lock Cycle Time (DBLC) addresses how efficiently resources are converted into outputs and is a fixture of pharma r&d & clinical trials reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Days from Last Patient Visit to Database Lock - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Pharmaceuticals sector.

## 3. Context

Measures time from last-patient-out (or data cutoff) to clinical database lock in trials. It sits on the critical path of every submission: late locks delay analysis, submission, and ultimately time-to-patient. Errors that surface at lock (rescue-driven, not process-driven) predict data quality problems upstream, so track both speed and post-lock correction rates. Read with query resolution cycle time and submission acceptance rate.

## Formula

```
Days from Last Patient Visit to Database Lock
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1612 (batch 6)
