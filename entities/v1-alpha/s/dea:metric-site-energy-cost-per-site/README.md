# dea:metric-site-energy-cost-per-site

Candidate Performance Metric record for **Site Energy Cost per Site** (SECS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-site-energy-cost-per-site`
- **Name:** Site Energy Cost per Site
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SECS

## 2. Definition

A Telecom Network Operations indicator, Site Energy Cost per Site (SECS) quantifies how efficiently resources are converted into outputs. It is computed as Total Network Site Energy Cost / Sites, expressed in currency per unit. Its use is concentrated in Telecommunications. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures average energy cost across telecom network sites. It matters because energy is among the largest operating costs in network infrastructure. Cost averaging can hide a few energy-inefficient sites driving the total. Read with Energy per Byte Carried and site-level outliers to confirm the average reflects real efficiency.

## Formula

```
SECS = Total Network Site Energy Cost / Sites
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 858 (batch 3)
