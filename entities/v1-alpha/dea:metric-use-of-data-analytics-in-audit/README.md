# dea:metric-use-of-data-analytics-in-audit

Candidate Performance Metric record for **Use of Data Analytics in Audit** (UDAA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-use-of-data-analytics-in-audit`
- **Name:** Use of Data Analytics in Audit
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UDAA

## 2. Definition

Use of Data Analytics in Audit (UDAA) captures capability maturity or development for organizations tracking internal audit. It is defined as Audits Using Continuous Auditing or Analytics / Total Audits; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The share of audit work executed with data analytics - full-population testing, anomaly detection, continuous monitoring - rather than sampling, the maturity metric of the audit function that measures the transition from periodic assurance to continuous assurance. Its strategic significance is the coverage-scope change analytics enables: sampling inspects a fragment on a schedule, while full-population analysis inspects everything continuously, and that difference converts audit from finding last year's problems to flagging this quarter's - a phase change in the function's value, not an efficiency gain. The honest metric counts audit-hours or engagements materially using analytics, not tool purchases or dashboards built, since tool ownership without procedural integration is theater. Read with the finding-source trend: functions that genuinely shift to analytics report more findings from exception alerts and fewer from traditional walkthroughs - the signature of the transition actually happening.

## Formula

```
UDAA = Audits Using Continuous Auditing or Analytics / Total Audits
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_audit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 620 (batch 2)
