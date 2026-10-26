# dea:metric-picks-per-labor-hour

Candidate Performance Metric record for **Picks per Labor Hour** (PPH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-picks-per-labor-hour`
- **Name:** Picks per Labor Hour
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PPH

## 2. Definition

Picks per Labor Hour (PPH) captures how efficiently resources are converted into outputs for organizations tracking warehousing. Its calculation is Total Picks / Total Labor Hours, measured in ratio (x:1 or x). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Total Picks / Total Labor Hours
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** warehousing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 210 (batch 1)
