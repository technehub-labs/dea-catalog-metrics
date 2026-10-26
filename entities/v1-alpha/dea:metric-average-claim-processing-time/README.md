# dea:metric-average-claim-processing-time

Candidate Performance Metric record for **Average Claim Processing Time** (ACPT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-claim-processing-time`
- **Name:** Average Claim Processing Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ACPT

## 2. Definition

A Insurance indicator, Average Claim Processing Time (ACPT) quantifies how efficiently resources are converted into outputs. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Total Claims Processing Days / Claims Settled - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Insurance sector.

## Formula

```
Total Claims Processing Days / Claims Settled
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 62 (batch 1)
