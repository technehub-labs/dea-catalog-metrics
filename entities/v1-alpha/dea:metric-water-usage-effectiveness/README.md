# dea:metric-water-usage-effectiveness

Candidate Performance Metric record for **Water Usage Effectiveness** (WUE-DC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-water-usage-effectiveness`
- **Name:** Water Usage Effectiveness
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WUE-DC

## 2. Definition

Water Usage Effectiveness (WUE-DC) addresses environmental and social sustainability performance and is a fixture of data centers & cloud infrastructure reporting. It is computed as Water Used / IT Energy, expressed in ratio (x:1 or x). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Technology.

## 3. Context

Measures water consumed per unit of IT equipment energy (WUE). As AI-scale densities make water the binding community constraint in many jurisdictions, WUE has moved from sustainability reporting to license-to-operate, with drought exposure concentrating risk in specific metros. Read alongside PUE, since dry cooling trades water for energy. Read with watershed stress assessments and community water commitments.

## Formula

```
Water Used / IT Energy
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2150 (batch 6)
