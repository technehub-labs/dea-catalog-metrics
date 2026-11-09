# dea:metric-cost-per-location-opening

Candidate Performance Metric record for **Cost per Location Opening** (CLO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-location-opening`
- **Name:** Cost per Location Opening
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CLO

## 2. Definition

A Franchise & Multi-site indicator, Cost per Location Opening (CLO) quantifies how efficiently resources are converted into outputs. The formula is Total Opening Costs / New Locations Opened - reported in currency per unit. It is a standard measure in the Franchise & multi-site sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures average cost to open a new franchise or store location. It matters because opening cost determines expansion economics and payback timelines. Costs can be undercounted by capitalizing pre-opening expenses into other budgets. Read with Time to Break Even for new locations and Same-Store Sales to weigh opening efficiency against location quality.

## Formula

```
CLO = Total Opening Costs / New Locations Opened
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** franchise_multi_site
- **Sector:** franchise_multi_site

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 811 (batch 2)
