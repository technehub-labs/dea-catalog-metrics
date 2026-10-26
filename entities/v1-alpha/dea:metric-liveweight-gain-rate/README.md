# dea:metric-liveweight-gain-rate

Candidate Performance Metric record for **Liveweight Gain Rate** (LWG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-liveweight-gain-rate`
- **Name:** Liveweight Gain Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LWG

## 2. Definition

Liveweight Gain Rate (LWG) captures how efficiently resources are converted into outputs for organizations tracking agriculture & food processing. Its calculation is Animal Weight Gain / Days on Feed, measured in ratio (x:1 or x). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Agriculture & food practice.

## Formula

```
Animal Weight Gain / Days on Feed
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_food_processing
- **Sector:** agriculture_food

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 727 (batch 2)
