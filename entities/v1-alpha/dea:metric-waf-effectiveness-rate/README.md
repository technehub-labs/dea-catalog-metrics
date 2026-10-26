# dea:metric-waf-effectiveness-rate

Candidate Performance Metric record for **WAF Effectiveness Rate** (WAFER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-waf-effectiveness-rate`
- **Name:** WAF Effectiveness Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WAFER

## 2. Definition

WAF Effectiveness Rate (WAFER) addresses exposure to adverse outcomes and is a fixture of application security (appsec) reporting. It is computed as Attacks Blocked by WAF / Attack Attempts Detected, expressed in percent (%). Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Attacks Blocked by WAF / Attack Attempts Detected
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
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** application_security_appsec
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3336 (batch 7)
