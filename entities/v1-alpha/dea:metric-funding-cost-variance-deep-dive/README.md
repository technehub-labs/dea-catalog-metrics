# dea:metric-funding-cost-variance-deep-dive

Candidate Performance Metric record for **Funding Cost Variance (Deep Dive)** (FCV-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-funding-cost-variance-deep-dive`
- **Name:** Funding Cost Variance (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FCV-D

## 2. Definition

Funding Cost Variance (Deep Dive) (FCV-D) addresses the economic value created or preserved and is a fixture of corporate treasury (deep dive) reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Actual Funding Cost - Plan / Plan, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures realized funding cost against benchmark or plan (for corporates) or against peer spreads (for banks). Funding cost is the margin line most exposed to market and credit sentiment, and variance decomposition - rate environment, tenor mix, spread, instrument choice - identifies controllable drivers from market noise. Read with debt maturity walls, since refinancing timing interacts with spread environment. Read with hedge effectiveness on rate exposure and rating trajectory.

## Formula

```
FCV-D = Actual Funding Cost - Plan / Plan
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2190 (batch 6)
