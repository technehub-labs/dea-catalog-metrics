# dea:metric-employee-net-promoter-score

Candidate Performance Metric record for **Employee Net Promoter Score** (eNPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-employee-net-promoter-score`
- **Name:** Employee Net Promoter Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** eNPS

## 2. Definition

A Human Resources indicator, Employee Net Promoter Score (eNPS) quantifies the engagement or satisfaction of the people involved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is % Employee Promoters - % Employee Detractors, measured in score (points). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

eNPS applies the Reichheld NPS mechanism to employees: would you recommend this organization as a place to work? Scores below 0 are a retention warning; above +20 is generally healthy; tech leaders often exceed +30. It is a temperature check, not a diagnosis - treat sustained drops as a trigger for focus groups and stay interviews rather than an end in itself. Anonymity is essential: if staff doubt it, participation and honesty collapse together.

## Formula

```
% Employee Promoters - % Employee Detractors
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** organization
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Adapted from Fred Reichheld's NPS methodology

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 130 (batch 1)
