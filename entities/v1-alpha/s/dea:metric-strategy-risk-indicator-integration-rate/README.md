# dea:metric-strategy-risk-indicator-integration-rate

Candidate Performance Metric record for **Strategy Risk Indicator Integration Rate** (SRII) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-strategy-risk-indicator-integration-rate`
- **Name:** Strategy Risk Indicator Integration Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SRII

## 2. Definition

Strategy Risk Indicator Integration Rate (SRII) captures exposure to adverse outcomes for organizations tracking balanced scorecard implementation & review. Its calculation is Strategic Risks Reflected in Scorecard Measures / Strategic Risks, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how completely strategic risk indicators are embedded in the scorecard alongside performance measures. Performance without risk visibility invites optimization into fragility. Indicators added without thresholds and escalation owners are decorative. Read with risk appetite threshold utilization and leading indicator share.

## Formula

```
SRII = Strategic Risks Reflected in Scorecard Measures / Strategic Risks
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_implementation_review

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3489 (batch 7)
