# dea:metric-golden-config-compliance

Candidate Performance Metric record for **Golden Config Compliance** (GCC-NW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-golden-config-compliance`
- **Name:** Golden Config Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** GCC-NW

## 2. Definition

Golden Config Compliance (GCC-NW) addresses conformance to standards, plans, or obligations and is a fixture of network change & configuration management reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Devices Matching Golden Configuration / Devices in Scope, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Devices Matching Golden Configuration / Devices in Scope
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3365 (batch 7)
