# dea:metric-ci-compute-cost-per-build

Candidate Performance Metric record for **CI Compute Cost per Build** (CICPB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ci-compute-cost-per-build`
- **Name:** CI Compute Cost per Build
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CICPB

## 2. Definition

Within Continuous Integration, CI Compute Cost per Build (CICPB) is used to gauge how efficiently resources are converted into outputs. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is CI Infrastructure Cost / Builds - reported in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CI Infrastructure Cost / Builds
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2670 (batch 7)
