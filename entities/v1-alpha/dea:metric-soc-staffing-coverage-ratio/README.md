# dea:metric-soc-staffing-coverage-ratio

Candidate Performance Metric record for **SOC Staffing Coverage Ratio** (SSCR-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-soc-staffing-coverage-ratio`
- **Name:** SOC Staffing Coverage Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSCR-SOC

## 2. Definition

SOC Staffing Coverage Ratio (SSCR-SOC) addresses the utilization or availability of capacity and is a fixture of secops & security operations center reporting. It is a working-level control: thresholds trigger immediate operational response. It is defined as 24x7 Shifts Fully Staffed / Shifts; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
24x7 Shifts Fully Staffed / Shifts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2789 (batch 7)
