# dea:metric-production-per-employee-deep-dive

Candidate Performance Metric record for **Production per Employee (Deep Dive)** (PPE-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-production-per-employee-deep-dive`
- **Name:** Production per Employee (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PPE-D

## 2. Definition

Production per Employee (Deep Dive) (PPE-D) measures how efficiently resources are converted into outputs in the Automotive Manufacturing (Deep Dive) domain. Its calculation is Vehicles / Employee, measured in ratio (x:1 or x). It originates from and is most used in Automotive practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures output per manufacturing employee, normalized by plant. It is the labor-productivity metric of automotive operations, where automation, line balancing, and absence management all converge. Comparisons across plants need automation-adjustment, since a highly automated line's productivity is capital, not labor discipline. Read with labor cost per vehicle and absence and overtime patterns for the human-side detail.

## Formula

```
Vehicles / Employee
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive_manufacturing_deep_dive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2371 (batch 6)
