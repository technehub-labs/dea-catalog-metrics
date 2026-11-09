# dea:metric-waste-intensity

Candidate Performance Metric record for **Waste Intensity** (WI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-waste-intensity`
- **Name:** Waste Intensity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WI

## 2. Definition

Waste Intensity (WI) addresses environmental and social sustainability performance and is a fixture of manufacturing reporting. Its calculation is Waste Mass / Unit Produced, measured in ratio (x:1 or x). Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. It originates from and is most used in Manufacturing practice.

## 3. Context

Measures waste generated per unit of output or revenue. It matters because waste is paid-for input that leaves as disposal cost instead of product. It can be gamed by reclassifying waste streams or counting recycled disposal as eliminated waste. Read with Waste Diversion Rate and Scrap Cost Percentage to confirm intensity drops reflect process change, not relabeling.

## Formula

```
WI = Waste Mass / Unit Produced
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 263 (batch 1)
