# dea:metric-customer-effort-score

Candidate Performance Metric record for **Customer Effort Score** (CES) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-effort-score`
- **Name:** Customer Effort Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CES

## 2. Definition

Within Customer, Customer Effort Score (CES) is used to gauge the engagement or satisfaction of the people involved. It is defined as Average Ease Rating on 7-Point Scale; the result is stated in score (points). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how hard customers had to work to resolve an issue or complete a task. It matters because high-effort experiences are the strongest predictor of disloyalty in service settings. Teams can lower it cosmetically by scripting the effort question or measuring only self-selected easy journeys. Read with First Contact Resolution and Customer Satisfaction Score to confirm low effort reflects genuinely smoother journeys.

## Formula

```
CES = Average Ease Rating on 7-Point Scale
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 68 (batch 1)
