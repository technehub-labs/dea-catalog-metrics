# dea:metric-configuration-drift-rate-network

Candidate Performance Metric record for **Configuration Drift Rate (Network)** (CDRN) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-configuration-drift-rate-network`
- **Name:** Configuration Drift Rate (Network)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CDRN

## 2. Definition

Within Network Change & Configuration Management, Configuration Drift Rate (Network) (CDRN) is used to gauge conformance to standards, plans, or obligations. It is a working-level control: thresholds trigger immediate operational response. It is defined as Devices with Unapproved Config Drift / Devices; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Devices with Unapproved Config Drift / Devices
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_change_configuration_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3364 (batch 7)
