# dea:metric-reinsurance-cost-of-cover

Candidate Performance Metric record for **Reinsurance Cost of Cover** (RCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reinsurance-cost-of-cover`
- **Name:** Reinsurance Cost of Cover
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCC

## 2. Definition

Reinsurance Cost of Cover (RCC) captures the economic value created or preserved for organizations tracking insurance underwriting. It is defined as Reinsurance Premium Ceded / Gross Written Premium; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. In Insurance, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the net cost of reinsurance - ceded premium less recoveries and profit commissions - as a measure of protection value. It anchors the buy-versus-retain capital decision, and it is easy to misread: cheap cover is often cheap because it is shallow or exclusion-riddled. Evaluate against capital relief and volatility reduction actually obtained, over full cycles rather than benign years. Read with recovery experience in large events and net retention levels.

## Formula

```
RCC = Reinsurance Premium Ceded / Gross Written Premium
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
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1512 (batch 6)
