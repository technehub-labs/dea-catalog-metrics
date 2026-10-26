# dea:metric-grid-losses-ratio-technical-plus-non-technical

Candidate Performance Metric record for **Grid Losses Ratio (Technical plus Non-Technical)** (GLR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-grid-losses-ratio-technical-plus-non-technical`
- **Name:** Grid Losses Ratio (Technical plus Non-Technical)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GLR

## 2. Definition

Grid Losses Ratio (Technical plus Non-Technical) (GLR) addresses how efficiently resources are converted into outputs and is a fixture of utilities field operations & grid reporting. Its calculation is (Generation - Billed Energy) / Generation, measured in percent (%). It originates from and is most used in Utilities practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures energy lost between generation and billing - technical losses in conductors and transformers plus non-technical losses from theft and metering failure. Losses are pure margin erosion, and the non-technical share is where investment (smart metering, analytics) pays fastest. Loss allocation between technical and non-technical is estimation-heavy, so require methodology stability across periods. Read with smart meter deployment penetration and theft-recovery program yields.

## Formula

```
(Generation - Billed Energy) / Generation
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1889 (batch 6)
