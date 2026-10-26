# dea:metric-runway-utilization

Candidate Performance Metric record for **Runway Utilization** (RWU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-runway-utilization`
- **Name:** Runway Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RWU

## 2. Definition

Runway Utilization (RWU) captures the utilization or availability of capacity for organizations tracking airport operations. It is computed as Aircraft Movements / Available Runway Hours, expressed in ratio (x:1 or x). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Airports.

## 3. Context

Measures the share of runway capacity used for movements. It matters because runway capacity is the binding airport constraint, and utilization determines delay economics. Scheduling off-peak runway usage can look efficient but shift costs to airlines and passengers. Read with Average Taxi Time and On-Time Departure Rate to confirm utilization converts into punctuality.

## Formula

```
Aircraft Movements / Available Runway Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations
- **Sector:** airports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1182 (batch 4)
