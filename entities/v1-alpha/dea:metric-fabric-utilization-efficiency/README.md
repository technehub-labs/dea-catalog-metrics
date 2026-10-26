# dea:metric-fabric-utilization-efficiency

Candidate Performance Metric record for **Fabric Utilization Efficiency** (FUE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fabric-utilization-efficiency`
- **Name:** Fabric Utilization Efficiency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FUE

## 2. Definition

Fabric Utilization Efficiency (FUE) captures how efficiently resources are converted into outputs for organizations tracking textile & apparel. It is computed as Fabric Used in Garments / Fabric Issued, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Textile & apparel.

## 3. Context

Measures effective capacity use of textile fabric against waste. It matters because fabric is the dominant material cost in apparel and marker efficiency decides it. Efficiency can be improved by cutting simpler patterns that waste less, shifting complexity cost elsewhere. Read with Marker Efficiency benchmarks and Fabric Waste Rate to confirm utilization gains are real.

## Formula

```
Fabric Used in Garments / Fabric Issued
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** textile_apparel
- **Sector:** textile_apparel

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 916 (batch 3)
