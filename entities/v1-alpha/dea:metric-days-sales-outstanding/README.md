# dea:metric-days-sales-outstanding

Candidate Performance Metric record for **Days Sales Outstanding** (DSO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-days-sales-outstanding`
- **Name:** Days Sales Outstanding
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DSO

## 2. Definition

Days Sales Outstanding (DSO) addresses how efficiently resources are converted into outputs and is a fixture of finance & accounting reporting. Its calculation is (Accounts Receivable / Revenue) x 365, measured in days. It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the average number of days it takes to collect revenue after a sale. It matters because receivables are effectively interest-free loans to customers and slow collection strains cash. Teams can cut it by factoring receivables or offering steep early-payment discounts that quietly erode margin. Read with Accounts Receivable Turnover and Cash Conversion Cycle to check whether collection gains are real or bought.

## Formula

```
DSO = (Accounts Receivable / Revenue) x 365
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 23 (batch 1)
