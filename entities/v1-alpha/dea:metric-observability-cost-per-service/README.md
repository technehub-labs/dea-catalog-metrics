# dea:metric-observability-cost-per-service

Candidate Performance Metric record for **Observability Cost per Service** (OCS-SRE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-observability-cost-per-service`
- **Name:** Observability Cost per Service
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OCS-SRE

## 2. Definition

Observability Cost per Service (OCS-SRE) addresses how efficiently resources are converted into outputs and is a fixture of observability & site reliability engineering reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Telemetry Spend per Service per Month, expressed in currency value. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Telemetry Spend per Service per Month
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2880 (batch 7)
