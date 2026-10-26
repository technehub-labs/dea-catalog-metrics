# dea:metric-equipment-idle-time

Candidate Performance Metric record for **Equipment Idle Time** (EIT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-equipment-idle-time`
- **Name:** Equipment Idle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EIT

## 2. Definition

Equipment Idle Time (EIT) addresses the utilization or availability of capacity and is a fixture of construction & engineering reporting. The formula is Idle Equipment Hours / Available Equipment Hours - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Construction & engineering sector.

## Formula

```
EIT = Idle Equipment Hours / Available Equipment Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_engineering
- **Sector:** construction_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 674 (batch 2)
