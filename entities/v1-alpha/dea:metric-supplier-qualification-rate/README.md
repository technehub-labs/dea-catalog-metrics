# dea:metric-supplier-qualification-rate

Candidate Performance Metric record for **Supplier Qualification Rate** (SQR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-qualification-rate`
- **Name:** Supplier Qualification Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SQR

## 2. Definition

Supplier Qualification Rate (SQR) measures the quality of outputs and outcomes in the Procurement domain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Approved Suppliers / Suppliers Assessed, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of candidate suppliers that pass onboarding and qualification checks. It matters because it gates supply risk and quality before any purchase is made. Gaming risk includes waving through suppliers when capacity is tight, storing future quality problems. Read with Supplier Defect Rate and Supplier On-Time Delivery to check that qualification rigor holds under pressure.

## Formula

```
SQR = Approved Suppliers / Suppliers Assessed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** procurement

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 230 (batch 1)
