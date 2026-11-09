# dea:metric-api-consumer-satisfaction-score

Candidate Performance Metric record for **API Consumer Satisfaction Score** (APICSAT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-consumer-satisfaction-score`
- **Name:** API Consumer Satisfaction Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** APICSAT

## 2. Definition

API Consumer Satisfaction Score (APICSAT) measures the economic value created or preserved in the API Lifecycle Management domain. It is computed as Consumer Survey Score for API Usability, expressed in score (points). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Software.

## Formula

```
APICSAT = Consumer Survey Score for API Usability
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3218 (batch 7)
