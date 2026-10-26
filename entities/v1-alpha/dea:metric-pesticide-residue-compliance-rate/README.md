# dea:metric-pesticide-residue-compliance-rate

Candidate Performance Metric record for **Pesticide Residue Compliance Rate** (PRCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pesticide-residue-compliance-rate`
- **Name:** Pesticide Residue Compliance Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PRCR

## 2. Definition

Pesticide Residue Compliance Rate (PRCR) addresses conformance to standards, plans, or obligations and is a fixture of agriculture & food processing reporting. It is computed as Batches within Residue Limits / Batches Tested, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Agriculture & food.

## 3. Context

Pesticide residue compliance rate is the share of tested lots meeting maximum residue limits for export markets, and it is the metric where a producer's field practices collide with destination-market regulation - the EU, Japan, and the US each maintain different MRLs, so a lot can be compliant domestically and rejected abroad. A single exceedance can blacklist an entire growing region for a season. Risk concentrates at the grower interface: aggregate grower statistics conceal a handful of non-compliant plots, so read with per-grower testing results, pre-harvest interval adherence, and supplier certification status rather than the aggregate rate.

## Formula

```
Batches within Residue Limits / Batches Tested
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_food_processing
- **Sector:** agriculture_food

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 736 (batch 2)
