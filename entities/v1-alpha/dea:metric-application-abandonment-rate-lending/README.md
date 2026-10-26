# dea:metric-application-abandonment-rate-lending

Candidate Performance Metric record for **Application Abandonment Rate (Lending)** (AAR-L) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-application-abandonment-rate-lending`
- **Name:** Application Abandonment Rate (Lending)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AAR-L

## 2. Definition

Application Abandonment Rate (Lending) (AAR-L) captures exposure to adverse outcomes for organizations tracking retail banking & lending. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Abandoned Applications / Started Applications - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Banking sector.

## 3. Context

Measures the share of started loan applications never submitted. It matters because abandonment at the application stage is lost demand and signals friction or disclosure fatigue. It can be gamed by counting pre-filled direct-mail applications as completed starts. Read with Loan Application Approval Rate and Time to Decision to see whether friction or decline fear drives abandonment.

## Formula

```
Abandoned Applications / Started Applications
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 839 (batch 3)
