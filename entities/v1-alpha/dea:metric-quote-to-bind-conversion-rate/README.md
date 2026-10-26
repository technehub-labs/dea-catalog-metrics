# dea:metric-quote-to-bind-conversion-rate

Candidate Performance Metric record for **Quote-to-Bind Conversion Rate** (QBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-quote-to-bind-conversion-rate`
- **Name:** Quote-to-Bind Conversion Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** QBR

## 2. Definition

Quote-to-Bind Conversion Rate (QBR) addresses growth over time and is a fixture of insurance underwriting reporting. It is defined as Policies Bound / Quotes Issued; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Insurance, it is a recognized element of the standard performance toolkit.

## Formula

```
QBR = Policies Bound / Quotes Issued
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_underwriting
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1501 (batch 6)
