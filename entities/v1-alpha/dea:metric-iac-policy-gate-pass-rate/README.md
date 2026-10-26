# dea:metric-iac-policy-gate-pass-rate

Candidate Performance Metric record for **IaC Policy Gate Pass Rate** (IACPG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-iac-policy-gate-pass-rate`
- **Name:** IaC Policy Gate Pass Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IACPG

## 2. Definition

Within Cloud Security Posture Management, IaC Policy Gate Pass Rate (IACPG) is used to gauge conformance to standards, plans, or obligations. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Pipeline Runs Passing Policy-as-Code / Runs - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Pipeline Runs Passing Policy-as-Code / Runs
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3319 (batch 7)
