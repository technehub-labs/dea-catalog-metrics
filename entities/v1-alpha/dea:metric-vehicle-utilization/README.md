# dea:metric-vehicle-utilization

Candidate Performance Metric record for **Vehicle Utilization** (VUT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vehicle-utilization`
- **Name:** Vehicle Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** VUT

## 2. Definition

Vehicle Utilization (VUT) measures the utilization or availability of capacity in the Logistics & Transportation domain. It is computed as Vehicle Hours in Use / Vehicle Hours Available, expressed in percent (%). Its use is concentrated in Logistics. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of available vehicle capacity or time actually used for revenue work. It matters because fleets are fixed-cost assets whose economics live or die on utilization. Teams can inflate it by counting deadhead repositioning as productive or extending shifts beyond safe limits. Read with Empty Miles Rate and Fleet Downtime Percentage to ensure utilization is profitable and sustainable.

## Formula

```
Vehicle Hours in Use / Vehicle Hours Available
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 195 (batch 1)
