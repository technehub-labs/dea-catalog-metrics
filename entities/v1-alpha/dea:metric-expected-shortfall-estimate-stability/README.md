# dea:metric-expected-shortfall-estimate-stability

Candidate Performance Metric record for **Expected Shortfall Estimate Stability** (ESES) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-expected-shortfall-estimate-stability`
- **Name:** Expected Shortfall Estimate Stability
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ESES

## 2. Definition

Expected Shortfall Estimate Stability (ESES) measures exposure to adverse outcomes in the Investment Risk & Middle Office Operations domain. It is computed as Period Change in ES Estimate at 97.5% / Prior ES, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Investment management.

## 3. Context

Measures how stable the expected-shortfall (tail loss) estimates are across estimation windows. Stability determines whether tail metrics can guide position limits at all. Instability under stress is normal; instability in calm markets signals model fragility. Read with value at risk backtesting exception rate and stress test scenario coverage.

## Formula

```
Period Change in ES Estimate at 97.5% / Prior ES
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3458 (batch 7)
