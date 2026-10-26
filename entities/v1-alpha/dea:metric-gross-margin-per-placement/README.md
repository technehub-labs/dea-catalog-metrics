# dea:metric-gross-margin-per-placement

Candidate Performance Metric record for **Gross Margin per Placement** (GMP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-margin-per-placement`
- **Name:** Gross Margin per Placement
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GMP

## 2. Definition

Gross Margin per Placement (GMP) addresses the economic value created or preserved and is a fixture of staffing & recruiting reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as (Placement Revenue - Payroll and Statutory Costs) / Placement Revenue; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Staffing & recruiting, it is a recognized element of the standard performance toolkit.

## 3. Context

Gross margin per placement measures the profit on each completed placement after candidate pay, payroll taxes, and direct costs, and it is the unit-economics metric that drives the entire staffing business model - a staffing agency's scale economics are simply margin per placement times placement volume, with most infrastructure costs fixed. The metric has a strategic tension inside it: high-margin placements (direct-hire, executive search) carry lower volume than low-margin ones (temp staffing, high-volume clerical), so portfolio mix determines both revenue and margin character. Temp-staffing margin dynamics also embed risk (workers comp, unemployment claims, conversion fees), which distort naive comparisons. Read with placements per recruiter (productivity), margin mix by service line, and gross margin trend versus bill-rate compression.

## Formula

```
(Placement Revenue - Payroll and Statutory Costs) / Placement Revenue
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** staffing_recruiting
- **Sector:** staffing_recruiting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1026 (batch 3)
