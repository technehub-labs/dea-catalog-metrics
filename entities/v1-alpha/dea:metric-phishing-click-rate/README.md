# dea:metric-phishing-click-rate

Candidate Performance Metric record for **Phishing Click Rate** (PCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-phishing-click-rate`
- **Name:** Phishing Click Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PCR

## 2. Definition

Phishing Click Rate (PCR) captures exposure to adverse outcomes for organizations tracking cybersecurity. It is defined as Users Clicking Simulated Phish / Users Targeted; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of simulated phishing recipients who click the lure. It matters because phishing remains the top initial access vector and training efficacy shows here. Gaming risk includes sending trivially obvious simulations to drive the rate down, or timing tests to avoid busy periods. Read with Phishing Reporting Rate and Security Training completion to confirm clicks fall while reporting rises, the healthy pattern.

## Formula

```
Users Clicking Simulated Phish / Users Targeted
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 323 (batch 1)
