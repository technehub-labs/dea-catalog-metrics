# dea:metric-baggage-mishandling-rate

Candidate Performance Metric record for **Baggage Mishandling Rate** (BMR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-baggage-mishandling-rate`
- **Name:** Baggage Mishandling Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BMR

## 2. Definition

Baggage Mishandling Rate (BMR) captures the quality of outputs and outcomes for organizations tracking airlines & aviation. It is defined as Mishandled Bags / Total Bags Handled; the result is stated in ratio (x:1 or x). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. In Airlines & aviation, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures mishandled bags per 1,000 passengers. It matters because baggage failure is a top driver of airline complaints and compensation cost. Gaming risk includes tightening what counts as mishandled (e.g. excluding late-delivered rather than lost bags). Read with On-Time Performance and Complaints per 1,000 Passengers to confirm handling improvements are customer-felt.

## Formula

```
Mishandled Bags / Total Bags Handled
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airlines_aviation
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 653 (batch 2)
