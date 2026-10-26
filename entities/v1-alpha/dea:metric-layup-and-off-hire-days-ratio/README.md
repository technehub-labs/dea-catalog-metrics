# dea:metric-layup-and-off-hire-days-ratio

Candidate Performance Metric record for **Layup and Off-hire Days Ratio** (LODR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-layup-and-off-hire-days-ratio`
- **Name:** Layup and Off-hire Days Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LODR

## 2. Definition

A Maritime Shipping (Deep Dive) indicator, Layup and Off-hire Days Ratio (LODR) quantifies exposure to adverse outcomes. It is computed as Off-hire Days / Total Vessel Days, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Maritime.

## 3. Context

Measures the share of fleet capacity inactive - laid up, in drydock beyond plan, or off-hire. In cyclical shipping, active management of layup is the capacity lever that operators have, and the ratio signals how management is playing the cycle: capacity withdrawn early protects rates, withdrawn late is distress. Planned drydock belongs separately from distressed layup. Read with slot utilization - liner (Deep Dive) and charter-rate environment context.

## Formula

```
Off-hire Days / Total Vessel Days
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2436 (batch 6)
