# dea:metric-serviceable-spares-availability

Candidate Performance Metric record for **Serviceable Spares Availability** (SSPA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-serviceable-spares-availability`
- **Name:** Serviceable Spares Availability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SSPA

## 2. Definition

Serviceable Spares Availability (SSPA) measures the utilization or availability of capacity in the Aviation Maintenance Repair & Overhaul domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Serviceable Parts Available at Need / Parts Demands, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Airlines & aviation.

## 3. Context

Measures the share of demanded spare parts available serviceable at need. It matters because unserviceable spares ground aircraft and cascade into delays. Availability can be gamed by borrowing and pooling stock that flatters local metrics. Read with Component Repair Turnaround Time and Fill Rate for parts to confirm availability is sustainable.

## Formula

```
SSPA = Serviceable Parts Available at Need / Parts Demands
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** aviation_maintenance_repair_overhaul
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1188 (batch 4)
