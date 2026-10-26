# dea:metric-automation-ratio

Candidate Performance Metric record for **Automation Ratio** (AUTO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automation-ratio`
- **Name:** Automation Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AUTO

## 2. Definition

Automation Ratio (AUTO) addresses capability maturity or development and is a fixture of manufacturing reporting. It is computed as Automated Process Steps / Total Process Steps, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Manufacturing.

## 3. Context

The share of production steps, capacity, or output performed by automated systems - the structural gauge of how much of the operation runs without human hands. Its strategic weight is the shape of the cost base it produces: high automation converts variable labor cost into fixed capital, which is excellent at high utilization and punishing in downturns, so the correct level depends on demand variability as much as on wage rates. The metric also tracks the resilience debate - automated lines concentrate output in fewer assets whose failure stops everything, which is why redundancy enters the automation business case as a cost, not a nicety. Read it with flexibility metrics: the ratio of changeover speed to volume per SKU determines whether automation adds or subtracts the ability to respond to product change.

## Formula

```
Automated Process Steps / Total Process Steps
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 259 (batch 1)
