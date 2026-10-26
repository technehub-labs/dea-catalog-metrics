# dea:metric-cost-variance-percent-deep-dive

Candidate Performance Metric record for **Cost Variance Percent (Deep Dive)** (CVP-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-variance-percent-deep-dive`
- **Name:** Cost Variance Percent (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CVP-D

## 2. Definition

Cost Variance Percent (Deep Dive) (CVP-D) captures conformance to standards, plans, or obligations for organizations tracking project management (deep dive). It is computed as (Actual Cost - Baseline Cost) / Baseline Cost, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures deviation of actual spend from the approved budget baseline. Cost variance reveals whether estimates, controls, or scope discipline are failing. Variance hidden through capitalization and category shifting surfaces later and larger. Read with estimate accuracy - cost and portfolio cost overrun ratio.

## Formula

```
(Actual Cost - Baseline Cost) / Baseline Cost
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2930 (batch 7)
