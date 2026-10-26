# dea:metric-firmware-currency-rate

Candidate Performance Metric record for **Firmware Currency Rate** (FCR-NW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-firmware-currency-rate`
- **Name:** Firmware Currency Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FCR-NW

## 2. Definition

Firmware Currency Rate (FCR-NW) captures exposure to adverse outcomes for organizations tracking network change & configuration management. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Devices within Supported Firmware Baseline / Devices, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Devices within Supported Firmware Baseline / Devices
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_change_configuration_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3373 (batch 7)
