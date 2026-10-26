# dea:metric-unplanned-outage-rate

Candidate Performance Metric record for **Unplanned Outage Rate** (UOR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unplanned-outage-rate`
- **Name:** Unplanned Outage Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** UOR

## 2. Definition

Unplanned Outage Rate (UOR) measures exposure to adverse outcomes in the Energy & Utilities domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Unplanned Outages / Total Operating Units per Period, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Energy & utilities.

## 3. Context

Measures the frequency of unplanned service interruptions per asset or period. It matters because unplanned outages drive regulatory penalties, safety risk, and customer churn in utility networks. Gaming risk includes reclassifying unplanned events as planned or force majeure. Read with Customer Average Interruption Duration Index and Preventive Maintenance Compliance to confirm outage reduction is structural.

## Formula

```
Unplanned Outages / Total Operating Units per Period
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 444 (batch 1)
