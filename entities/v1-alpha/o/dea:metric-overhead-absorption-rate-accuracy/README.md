# dea:metric-overhead-absorption-rate-accuracy

Candidate Performance Metric record for **Overhead Absorption Rate Accuracy** (OARA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overhead-absorption-rate-accuracy`
- **Name:** Overhead Absorption Rate Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OARA

## 2. Definition

Overhead Absorption Rate Accuracy (OARA) captures the quality of outputs and outcomes for organizations tracking product costing & margin management. It is defined as 1 - ABS(Absorbed Overhead - Actual Overhead) / Actual Overhead; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how closely absorbed overhead matches actual overhead incurred. It matters because absorption error silently distorts product cost and inventory valuation. Absorption can be tuned by adjusting activity denominators to absorb overhead cleanly. Read with Cost Variance to Standard and standard cost revision history to confirm absorption reflects reality.

## Formula

```
OARA = 1 - ABS(Absorbed Overhead - Actual Overhead) / Actual Overhead
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_costing_margin_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1246 (batch 4)
