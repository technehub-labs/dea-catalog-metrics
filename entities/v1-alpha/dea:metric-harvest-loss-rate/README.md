# dea:metric-harvest-loss-rate

Candidate Performance Metric record for **Harvest Loss Rate** (HLR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-harvest-loss-rate`
- **Name:** Harvest Loss Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HLR

## 2. Definition

Harvest Loss Rate (HLR) addresses the quality of outputs and outcomes and is a fixture of agriculture & food processing reporting. It is computed as Post-Harvest Losses / Total Harvest, expressed in percent (%). Its use is concentrated in Agriculture & food. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures crop or product lost between harvest and processing. It matters because post-harvest loss is grown-but-wasted value, and food security metrics depend on it. Loss estimation is often survey-based, so definitions can be quietly tightened to shrink the number. Read with Cold Chain Compliance and Yield per Hectare to locate where losses occur and whether interventions work.

## Formula

```
HLR = Post-Harvest Losses / Total Harvest
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_food_processing
- **Sector:** agriculture_food

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 729 (batch 2)
