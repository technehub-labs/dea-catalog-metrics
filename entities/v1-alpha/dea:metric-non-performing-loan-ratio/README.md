# dea:metric-non-performing-loan-ratio

Candidate Performance Metric record for **Non-Performing Loan Ratio** (NPL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-non-performing-loan-ratio`
- **Name:** Non-Performing Loan Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NPL

## 2. Definition

Non-Performing Loan Ratio (NPL) captures exposure to adverse outcomes for organizations tracking banking & financial services. It is computed as Non-Performing Loans / Gross Loans, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Financial services.

## 3. Context

Loans past due or otherwise impaired as a share of the gross loan book - the canonical asset-quality gauge in credit institutions. It is a lagging indicator by construction: a loan stops performing well after the credit decision that doomed it, so the NPL ratio describes yesterday's underwriting, not today's. Its strategic use is two-fold: the level signals balance-sheet risk and provisioning adequacy, and the direction - inflows versus outflows, sales to bad banks, write-offs - reveals whether the problem is being worked out or merely aged. Comparisons need care: 90-day versus 180-day classification conventions, forbearance policies, and IFRS 9 staging all move the number without changing the underlying credit.

## Formula

```
NPL = Non-Performing Loans / Gross Loans
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 37 (batch 1)
