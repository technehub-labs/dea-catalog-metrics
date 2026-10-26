# dea:metric-false-decline-rate-deep-dive

Candidate Performance Metric record for **False Decline Rate (Deep Dive)** (FDR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-false-decline-rate-deep-dive`
- **Name:** False Decline Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FDR-P

## 2. Definition

False Decline Rate (Deep Dive) (FDR-P) captures the economic value created or preserved for organizations tracking payments & cards (deep dive). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Legitimate Transactions Declined / Declined; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Payments, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures legitimate transactions declined by risk controls. False declines are the invisible tax of fraud prevention: they cost nothing on a loss line while destroying revenue, customer experience, and lifetime value, and issuers systematically underestimate them. Measurement requires declined-transaction re-purchase evidence or benchmark inference, since cardholders rarely report. Read with authorization approval rate (Deep Dive) and fraud strategy review cadence.

## Formula

```
Legitimate Transactions Declined / Declined
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** payments_cards_deep_dive
- **Sector:** payments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2089 (batch 6)
