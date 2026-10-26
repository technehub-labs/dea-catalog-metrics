# dea:metric-expense-ratio

Candidate Performance Metric record for **Expense Ratio** (ExR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-expense-ratio`
- **Name:** Expense Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ExR

## 2. Definition

Expense Ratio (ExR) measures how efficiently resources are converted into outputs in the Insurance domain. The formula is Underwriting Expenses / Earned Premiums - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Insurance sector.

## 3. Context

Underwriting and administrative expenses over earned premium - the cost side of the insurance combined ratio, capturing everything except claims: commissions, staff, technology, and the overhead of distribution. Where the loss ratio diagnoses risk selection, the expense ratio diagnoses operating model, and its structure varies systematically with distribution: direct writers can run well below 10 percent while commission-heavy agency models run near 20 without either being mismanaged. The strategic lever is the second-order one: spending on underwriting technology and data raises the expense ratio in the year it lands and lowers the loss ratio for years after, which is why the two ratios must always be read as a pair.

## Formula

```
Underwriting Expenses / Earned Premiums
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 59 (batch 1)
