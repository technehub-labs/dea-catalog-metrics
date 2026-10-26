# dea:metric-infrastructure-unit-cost-trend

Candidate Performance Metric record for **Infrastructure Unit Cost Trend** (IUCT-ITFM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-infrastructure-unit-cost-trend`
- **Name:** Infrastructure Unit Cost Trend
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IUCT-ITFM

## 2. Definition

Within IT Financial Management & Technology Budgeting, Infrastructure Unit Cost Trend (IUCT-ITFM) is used to gauge how efficiently resources are converted into outputs. Its calculation is Change in per-Unit Infrastructure Cost, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the direction of unit infrastructure costs (per VM, per GB, per transaction). Falling unit costs mean cloud rightsizing and FinOps discipline are working. Falling prices industry-wide make internal trends look better than effort justifies. Read with cloud cost allocation accuracy and technology unit cost per user.

## Formula

```
Change in per-Unit Infrastructure Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_financial_management_technology_budgeting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3181 (batch 7)
