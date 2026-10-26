# dea:metric-program-expense-ratio

Candidate Performance Metric record for **Program Expense Ratio** (PER-N) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-program-expense-ratio`
- **Name:** Program Expense Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PER-N

## 2. Definition

A Nonprofit & NGO indicator, Program Expense Ratio (PER-N) quantifies conformance to standards, plans, or obligations. The formula is Program Service Expenses / Total Expenses - reported in percent (%). It is a standard measure in the Nonprofit & NGO sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Program expense ratio measures the share of total spending that goes to program delivery versus overhead, and it is the efficiency-respectability metric of the nonprofit sector - charity raters publish it, donors cite it, and institutional funders sometimes set thresholds, despite years of evidence that overhead-based judgment is a poor proxy for actual impact. The metric's pathology is well documented: ratio pressure starves infrastructure (the nonprofit starvation cycle), pushing organizations to disguise overhead as program cost - so the reported ratio reflects accounting choices as much as real efficiency. The honest read is functional: what is being delivered per program dollar, not what share sits in overhead. Read with cost per outcome (the impact-adjusted view), sustainability of deferred-infrastructure investment, and funder-specific overhead-recovery policies.

## Formula

```
Program Service Expenses / Total Expenses
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** nonprofit_ngo
- **Sector:** nonprofit_ngo

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1164 (batch 4)
