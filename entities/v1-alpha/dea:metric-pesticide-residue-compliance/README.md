# dea:metric-pesticide-residue-compliance

Candidate Performance Metric record for **Pesticide Residue Compliance** (PRC-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pesticide-residue-compliance`
- **Name:** Pesticide Residue Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRC-A

## 2. Definition

Pesticide Residue Compliance (PRC-A) measures conformance to standards, plans, or obligations in the Agriculture & Agronomy (Deep Dive) domain. It is computed as Samples within MRL / Samples Tested, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Agriculture.

## 3. Context

Measures harvested product against maximum residue limits for destination markets. Compliance is market access for growers - a single consignment failure can close an export season - and it tests the whole spray-diary-harvest-interval discipline chain. Sampling plans must reflect the market's own testing regimes, since MRLs differ by destination. Read with spray-record audit findings and rejection history by buyer market.

## Formula

```
PRC-A = Samples within MRL / Samples Tested
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_agronomy_deep_dive
- **Sector:** agriculture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2324 (batch 6)
