# dea:metric-contract-compliance-rate

Candidate Performance Metric record for **Contract Compliance Rate** (CCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contract-compliance-rate`
- **Name:** Contract Compliance Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCR

## 2. Definition

Contract Compliance Rate (CCR) measures conformance to standards, plans, or obligations in the Procurement domain. The formula is Purchases via Contract / Total Addressable Purchases - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of purchases executed per agreed contract terms and pricing. It matters because off-contract buying erodes negotiated savings and audit control. It can be gamed by loosely defining what counts as compliant or by retroactively applying contracts to maverick buys. Read with Maverick Spend Rate and Purchase Price Variance to test whether contract discipline is real.

## Formula

```
Purchases via Contract / Total Addressable Purchases
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** procurement

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 226 (batch 1)
