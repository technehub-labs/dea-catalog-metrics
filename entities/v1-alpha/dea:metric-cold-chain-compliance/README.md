# dea:metric-cold-chain-compliance

Candidate Performance Metric record for **Cold Chain Compliance** (CCC-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cold-chain-compliance`
- **Name:** Cold Chain Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CCC-F

## 2. Definition

Cold Chain Compliance (CCC-F) addresses the quality of outputs and outcomes and is a fixture of agriculture & food processing reporting. It is computed as Shipments within Temperature Range / Shipments Monitored, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Agriculture & food.

## 3. Context

Measures the share of perishable products maintained within required temperature ranges through the chain. It matters because cold chain breaks cause invisible quality loss and food safety risk. Compliance can be overstated by relying on spot checks at endpoints instead of continuous logging. Read with Temperature Excursion Rate and Product Waste Rate to confirm compliance is continuous, not sampled.

## Formula

```
Shipments within Temperature Range / Shipments Monitored
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_food_processing
- **Sector:** agriculture_food

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 733 (batch 2)
