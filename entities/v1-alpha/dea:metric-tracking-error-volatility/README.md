# dea:metric-tracking-error-volatility

Candidate Performance Metric record for **Tracking Error Volatility** (TEV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tracking-error-volatility`
- **Name:** Tracking Error Volatility
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TEV

## 2. Definition

Tracking Error Volatility (TEV) addresses exposure to adverse outcomes and is a fixture of investment performance measurement reporting. It is computed as Standard Deviation of Portfolio vs Benchmark Returns, expressed in percent (%). Its use is concentrated in Investment management. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the variability of the portfolio's tracking error itself. Volatile TE means the active risk taken is uncontrolled. Steady TE is a precondition for attributing excess return to deliberate choices. Read with tracking error (Deep Dive) and excess return consistency rate.

## Formula

```
Standard Deviation of Portfolio vs Benchmark Returns
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3438 (batch 7)
