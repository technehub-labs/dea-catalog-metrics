# dea:metric-stress-related-absence-rate

Candidate Performance Metric record for **Stress-Related Absence Rate** (SAR-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stress-related-absence-rate`
- **Name:** Stress-Related Absence Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SAR-E

## 2. Definition

Stress-Related Absence Rate (SAR-E) measures exposure to adverse outcomes in the Employee Wellbeing domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Stress-Related Absence Days / Total Absence Days, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Stress-related absence measures leave attributed to psychological strain, and in many workforces it is the fastest-growing absence category - and it is the cost-surfacing metric for workforce strain that culture and workload metrics measure as sentiment. Its measurement honesty depends on certification and recording practice: stress attribution is fuzzy (a back injury worsened by strain?), recording culture varies by manager and country, and cross-comparison needs care. The diagnostic value is in pattern: stress absence clustering by team, role type, or manager points at structural causes rather than individual fragility, and long-duration stress absences dominate the cost. Read with duration distribution (long cases are the cost), return-to-work and recurrence rates (failed returns signal unresolved causes), burnout and engagement scores as the leading indicators, and workload metrics in affected teams.

## Formula

```
Stress-Related Absence Days / Total Absence Days
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** employee_wellbeing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1231 (batch 4)
