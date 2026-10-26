# dea:metric-warranty-recovery-rate-mro

Candidate Performance Metric record for **Warranty Recovery Rate (MRO)** (WRR-MRO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-warranty-recovery-rate-mro`
- **Name:** Warranty Recovery Rate (MRO)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WRR-MRO

## 2. Definition

Within Aviation Maintenance Repair & Overhaul, Warranty Recovery Rate (MRO) (WRR-MRO) is used to gauge the economic value created or preserved. It is computed as Recovered Warranty Value / Eligible Warranty Value, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Airlines & aviation.

## 3. Context

Measures the share of eligible warranty costs recovered from OEMs. It matters because unrecovered warranty work is margin quietly lost on work already done. Claims can be abandoned when filing effort exceeds perceived value. Read with Claims Approval Rate and aging of unfiled claims to confirm recovery discipline is complete.

## Formula

```
WRR-MRO = Recovered Warranty Value / Eligible Warranty Value
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1192 (batch 4)
