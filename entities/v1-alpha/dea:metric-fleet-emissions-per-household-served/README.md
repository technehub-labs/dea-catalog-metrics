# dea:metric-fleet-emissions-per-household-served

Candidate Performance Metric record for **Fleet Emissions per Household Served** (FEHS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fleet-emissions-per-household-served`
- **Name:** Fleet Emissions per Household Served
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FEHS

## 2. Definition

Fleet Emissions per Household Served (FEHS) measures environmental and social sustainability performance in the Waste & Environmental Services domain. The formula is Fleet CO2e / Households Served - reported in ratio (x:1 or x). It is a standard measure in the Environmental services sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures collection-fleet emissions normalized by households served. It matters because it is the key decarbonization efficiency metric for waste logistics. Route-efficiency gains can be offset by heavier vehicles, which per-household normalization may reveal. Read with Fuel Efficiency and Route Density metrics to confirm emission cuts are structural.

## Formula

```
Fleet CO2e / Households Served
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** waste_environmental_services
- **Sector:** environmental_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 820 (batch 2)
