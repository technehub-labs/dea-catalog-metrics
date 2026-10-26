# dea:metric-labor-cost-percentage

Candidate Performance Metric record for **Labor Cost Percentage** (LCP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-labor-cost-percentage`
- **Name:** Labor Cost Percentage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LCP

## 2. Definition

Labor Cost Percentage (LCP) addresses how efficiently resources are converted into outputs and is a fixture of standard workforce & pay metrics reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Total Labor Cost / Revenue, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures labor cost as a share of revenue or total cost. It frames workforce economics at the margin-management level. Percentage improved by understaffing converts into quality and attrition costs. Read with labor cost productivity ratio and benefit cost per employee.

## Formula

```
Total Labor Cost / Revenue
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** standard_workforce_pay_metrics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4118 (batch 9)
