# dea:metric-days-payable-outstanding

Candidate Performance Metric record for **Days Payable Outstanding** (DPO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-days-payable-outstanding`
- **Name:** Days Payable Outstanding
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DPO

## 2. Definition

Within Finance & Accounting, Days Payable Outstanding (DPO) is used to gauge how efficiently resources are converted into outputs. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is (Accounts Payable / Cost of Goods Sold) x 365 - reported in days. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the average number of days a firm takes to pay its suppliers. It matters because longer terms are a free source of financing, but over-extension damages supplier relationships and credit terms. Gaming risk includes delaying payments into the next period purely to flatter working capital metrics. Read with Cash Conversion Cycle and Supplier On-Time Delivery to see whether stretched payments are hurting supply reliability.

## Formula

```
DPO = (Accounts Payable / Cost of Goods Sold) x 365
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 24 (batch 1)
