# dea:metric-contingency-drawdown-rate

Candidate Performance Metric record for **Contingency Drawdown Rate** (CDR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contingency-drawdown-rate`
- **Name:** Contingency Drawdown Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDR-P

## 2. Definition

Contingency Drawdown Rate (CDR-P) measures exposure to adverse outcomes in the Project Risk & Issue Management domain. Its calculation is Contingency Consumed / Contingency Budget, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how quickly project contingency reserves are consumed relative to progress. Fast early drawdown is the most reliable predictor of overrun. Contingency re-baselined away hides the signal. Read with cost variance percent and risk exposure trend index (Projects).

## Formula

```
CDR-P = Contingency Consumed / Contingency Budget
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** project_risk_issue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3424 (batch 7)
