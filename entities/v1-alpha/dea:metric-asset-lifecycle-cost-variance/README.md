# dea:metric-asset-lifecycle-cost-variance

Candidate Performance Metric record for **Asset Lifecycle Cost Variance** (ALCV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-lifecycle-cost-variance`
- **Name:** Asset Lifecycle Cost Variance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ALCV

## 2. Definition

Asset Lifecycle Cost Variance (ALCV) measures the economic value created or preserved in the Field Service & Asset Performance domain. It is computed as Actual Lifecycle Cost vs Plan / Plan, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures deviation of actual total cost of ownership from the planned lifecycle cost per asset. Variance reveals whether procurement assumptions were fantasy. Early-life variance is dominated by procurement decisions; late-life by maintenance. Read with asset downtime cost per incident and total cost of ownership per application.

## Formula

```
ALCV = Actual Lifecycle Cost vs Plan / Plan
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** operations
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3397 (batch 7)
