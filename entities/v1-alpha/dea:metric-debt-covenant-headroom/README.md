# dea:metric-debt-covenant-headroom

Candidate Performance Metric record for **Debt Covenant Headroom** (DCH-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-debt-covenant-headroom`
- **Name:** Debt Covenant Headroom
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DCH-T

## 2. Definition

Debt Covenant Headroom (DCH-T) captures exposure to adverse outcomes for organizations tracking corporate treasury (deep dive). It is computed as Distance to Tightest Covenant / Covenant Level, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures distance between actual covenant metrics (leverage, interest cover, DSCR) and contractual thresholds. Headroom is the strategic-space metric: thin headroom converts business volatility into lender control, forcing equity raises or asset sales at the worst moments, and covenant amendment costs are real. Model headroom against downside scenarios, not just current run-rate. Read with liquidity buffer compliance and forecast credibility under stress.

## Formula

```
Distance to Tightest Covenant / Covenant Level
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_treasury_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2189 (batch 6)
