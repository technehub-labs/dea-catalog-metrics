# dea:metric-cost-variance-in-construction

Candidate Performance Metric record for **Cost Variance in Construction** (CV-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-variance-in-construction`
- **Name:** Cost Variance in Construction
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CV-C

## 2. Definition

Cost Variance in Construction (CV-C) addresses conformance to standards, plans, or obligations and is a fixture of construction & engineering reporting. It is defined as (Earned Value of Work - Actual Cost) / Actual Cost; the result is stated in percent (%). In Construction & engineering, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures deviation of actual cost from the baseline budget. It matters because construction margins are thin and variance compounds through the project. Pending change-order revenue can mask cost overruns until claims resolve. Read with Change Order Rate and Rework Rate (Construction) to see whether variance control reflects true productivity or accounting treatment.

## Formula

```
(Earned Value of Work - Actual Cost) / Actual Cost
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_engineering
- **Sector:** construction_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 663 (batch 2)
