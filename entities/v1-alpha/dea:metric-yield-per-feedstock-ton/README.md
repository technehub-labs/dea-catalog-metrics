# dea:metric-yield-per-feedstock-ton

Candidate Performance Metric record for **Yield per Feedstock Ton** (YPFT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-yield-per-feedstock-ton`
- **Name:** Yield per Feedstock Ton
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** YPFT

## 2. Definition

Yield per Feedstock Ton (YPFT) captures how efficiently resources are converted into outputs for organizations tracking chemicals. Its calculation is Product Output Tonnes / Feedstock Tonnes, measured in ratio (x:1 or x). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Chemicals practice.

## 3. Context

Measures product output per ton of feedstock input. It matters because yield is the core conversion efficiency ratio in chemicals production. Yield can improve by shifting to premium feedstock, which costs more than the gain. Read with Feedstock Cost per Ton and Margin per Ton to confirm yield gains are economic.

## Formula

```
Product Output Tonnes / Feedstock Tonnes
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 901 (batch 3)
