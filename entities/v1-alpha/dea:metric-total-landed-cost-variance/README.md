# dea:metric-total-landed-cost-variance

Candidate Performance Metric record for **Total Landed Cost Variance** (TLCV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-total-landed-cost-variance`
- **Name:** Total Landed Cost Variance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TLCV

## 2. Definition

Within Supply Chain Standard Measures (Deep Dive), Total Landed Cost Variance (TLCV) is used to gauge the economic value created or preserved. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Actual vs Planned Landed Cost / Planned, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures deviation of actual landed cost (product, freight, duty, handling) from planned. Landed cost variance exposes the hidden economics of sourcing decisions. Variance baselines set on favorable freight rates decay silently. Read with freight cost per unit landed and total cost of ownership optimization rate.

## Formula

```
Actual vs Planned Landed Cost / Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4269 (batch 10)
