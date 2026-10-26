# dea:metric-log-source-coverage-rate

Candidate Performance Metric record for **Log Source Coverage Rate** (LSCR-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-log-source-coverage-rate`
- **Name:** Log Source Coverage Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LSCR-SOC

## 2. Definition

Log Source Coverage Rate (LSCR-SOC) captures capability maturity or development for organizations tracking secops & security operations center. The formula is Required Log Sources Onboarded / Required - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the proportion of critical assets and applications forwarding logs to the SIEM. Detections can only fire on data that arrives; blind spots are breach paths. Coverage that includes asset classes but not cloud control planes leaves the modern attack surface dark. Read with log retention compliance rate and detection rule coverage.

## Formula

```
Required Log Sources Onboarded / Required
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2787 (batch 7)
