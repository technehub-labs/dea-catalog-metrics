# dea:metric-cost-per-case

Candidate Performance Metric record for **Cost per Case** (CPC2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-case`
- **Name:** Cost per Case
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPC2

## 2. Definition

A Healthcare indicator, Cost per Case (CPC2) quantifies how efficiently resources are converted into outputs. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Total Treatment Cost / Cases Treated, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Healthcare.

## 3. Context

The full cost of treating an episode, divided by cases - the unit-economics metric of healthcare delivery, where pricing pressure, reimbursement bundling, and margin analysis all operate on exactly this number. Its strategic significance is the payment-regime alignment: as payment models shift toward bundled and episode-based reimbursement, cost per case stops being an internal statistic and becomes the direct determinant of whether the organization makes or loses money on each service line. The measurement honesty requirement is cost allocation: clinical costs trace to cases, but overhead allocation conventions can move cost per case materially, and improvement claims that are really allocation changes are the metric's classic failure. Read with case-mix index: cost per case rising while case-mix rises is acuity, not inefficiency - and the risk-adjusted cost trend is the number that tells the truth about productivity.

## Formula

```
Total Treatment Cost / Cases Treated
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 468 (batch 1)
