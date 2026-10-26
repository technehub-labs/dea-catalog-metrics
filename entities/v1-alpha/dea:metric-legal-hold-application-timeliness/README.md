# dea:metric-legal-hold-application-timeliness

Candidate Performance Metric record for **Legal Hold Application Timeliness** (LHAT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-legal-hold-application-timeliness`
- **Name:** Legal Hold Application Timeliness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LHAT

## 2. Definition

Within Records & Information Management, Legal Hold Application Timeliness (LHAT) is used to gauge exposure to adverse outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Days from Hold Order to Preservation Confirmed - reported in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Days from Hold Order to Preservation Confirmed
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** records_information_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3677 (batch 8)
