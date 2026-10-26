# dea:metric-cost-of-quality-ratio

Candidate Performance Metric record for **Cost of Quality Ratio** (COQR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-of-quality-ratio`
- **Name:** Cost of Quality Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** COQR

## 2. Definition

A Product Costing & Margin Management indicator, Cost of Quality Ratio (COQR) quantifies the economic value created or preserved. It is defined as Cost of Poor Quality / Total Production Cost; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Expresses total quality costs - prevention, appraisal, internal failure, and external failure - as a share of revenue or cost of goods sold. It reframes quality spending from a compliance expense into an economic trade-off, since a dollar moved from failure costs to prevention typically returns multiples. The gaming risk is undercounting external failure (warranty, brand damage, lost sales), which flatters the ratio precisely when quality is worst. Read with warranty cost trends, defect rates, and customer complaint volume.

## Formula

```
Cost of Poor Quality / Total Production Cost
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_costing_margin_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1242 (batch 4)
