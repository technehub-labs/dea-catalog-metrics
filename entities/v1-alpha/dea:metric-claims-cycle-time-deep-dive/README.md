# dea:metric-claims-cycle-time-deep-dive

Candidate Performance Metric record for **Claims Cycle Time (Deep Dive)** (CCT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claims-cycle-time-deep-dive`
- **Name:** Claims Cycle Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCT-D

## 2. Definition

Claims Cycle Time (Deep Dive) (CCT-D) captures how efficiently resources are converted into outputs for organizations tracking insurance claims deep dive. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Days from First Notification to Claim Closure, measured in days. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Insurance practice.

## 3. Context

Measures elapsed time from first notice of loss to settlement (or denial closure), the single strongest driver of claims satisfaction and expense. Fast cycle times reduce leakage (less time for inflated or fraudulent demands to fester) and legal escalation, but speed purchased by under-investigating converts into reopenings and bad-faith exposure. Segment by claim type and complexity band, since a blended average hides exactly where backlog hides. Read with straight-through claims settlement rate and claims leakage rate (Deep Dive).

## Formula

```
Days from First Notification to Claim Closure
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1541 (batch 6)
