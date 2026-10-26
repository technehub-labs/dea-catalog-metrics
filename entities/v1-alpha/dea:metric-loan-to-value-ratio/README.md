# dea:metric-loan-to-value-ratio

Candidate Performance Metric record for **Loan-to-Value Ratio** (LTV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loan-to-value-ratio`
- **Name:** Loan-to-Value Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LTV

## 2. Definition

Loan-to-Value Ratio (LTV) addresses exposure to adverse outcomes and is a fixture of banking & financial services reporting. The formula is Loan Amount / Collateral Value - reported in percent (%). It is a standard measure in the Financial services sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the loan amount as a percentage of the collateral value at origination. It matters as the primary buffer protecting the lender if the borrower defaults. Gaming risk includes inflated appraisals or valuation timing tricks that understate true exposure at booking. Read with Debt Service Coverage Ratio and Delinquency Rate to track whether origination discipline holds through the cycle.

## Formula

```
Loan Amount / Collateral Value
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 38 (batch 1)
