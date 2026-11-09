# dea:metric-scrap-rate

Candidate Performance Metric record for **Scrap Rate** (SR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scrap-rate`
- **Name:** Scrap Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SR

## 2. Definition

Scrap Rate (SR) addresses the quality of outputs and outcomes and is a fixture of operations reporting. The formula is Scrapped Units / Total Units Started - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
SR = Scrapped Units / Total Units Started
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 164 (batch 1)
