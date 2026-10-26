# dea:metric-cost-per-invoice-processed

Candidate Performance Metric record for **Cost per Invoice Processed** (CPIP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-invoice-processed`
- **Name:** Cost per Invoice Processed
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPIP

## 2. Definition

Within Finance & Accounting, Cost per Invoice Processed (CPIP) is used to gauge how efficiently resources are converted into outputs. It provides the day-to-day signal that a process is running as designed. Its calculation is Total Invoice Processing Cost / Invoices Processed, measured in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Total Invoice Processing Cost / Invoices Processed
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 30 (batch 1)
