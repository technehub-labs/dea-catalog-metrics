# dea:metric-collateral-revaluation-currency

Candidate Performance Metric record for **Collateral Revaluation Currency** (CRC-B) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-collateral-revaluation-currency`
- **Name:** Collateral Revaluation Currency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRC-B

## 2. Definition

A Banking Retail Lending (Deep Dive) indicator, Collateral Revaluation Currency (CRC-B) quantifies conformance to standards, plans, or obligations. It is defined as Collateral Valuations within Policy Cycle / Portfolio; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Banking, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of collateral with valuations within policy refresh cycles. In secured lending, stale collateral values silently inflate security coverage and distort loss-given-default, and house-price or vehicle-price drift makes currency a material risk question. Automated valuation methods change refresh economics, but methodology consistency matters for LGD modeling. Read with loan-to-value distributions and recovery rate (Charged-Off Loans Deep Dive) evidence.

## Formula

```
CRC-B = Collateral Valuations within Policy Cycle / Portfolio
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2084 (batch 6)
