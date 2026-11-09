# dea:metric-selectivity

Candidate Performance Metric record for **Selectivity** (SEL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-selectivity`
- **Name:** Selectivity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SEL

## 2. Definition

Selectivity (SEL) captures the quality of outputs and outcomes for organizations tracking chemicals. Its calculation is Desired Product Formed / Reactant Converted, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Chemicals practice.

## Formula

```
SEL = Desired Product Formed / Reactant Converted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 895 (batch 3)
