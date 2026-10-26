# dea:metric-underwriting-loss-ratio

Candidate Performance Metric record for **Underwriting Loss Ratio** (UWLR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-underwriting-loss-ratio`
- **Name:** Underwriting Loss Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** UWLR

## 2. Definition

A Insurance Underwriting indicator, Underwriting Loss Ratio (UWLR) quantifies exposure to adverse outcomes. It is computed as Incurred Claims / Earned Premium, expressed in percent (%). Its use is concentrated in Insurance. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures incurred claims against earned premium, the core profitability gauge of an underwriting portfolio. It anchors pricing adequacy, reinsurance strategy, and capital consumption. Read the trend by segment and vintage, since blended ratios hide deteriorating pockets, and watch for loss ratios flattered by premium growth outpacing loss emergence. Read with rate adequacy index (Underwriting) and reserve development patterns.

## Formula

```
Incurred Claims / Earned Premium
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1500 (batch 6)
