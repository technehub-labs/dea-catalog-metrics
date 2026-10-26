# dea:metric-card-fraud-rate-basis-points

Candidate Performance Metric record for **Card Fraud Rate Basis Points** (CFRB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-card-fraud-rate-basis-points`
- **Name:** Card Fraud Rate Basis Points
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CFRB

## 2. Definition

Within Payments & Cards (Deep Dive), Card Fraud Rate Basis Points (CFRB) is used to gauge exposure to adverse outcomes. Its calculation is Fraud Value / Transaction Value, measured in events per thousand or million (scaled). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Payments practice.

## 3. Context

Measures card fraud losses as basis points of transaction volume. It is the industry-standard fraud metric, enabling issuer, network, and portfolio comparisons, and it is cyclical - fraud migrates to the weakest control environment. Rate improvements from declining cross-border volume rather than control improvements reverse quickly. Read with false decline rate (Deep Dive) for the customer-experience cost of controls.

## Formula

```
Fraud Value / Transaction Value
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2094 (batch 6)
