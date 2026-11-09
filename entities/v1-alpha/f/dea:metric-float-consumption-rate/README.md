# dea:metric-float-consumption-rate

Candidate Performance Metric record for **Float Consumption Rate** (FCR-PM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-float-consumption-rate`
- **Name:** Float Consumption Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FCR-PM

## 2. Definition

Float Consumption Rate (FCR-PM) measures exposure to adverse outcomes in the Project Management (Deep Dive) domain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Float Consumed / Total Float, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
FCR-PM = Float Consumed / Total Float
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2935 (batch 7)
