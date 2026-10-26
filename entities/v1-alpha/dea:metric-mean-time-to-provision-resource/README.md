# dea:metric-mean-time-to-provision-resource

Candidate Performance Metric record for **Mean Time to Provision Resource** (MTTP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-provision-resource`
- **Name:** Mean Time to Provision Resource
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTTP

## 2. Definition

A Data Center & Cloud Operations indicator, Mean Time to Provision Resource (MTTP) quantifies how efficiently resources are converted into outputs. It is computed as Hours from Request to Provisioned Resource, expressed in hours. Its use is concentrated in Technology & data centers. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Hours from Request to Provisioned Resource
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_center_cloud_operations
- **Sector:** technology_data_centers

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1094 (batch 4)
