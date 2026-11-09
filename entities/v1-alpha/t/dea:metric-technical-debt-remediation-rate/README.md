# dea:metric-technical-debt-remediation-rate

Candidate Performance Metric record for **Technical Debt Remediation Rate** (TDR-EA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-technical-debt-remediation-rate`
- **Name:** Technical Debt Remediation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TDR-EA

## 2. Definition

Technical Debt Remediation Rate (TDR-EA) captures exposure to adverse outcomes for organizations tracking enterprise architecture. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Debt Items Remediated / Debt Items Identified per Period, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of identified technical debt retired per period, or remediation velocity against accruing debt. It matters because unremediated debt compounds into change failures, security exposure, and eventually forced rewrites. The measurement honesty question is the denominator - debt identified by scanners underestimates architectural debt, while self-assessed debt is elastic. Read with change failure rate and unplanned outage trends for the felt consequence.

## Formula

```
TDR-EA = Debt Items Remediated / Debt Items Identified per Period
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** enterprise_architecture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1346 (batch 5)
