# dea:metric-hedge-effectiveness-ratio

Candidate Performance Metric record for **Hedge Effectiveness Ratio** (HER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hedge-effectiveness-ratio`
- **Name:** Hedge Effectiveness Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HER

## 2. Definition

Hedge Effectiveness Ratio (HER) captures exposure to adverse outcomes for organizations tracking treasury & cash management. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Change in Hedge Fair Value / Change in Hedged Exposure Value, expressed in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how much of an exposure's value change is offset by the hedge. It matters because it validates whether hedging reduces risk or just adds cost. Retroactive hedge designation can make ratios look effective after the fact. Read with FX Exposure Coverage and realized hedge P&L to confirm effectiveness holds prospectively.

## Formula

```
HER = Change in Hedge Fair Value / Change in Hedged Exposure Value
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 596 (batch 2)
