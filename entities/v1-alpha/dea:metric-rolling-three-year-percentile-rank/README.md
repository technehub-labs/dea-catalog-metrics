# dea:metric-rolling-three-year-percentile-rank

Candidate Performance Metric record for **Rolling Three-Year Percentile Rank** (RTYPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rolling-three-year-percentile-rank`
- **Name:** Rolling Three-Year Percentile Rank
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RTYPR

## 2. Definition

Rolling Three-Year Percentile Rank (RTYPR) measures the economic value created or preserved in the Investment Performance Measurement domain. It is computed as Peer Percentile of Rolling 3-Year Return, expressed in percent (%). Its use is concentrated in Investment management. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the portfolio's rank versus peers over rolling three-year windows. Peer-relative framing matches how clients select funds. Peer groups with style drift make ranks flattering. Read with excess return consistency rate and manager selection win rate.

## Formula

```
Peer Percentile of Rolling 3-Year Return
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3453 (batch 7)
