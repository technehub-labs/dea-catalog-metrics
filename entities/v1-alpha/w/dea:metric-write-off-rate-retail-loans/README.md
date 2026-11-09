# dea:metric-write-off-rate-retail-loans

Candidate Performance Metric record for **Write-Off Rate (Retail Loans)** (WORL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-write-off-rate-retail-loans`
- **Name:** Write-Off Rate (Retail Loans)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WORL

## 2. Definition

Within Retail Banking & Lending, Write-Off Rate (Retail Loans) (WORL) is used to gauge exposure to adverse outcomes. It is defined as Written-Off Loans / Average Gross Loans; the result is stated in percent (%). In Banking, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Write-off rate measures loans charged off as uncollectible, and it is the realized credit loss metric - the point where risk stops being a provision estimate and becomes a P&L fact. For retail loans, charge-off is conventionally at 180 days delinquent (credit cards) or 120 (installment), so it lags underwriting changes by many months and reflects conditions long past. That lag makes it a poor management signal on its own - which is why roll rates and delinquency lead it - but it is the comparator for pricing: APR levels must clear funding cost plus target loss plus opex. Read with net charge-off versus gross (recoveries matter in collections-intensive products), vintage charge-off curves, and provision coverage ratios for the forward-looking view.

## Formula

```
WORL = Written-Off Loans / Average Gross Loans
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 845 (batch 3)
