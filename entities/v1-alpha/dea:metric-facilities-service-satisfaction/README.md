# dea:metric-facilities-service-satisfaction

Candidate Performance Metric record for **Facilities Service Satisfaction** (FSS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-facilities-service-satisfaction`
- **Name:** Facilities Service Satisfaction
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FSS

## 2. Definition

Facilities Service Satisfaction (FSS) measures the engagement or satisfaction of the people involved in the Facilities & Real Estate domain. It is computed as Satisfied Facilities Survey Responses / Responses, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures occupant satisfaction with facilities services such as maintenance, cleanliness, and space. It matters because workspace quality drives productivity and retention even though facilities is a cost center. Scores can be gamed by surveying right after service visits while chronic issues go unmeasured. Read with Work Order Resolution Time and Space Utilization to link satisfaction to operational performance.

## Formula

```
Satisfied Facilities Survey Responses / Responses
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 453 (batch 1)
