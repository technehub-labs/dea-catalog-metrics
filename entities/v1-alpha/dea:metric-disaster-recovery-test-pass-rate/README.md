# dea:metric-disaster-recovery-test-pass-rate

Candidate Performance Metric record for **Disaster Recovery Test Pass Rate** (DRTPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-disaster-recovery-test-pass-rate`
- **Name:** Disaster Recovery Test Pass Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DRTPR

## 2. Definition

Disaster Recovery Test Pass Rate (DRTPR) captures exposure to adverse outcomes for organizations tracking business continuity & disaster recovery. Its calculation is Successful DR Tests / DR Tests Executed, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how completely DR tests meet their objectives without major gaps. Tests are the only evidence that recovery plans work. Tests declared passed with waived exceptions are failures with paperwork. Read with recovery time objective compliance rate and continuity plan activation success rate.

## Formula

```
Successful DR Tests / DR Tests Executed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** business_continuity_disaster_recovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3519 (batch 8)
