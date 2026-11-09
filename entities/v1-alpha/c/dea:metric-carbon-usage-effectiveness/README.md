# dea:metric-carbon-usage-effectiveness

Candidate Performance Metric record for **Carbon Usage Effectiveness** (CUE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-carbon-usage-effectiveness`
- **Name:** Carbon Usage Effectiveness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CUE

## 2. Definition

Carbon Usage Effectiveness (CUE) captures environmental and social sustainability performance for organizations tracking data center & cloud operations. It is defined as CO2e from Facility Energy / IT Equipment Energy; the result is stated in ratio (x:1 or x). In Technology & data centers, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

CUE, The Green Grid's 2010 companion to PUE, divides total CO2 emissions from facility energy by IT equipment energy. It shifts the data-center conversation from energy efficiency to carbon intensity, so a diesel-heavy grid yields a far worse CUE than a hydro-rich one at identical PUE. Track it alongside PUE and renewable coverage: the practical levers are grid mix, power purchase agreements, and load shifting rather than cooling tuning alone.

## Formula

```
CUE = CO2e from Facility Energy / IT Equipment Energy
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_center_cloud_operations
- **Sector:** technology_data_centers

## Attribution

- **Source credit:** The Green Grid, 2010

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1096 (batch 4)
