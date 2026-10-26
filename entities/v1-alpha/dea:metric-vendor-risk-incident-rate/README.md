# dea:metric-vendor-risk-incident-rate

Candidate Performance Metric record for **Vendor Risk Incident Rate** (VRIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vendor-risk-incident-rate`
- **Name:** Vendor Risk Incident Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** VRIR

## 2. Definition

Within Third-Party Risk Management, Vendor Risk Incident Rate (VRIR) is used to gauge exposure to adverse outcomes. Its calculation is Material Vendor-Caused Incidents / Vendor Engagements, measured in events per thousand or million (scaled). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the frequency of incidents attributable to third parties. It is the outcome scoreboard for the entire TPRM program. Incident definitions that exclude near-misses understate the risk picture. Read with vendor incident notification compliance and third-party risk trend.

## Formula

```
Material Vendor-Caused Incidents / Vendor Engagements
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** third_party_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3734 (batch 8)
