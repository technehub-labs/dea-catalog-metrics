# dea:metric-non-standard-clause-exception-rate

Candidate Performance Metric record for **Non-Standard Clause Exception Rate** (NSCER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-non-standard-clause-exception-rate`
- **Name:** Non-Standard Clause Exception Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NSCER

## 2. Definition

Non-Standard Clause Exception Rate (NSCER) captures exposure to adverse outcomes for organizations tracking contract lifecycle management. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Clause Deviations Approved / Contracts - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Clause Deviations Approved / Contracts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contract_lifecycle_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3699 (batch 8)
