# dea:metric-marketing-qualified-lead-volume

Candidate Performance Metric record for **Marketing Qualified Lead Volume** (MQL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-marketing-qualified-lead-volume`
- **Name:** Marketing Qualified Lead Volume
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MQL

## 2. Definition

Marketing Qualified Lead Volume (MQL) captures growth over time for organizations tracking marketing. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Count of Leads Meeting Scoring Threshold; the result is stated in count (items per period). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the count of leads meeting the agreed qualification threshold in a period. It matters because it prices the top of the funnel and predicts downstream pipeline. Teams can inflate it by loosening qualification criteria or counting form-fills and webinar signups with no intent. Read with MQL to SQL Conversion and Cost per Lead to check volume is not coming at the cost of quality.

## Formula

```
MQL = Count of Leads Meeting Scoring Threshold
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 105 (batch 1)
