# dea:metric-data-quality-rate-market-data

Candidate Performance Metric record for **Data Quality Rate (Market Data)** (DQRMD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-quality-rate-market-data`
- **Name:** Data Quality Rate (Market Data)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DQRMD

## 2. Definition

Data Quality Rate (Market Data) (DQRMD) measures the quality of outputs and outcomes in the Investment Risk & Middle Office Operations domain. It is computed as Market Data Fields Passing Checks / Fields, expressed in percent (%). Its use is concentrated in Investment management. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Market Data Fields Passing Checks / Fields
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3476 (batch 7)
