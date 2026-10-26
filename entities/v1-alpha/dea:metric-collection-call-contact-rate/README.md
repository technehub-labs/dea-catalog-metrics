# dea:metric-collection-call-contact-rate

Candidate Performance Metric record for **Collection Call Contact Rate** (CCCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-collection-call-contact-rate`
- **Name:** Collection Call Contact Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCCR

## 2. Definition

Within Accounts Payable & Receivable Operations (Deep Dive), Collection Call Contact Rate (CCCR) is used to gauge how efficiently resources are converted into outputs. It is defined as Debtors Contacted per Dunning Schedule / Debtors Due; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Debtors Contacted per Dunning Schedule / Debtors Due
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3810 (batch 8)
