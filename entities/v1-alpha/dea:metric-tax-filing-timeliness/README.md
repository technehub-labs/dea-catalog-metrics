# dea:metric-tax-filing-timeliness

Candidate Performance Metric record for **Tax Filing Timeliness** (TFT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tax-filing-timeliness`
- **Name:** Tax Filing Timeliness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TFT

## 2. Definition

A Tax & Fiscal indicator, Tax Filing Timeliness (TFT) quantifies conformance to standards, plans, or obligations. The formula is Filings Submitted by Deadline / Filings Due - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of tax filings submitted by statutory deadlines. It matters because late filings trigger penalties and scrutiny that lasts years. Teams can game it by counting extensions as timely, which is true for filing but not for exposure. Read with Tax Audit Adjustment Ratio and penalty history to confirm timeliness reflects genuine compliance discipline.

## Formula

```
TFT = Filings Submitted by Deadline / Filings Due
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** tax_fiscal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 605 (batch 2)
