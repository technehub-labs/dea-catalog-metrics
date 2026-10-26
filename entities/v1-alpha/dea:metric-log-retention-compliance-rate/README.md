# dea:metric-log-retention-compliance-rate

Candidate Performance Metric record for **Log Retention Compliance Rate** (LRCR-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-log-retention-compliance-rate`
- **Name:** Log Retention Compliance Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LRCR-SOC

## 2. Definition

A SecOps & Security Operations Center indicator, Log Retention Compliance Rate (LRCR-SOC) quantifies conformance to standards, plans, or obligations. The formula is Sources Meeting Retention Policy / Sources - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures adherence to required log retention periods across systems. Retention determines whether investigations can reconstruct attacker activity or face evidentiary gaps. Hot-storage costs push teams to trim retention below requirements, silently. Read with log source coverage rate and audit finding recurrence.

## Formula

```
Sources Meeting Retention Policy / Sources
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2788 (batch 7)
