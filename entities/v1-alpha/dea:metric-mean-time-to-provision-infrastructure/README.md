# dea:metric-mean-time-to-provision-infrastructure

Candidate Performance Metric record for **Mean Time to Provision (Infrastructure)** (MTTP-I) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-provision-infrastructure`
- **Name:** Mean Time to Provision (Infrastructure)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTTP-I

## 2. Definition

Mean Time to Provision (Infrastructure) (MTTP-I) measures how efficiently resources are converted into outputs in the Data Centers & Cloud Infrastructure domain. It is computed as Days from Request to Provisioned Resource, expressed in days. Its use is concentrated in Technology. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
MTTP-I = Days from Request to Provisioned Resource
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2153 (batch 6)
