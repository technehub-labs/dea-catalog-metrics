# dea:metric-net-dollar-retention-deep-dive

Candidate Performance Metric record for **Net Dollar Retention (Deep Dive)** (NDRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-dollar-retention-deep-dive`
- **Name:** Net Dollar Retention (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NDRD

## 2. Definition

Net Dollar Retention (Deep Dive) (NDRD) measures the retention of customers, users, or assets over time in the Unit Economics & Growth (Deep Dive) domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Cohort Revenue Now / Same Cohort Prior Period, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Software.

## 3. Context

Measures recurring revenue from a customer cohort including expansion, net of churn. Above 100% is the compounding engine of modern software economics. NDR concentrated in a few big accounts is fragile expansion. Read with gross dollar retention (Deep Dive) and revenue churn with expansion offset.

## Formula

```
NDRD = Cohort Revenue Now / Same Cohort Prior Period
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4162 (batch 9)
