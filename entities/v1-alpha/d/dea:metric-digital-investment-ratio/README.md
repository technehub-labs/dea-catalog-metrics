# dea:metric-digital-investment-ratio

Candidate Performance Metric record for **Digital Investment Ratio** (DIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-digital-investment-ratio`
- **Name:** Digital Investment Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DIR

## 2. Definition

Within Digital Transformation, Digital Investment Ratio (DIR) is used to gauge the economic value created or preserved. It is computed as Digital Initiative Spend / Total Change Spend, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Compares digital investment as a share of total capital and opex, or of revenue, indicating the scale of transformation ambition relative to the base business. It is a context metric, not a virtue: high ratios with weak value realization signal an unproductive transformation, while low ratios in a digitizing sector signal strategic denial. Benchmarks vary widely by industry and by what is classified as digital. Read with digital initiative value realization and digital revenue share.

## Formula

```
DIR = Digital Initiative Spend / Total Change Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** digital_transformation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1317 (batch 5)
