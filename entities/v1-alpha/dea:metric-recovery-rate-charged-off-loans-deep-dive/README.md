# dea:metric-recovery-rate-charged-off-loans-deep-dive

Candidate Performance Metric record for **Recovery Rate (Charged-Off Loans Deep Dive)** (RRCL-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recovery-rate-charged-off-loans-deep-dive`
- **Name:** Recovery Rate (Charged-Off Loans Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RRCL-D

## 2. Definition

Recovery Rate (Charged-Off Loans Deep Dive) (RRCL-D) measures the economic value created or preserved in the Banking Retail Lending (Deep Dive) domain. The formula is Recovered Value / Charged-Off Value - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Banking sector.

## 3. Context

Measures principal recovered after charge-off, through collections, sale, or collateral. It is the tail-value metric of credit economics, and it is cyclical: recovery rates collapse in downturns precisely when charge-offs spike, compounding loss severity. Debt-sale prices and legal-recovery costs should be netted honestly. Read with charge-off trends and collateral revaluation currency for secured books.

## Formula

```
Recovered Value / Charged-Off Value
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** banking_retail_lending_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2082 (batch 6)
