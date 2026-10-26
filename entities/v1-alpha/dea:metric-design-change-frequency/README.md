# dea:metric-design-change-frequency

Candidate Performance Metric record for **Design Change Frequency** (DCF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-design-change-frequency`
- **Name:** Design Change Frequency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCF

## 2. Definition

A Construction & Engineering indicator, Design Change Frequency (DCF) quantifies exposure to adverse outcomes. It is computed as Design Changes Issued / Drawing Packages Released, expressed in ratio (x:1 or x). Its use is concentrated in Construction & engineering. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how often designs change after approval. It matters because late design churn is a leading driver of construction rework and claims. Frequency can be understated by bundling many changes into single formal revisions. Read with Change Order Rate and Rework Rate (Construction) to see whether design churn is truly falling or being repackaged.

## Formula

```
DCF = Design Changes Issued / Drawing Packages Released
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_engineering
- **Sector:** construction_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 677 (batch 2)
