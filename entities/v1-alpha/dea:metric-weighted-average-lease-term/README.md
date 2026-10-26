# dea:metric-weighted-average-lease-term

Candidate Performance Metric record for **Weighted Average Lease Term** (WALT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-weighted-average-lease-term`
- **Name:** Weighted Average Lease Term
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WALT

## 2. Definition

Weighted Average Lease Term (WALT) measures exposure to adverse outcomes in the Real Estate & Mortgage Standard Measures domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Lease Years Remaining weighted by Rental Income, expressed in years. Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Real estate.

## 3. Context

Measures the average remaining lease duration across tenants, weighted by income. WALT is the income durability signal for investors and lenders. WALT that counts options not yet exercised overstates security. Read with tenant retention rate (Real Estate) and occupancy rate.

## Formula

```
Lease Years Remaining weighted by Rental Income
```

## Unit

- **Unit reference:** `dea:unit-years`
- **Unit:** years
- **Unit label (as published):** years

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** real_estate_mortgage_standard_measures
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4221 (batch 10)
