# dea:metric-yield-on-cost-development

Candidate Performance Metric record for **Yield on Cost (Development)** (YOC-RE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-yield-on-cost-development`
- **Name:** Yield on Cost (Development)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** YOC-RE

## 2. Definition

Yield on Cost (Development) (YOC-RE) captures the economic value created or preserved for organizations tracking real estate & mortgage standard measures. Its calculation is Stabilized NOI / Total Development Cost, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Real estate practice.

## 3. Context

Measures development's stabilized income relative to total project cost. Yield on cost is the developer's test of whether the build beats buying. Stabilized income assumed at pro-forma rather than achieved is hope. Read with project IRR realization (Development) and capitalization rate.

## Formula

```
YOC-RE = Stabilized NOI / Total Development Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** real_estate_mortgage_standard_measures
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4220 (batch 10)
