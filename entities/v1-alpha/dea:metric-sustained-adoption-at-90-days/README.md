# dea:metric-sustained-adoption-at-90-days

Candidate Performance Metric record for **Sustained Adoption at 90 Days** (SA90) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sustained-adoption-at-90-days`
- **Name:** Sustained Adoption at 90 Days
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SA90

## 2. Definition

Sustained Adoption at 90 Days (SA90) captures the retention of customers, users, or assets over time for organizations tracking change management. Its calculation is Users Still Adopting at 90 Days / Initial Adopters, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether new behaviors and tool usage persist ninety days after launch, beyond the novelty and enforcement phase. It matters because early adoption often decays once attention moves on, and ninety-day persistence is the best cheap predictor of permanent change. Watch for definition drift - active use thresholds lowered to preserve the number. Read with adoption rate of change for trajectory and benefit confirmation for payoff.

## Formula

```
Users Still Adopting at 90 Days / Initial Adopters
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** change_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1385 (batch 5)
