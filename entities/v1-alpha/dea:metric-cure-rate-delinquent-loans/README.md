# dea:metric-cure-rate-delinquent-loans

Candidate Performance Metric record for **Cure Rate (Delinquent Loans)** (CRDL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cure-rate-delinquent-loans`
- **Name:** Cure Rate (Delinquent Loans)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRDL

## 2. Definition

A Banking Retail Lending (Deep Dive) indicator, Cure Rate (Delinquent Loans) (CRDL) quantifies the economic value created or preserved. It is defined as Accounts Returning to Current / Delinquent Accounts; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Banking, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of delinquent borrowers returning to current status. It is the effectiveness metric of collections treatment: cure rates reveal which early-stage interventions work, and they set the economics of how far into delinquency a lender should invest. Cure through refinancing or term extension that merely postpones loss is a measurement trap. Read with roll-rate transitions and redefault rates among cured accounts.

## Formula

```
Accounts Returning to Current / Delinquent Accounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2081 (batch 6)
