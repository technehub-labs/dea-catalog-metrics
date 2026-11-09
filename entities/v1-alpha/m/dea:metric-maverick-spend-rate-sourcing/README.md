# dea:metric-maverick-spend-rate-sourcing

Candidate Performance Metric record for **Maverick Spend Rate (Sourcing)** (MSR-SS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maverick-spend-rate-sourcing`
- **Name:** Maverick Spend Rate (Sourcing)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MSR-SS

## 2. Definition

A Strategic Sourcing & Supplier Performance (Deep Dive) indicator, Maverick Spend Rate (Sourcing) (MSR-SS) quantifies conformance to standards, plans, or obligations. Its calculation is Spend outside Approved Channels / Total Spend, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of addressable spend bypassing sourcing channels and contracts. Maverick spend pays full price for unmanaged risk. Rates falling through threat rather than service improvement relocate, not reduce, leakage. Read with managed spend under contract and spend under management ratio.

## Formula

```
MSR-SS = Spend outside Approved Channels / Total Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** strategic_sourcing_supplier_performance_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3744 (batch 8)
