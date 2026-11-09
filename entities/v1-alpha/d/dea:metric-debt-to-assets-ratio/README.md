# dea:metric-debt-to-assets-ratio

Candidate Performance Metric record for **Debt-to-Assets Ratio** (D/A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-debt-to-assets-ratio`
- **Name:** Debt-to-Assets Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** D/A

## 2. Definition

A Finance & Accounting indicator, Debt-to-Assets Ratio (D/A) quantifies exposure to adverse outcomes. It is computed as Total Debt / Total Assets, expressed in ratio (x:1 or x). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Total debt as a proportion of total assets - a solvency gauge that answers a blunt question: how much of the balance sheet is claimed by creditors. Where debt-to-equity frames leverage against the residual owners' stake, this ratio uses the whole asset base as the denominator, which makes it less explosive when equity is small or negative and easier to compare across firms. Values approaching 0.6 put creditors in the majority, and above that the equity cushion is thin enough that a modest asset writedown can wipe it out. Because it uses book values, it understates leverage for firms whose real assets (brands, software) sit off the balance sheet, and it says nothing about debt maturity - a ratio can be fine while a refinancing wall approaches.

## Formula

```
D/A = Total Debt / Total Assets
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 19 (batch 1)
