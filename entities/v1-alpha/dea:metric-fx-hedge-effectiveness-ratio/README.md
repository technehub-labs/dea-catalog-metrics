# dea:metric-fx-hedge-effectiveness-ratio

Candidate Performance Metric record for **FX Hedge Effectiveness Ratio** (FXHER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fx-hedge-effectiveness-ratio`
- **Name:** FX Hedge Effectiveness Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FXHER

## 2. Definition

Within Corporate Treasury (Deep Dive), FX Hedge Effectiveness Ratio (FXHER) is used to gauge exposure to adverse outcomes. It is defined as Hedge Gains or Losses vs Exposure Movement; the result is stated in ratio (x:1 or x). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures how well hedges offset the exposures they cover, against effectiveness thresholds. Hedge effectiveness is simultaneously an accounting requirement (affecting P&L volatility treatment) and a real risk question, and ineffective hedges are cost without protection. Retrospective effectiveness measured only in benign currency environments overstates robustness. Read with hedge documentation compliance rate and stress-period performance.

## Formula

```
Hedge Gains or Losses vs Exposure Movement
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_treasury_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2183 (batch 6)
