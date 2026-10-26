# dea:metric-total-cost-of-ownership-per-application-deep-dive

Candidate Performance Metric record for **Total Cost of Ownership per Application (Deep Dive)** (TCOA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-total-cost-of-ownership-per-application-deep-dive`
- **Name:** Total Cost of Ownership per Application (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TCOA-D

## 2. Definition

Total Cost of Ownership per Application (Deep Dive) (TCOA-D) captures how efficiently resources are converted into outputs for organizations tracking it financial management & technology budgeting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Annual All-in Application Cost / Application - reported in currency value. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the full annual cost of each application including license, infrastructure, and support effort. TCO exposes the applications whose true cost dwarfs their usage. Allocation of shared platform costs is the contestable part. Read with application rationalization progress rate and run versus change spend ratio.

## Formula

```
Annual All-in Application Cost / Application
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_financial_management_technology_budgeting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3179 (batch 7)
