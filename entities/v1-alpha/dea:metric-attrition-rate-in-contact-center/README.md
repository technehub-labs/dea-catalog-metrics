# dea:metric-attrition-rate-in-contact-center

Candidate Performance Metric record for **Attrition Rate in Contact Center** (CTR-AR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attrition-rate-in-contact-center`
- **Name:** Attrition Rate in Contact Center
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CTR-AR

## 2. Definition

Attrition Rate in Contact Center (CTR-AR) captures exposure to adverse outcomes for organizations tracking contact center. It is defined as Agent Departures / Average Agent Headcount; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures agent turnover in contact center roles. It matters because attrition destroys institutional knowledge and service quality while driving constant training cost. Teams can lower it by retaining disengaged agents who then damage satisfaction, trading attrition for quality. Read with Agent Engagement and Customer Satisfaction Score to confirm retention is healthy rather than stuck.

## Formula

```
Agent Departures / Average Agent Headcount
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 573 (batch 2)
