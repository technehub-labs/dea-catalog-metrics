# dea:metric-perfect-order-rate-deep-dive

Candidate Performance Metric record for **Perfect Order Rate (Deep Dive)** (PORD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-perfect-order-rate-deep-dive`
- **Name:** Perfect Order Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PORD

## 2. Definition

Perfect Order Rate (Deep Dive) (PORD) measures the quality of outputs and outcomes in the Supply Chain Standard Measures (Deep Dive) domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Orders Perfect on Time, Quality, Quantity, Documentation / Orders, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures orders delivered on time, complete, damage-free, and with correct documentation. It is the all-dimensions delivery quality metric. Every component must hold simultaneously; averaging components overstates. Read with on-time in-full rate (Deep Dive) and order accuracy rate.

## Formula

```
PORD = Orders Perfect on Time, Quality, Quantity, Documentation / Orders
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4256 (batch 10)
