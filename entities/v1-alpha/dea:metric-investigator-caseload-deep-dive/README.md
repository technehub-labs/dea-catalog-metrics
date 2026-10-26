# dea:metric-investigator-caseload-deep-dive

Candidate Performance Metric record for **Investigator Caseload (Deep Dive)** (ICL-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-investigator-caseload-deep-dive`
- **Name:** Investigator Caseload (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ICL-D

## 2. Definition

Investigator Caseload (Deep Dive) (ICL-D) captures the utilization or availability of capacity for organizations tracking insurance fraud & financial crime. It is computed as Open Cases per Investigator, expressed in count (items per period). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Financial Services.

## Formula

```
Open Cases per Investigator
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** risk
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_fraud_financial_crime
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2474 (batch 6)
