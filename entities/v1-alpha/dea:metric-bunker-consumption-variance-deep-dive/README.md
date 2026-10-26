# dea:metric-bunker-consumption-variance-deep-dive

Candidate Performance Metric record for **Bunker Consumption Variance (Deep Dive)** (BCV-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bunker-consumption-variance-deep-dive`
- **Name:** Bunker Consumption Variance (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BCV-D

## 2. Definition

Bunker Consumption Variance (Deep Dive) (BCV-D) addresses how efficiently resources are converted into outputs and is a fixture of maritime shipping (deep dive) reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Actual - Planned Consumption / Plan, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Its use is concentrated in Maritime.

## Formula

```
Actual - Planned Consumption / Plan
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2438 (batch 6)
