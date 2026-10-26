# dea:metric-formaldehyde-emission-compliance

Candidate Performance Metric record for **Formaldehyde Emission Compliance** (FEC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-formaldehyde-emission-compliance`
- **Name:** Formaldehyde Emission Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FEC

## 2. Definition

Formaldehyde Emission Compliance (FEC) measures conformance to standards, plans, or obligations in the Furniture & Wood Products domain. It is computed as Batches Meeting E1 or Equivalent / Batches Tested, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Manufacturing.

## 3. Context

Measures product and workplace formaldehyde emissions against standards (CARB, E1, workplace limits). For wood furniture and panels, formaldehyde compliance is market access - noncompliant product is unsellable in regulated markets - and a chronic consumer-safety concern. Product certification must be backed by production lot testing, since supplier declarations drift from reality. Read with panel supplier certification audits and indoor-air testing results.

## Formula

```
FEC = Batches Meeting E1 or Equivalent / Batches Tested
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
- **Domain:** furniture_wood_products
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1878 (batch 6)
