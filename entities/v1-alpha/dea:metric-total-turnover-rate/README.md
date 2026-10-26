# dea:metric-total-turnover-rate

Candidate Performance Metric record for **Total Turnover Rate** (TTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-total-turnover-rate`
- **Name:** Total Turnover Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TTR

## 2. Definition

A Human Resources indicator, Total Turnover Rate (TTR) quantifies exposure to adverse outcomes. The formula is All Departures / Average Headcount - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

All separations - voluntary and involuntary - over headcount, the composite workforce-stability gauge that HR reports first because it captures the full outflow. Its strategic role is as an envelope: when total turnover splits into voluntary and involuntary, management can see whether churn is being driven by employees leaving (engagement and market forces) or by the company restructuring (strategy and performance management), which have opposite implications. Very low total turnover is not automatically good - a static workforce that never refreshes skills can be a bigger liability than a dynamic one, particularly in technology functions where skill half-life is short. The metric gains meaning through cohort and tenure cuts, where early-tenure spikes reveal onboarding failure.

## Formula

```
All Departures / Average Headcount
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 127 (batch 1)
