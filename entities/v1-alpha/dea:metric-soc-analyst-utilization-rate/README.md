# dea:metric-soc-analyst-utilization-rate

Candidate Performance Metric record for **SOC Analyst Utilization Rate** (SAUR-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-soc-analyst-utilization-rate`
- **Name:** SOC Analyst Utilization Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SAUR-SOC

## 2. Definition

SOC Analyst Utilization Rate (SAUR-SOC) captures the utilization or availability of capacity for organizations tracking secops & security operations center. Its calculation is Triage Hours / Shift Hours, measured in percent (%). It provides the day-to-day signal that a process is running as designed. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
SAUR-SOC = Triage Hours / Shift Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2778 (batch 7)
