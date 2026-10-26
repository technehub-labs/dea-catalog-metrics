# dea:metric-mean-time-between-warranty-repairs

Candidate Performance Metric record for **Mean Time between Warranty Repairs** (MTBWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-between-warranty-repairs`
- **Name:** Mean Time between Warranty Repairs
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTBWR

## 2. Definition

Mean Time between Warranty Repairs (MTBWR) measures the quality of outputs and outcomes in the Automotive domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Vehicle Operating Time / Warranty Repair Events, expressed in hours. Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Automotive.

## 3. Context

Mean time between warranty repairs is the average operating interval a customer experiences before needing a covered repair, and it is a customer-lifetime reliability signal rather than a per-unit cost figure. It captures what warranty cost per vehicle misses: a vehicle could have high warranty cost from a single expensive part (like a transmission) yet still deliver long repair-free intervals, whereas a vehicle with frequent minor repairs will score well on cost per repair while frustrating the owner. Read alongside repair visits per vehicle and the spread between customers, since an owner with three shop trips in year one is a defection risk regardless of total cost.

## Formula

```
MTBWR = Vehicle Operating Time / Warranty Repair Events
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 747 (batch 2)
