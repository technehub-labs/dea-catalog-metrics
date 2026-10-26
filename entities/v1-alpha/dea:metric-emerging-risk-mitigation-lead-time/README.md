# dea:metric-emerging-risk-mitigation-lead-time

Candidate Performance Metric record for **Emerging Risk Mitigation Lead Time** (ERMLT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emerging-risk-mitigation-lead-time`
- **Name:** Emerging Risk Mitigation Lead Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ERMLT

## 2. Definition

Emerging Risk Mitigation Lead Time (ERMLT) captures how efficiently resources are converted into outputs for organizations tracking emerging risk & horizon scanning. Its calculation is Days from Risk Accepted to First Mitigation in Place, measured in days. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how far in advance of impact mitigation actions can be completed. Lead time is what makes mitigation cheaper than response. Lead times assumed under best-case conditions collapse in reality. Read with mitigation optionality score and zero-day response time.

## Formula

```
Days from Risk Accepted to First Mitigation in Place
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** risk
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** emerging_risk_horizon_scanning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4012 (batch 8)
