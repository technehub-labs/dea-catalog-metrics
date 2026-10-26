# dea:metric-chargeback-ratio-deep-dive

Candidate Performance Metric record for **Chargeback Ratio (Deep Dive)** (CBR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-chargeback-ratio-deep-dive`
- **Name:** Chargeback Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CBR-D

## 2. Definition

Chargeback Ratio (Deep Dive) (CBR-D) captures exposure to adverse outcomes for organizations tracking payments & cards (deep dive). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Chargebacks / Transactions - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Payments sector.

## 3. Context

Measures disputed transactions as a share of sales volume. It is the merchant-health and program-integrity metric of card networks: exceeding network thresholds triggers monitoring programs, fines, and ultimately loss of processing, and rising chargebacks usually indicate fulfillment or fraud problems upstream. Reason-code distribution directs the fix - fraud versus service disputes are different diseases. Read with fraud rate and dispute-resolution win rates.

## Formula

```
Chargebacks / Transactions
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** payments_cards_deep_dive
- **Sector:** payments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2090 (batch 6)
