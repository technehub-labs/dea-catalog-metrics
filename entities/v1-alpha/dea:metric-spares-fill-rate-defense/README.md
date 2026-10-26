# dea:metric-spares-fill-rate-defense

Candidate Performance Metric record for **Spares Fill Rate (Defense)** (SFR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-spares-fill-rate-defense`
- **Name:** Spares Fill Rate (Defense)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SFR-D

## 2. Definition

Spares Fill Rate (Defense) (SFR-D) captures the utilization or availability of capacity for organizations tracking defense & aerospace. It is computed as Spares Demands Filled from Stock / Spares Demands, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Defense & aerospace.

## 3. Context

Measures the share of spares demand filled from stock at weapon-system or platform level. It matters because spares availability drives mission-capable rates for defense fleets. Fill can be raised by overstocking cheap items while long-lead critical parts run short. Read with Mission Capability Rate and Backorder Age for critical spares to confirm fill reflects mission readiness, not inventory gaming.

## Formula

```
Spares Demands Filled from Stock / Spares Demands
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 976 (batch 3)
