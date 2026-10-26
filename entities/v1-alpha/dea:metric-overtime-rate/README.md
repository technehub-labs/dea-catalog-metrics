# dea:metric-overtime-rate

Candidate Performance Metric record for **Overtime Rate** (OTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-overtime-rate`
- **Name:** Overtime Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OTR

## 2. Definition

A Human Resources indicator, Overtime Rate (OTR) quantifies the utilization or availability of capacity. The formula is Overtime Hours / Total Paid Hours - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Overtime Hours / Total Paid Hours
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 147 (batch 1)
