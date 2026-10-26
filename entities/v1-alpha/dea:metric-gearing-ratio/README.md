# dea:metric-gearing-ratio

Candidate Performance Metric record for **Gearing Ratio** (GR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gearing-ratio`
- **Name:** Gearing Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GR

## 2. Definition

Within Finance & Accounting, Gearing Ratio (GR) is used to gauge exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Net Debt / (Net Debt + Shareholders' Equity), expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The British-Convention cousin of debt-to-equity, expressing debt relative to equity - sometimes net of cash, sometimes gross, depending on the house style that defines it. Because the term is used loosely, the definition matters more than the number: bank-style net gearing can read very differently from the gross figure after a large cash raise. It functions as a risk dial in credit analysis, covenant design, and takeover defence - high gearing amplifies equity returns in good times and covenants breach in bad ones, which is precisely the point. The strategic use is capacity: gearing tells you how much of the debt headroom is already spent before the next acquisition or downturn arrives.

## Formula

```
Net Debt / (Net Debt + Shareholders' Equity)
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
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 34 (batch 1)
