# dea:metric-auto-remediation-execution-rate

Candidate Performance Metric record for **Auto-Remediation Execution Rate** (ARER-NOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-auto-remediation-execution-rate`
- **Name:** Auto-Remediation Execution Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ARER-NOC

## 2. Definition

Within Network Operations Center (Deep Dive), Auto-Remediation Execution Rate (ARER-NOC) is used to gauge how efficiently resources are converted into outputs. Its calculation is Alerts Auto-Remediated without Human Touch / Auto-Eligible Alerts, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of standard network faults resolved automatically without human touch. Automation absorbs low-value ticket work and cuts resolution times from hours to seconds. Auto-remediation without robust post-change verification can mask recurring underlying faults. Read with proactive versus reactive ticket ratio and NOC mean time to resolve.

## Formula

```
Alerts Auto-Remediated without Human Touch / Auto-Eligible Alerts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2852 (batch 7)
