# dea:metric-revenue-per-employee-standard

Candidate Performance Metric record for **Revenue per Employee (Standard)** (RPEDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-employee-standard`
- **Name:** Revenue per Employee (Standard)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPEDD

## 2. Definition

Revenue per Employee (Standard) (RPEDD) captures how efficiently resources are converted into outputs for organizations tracking standard workforce & pay metrics. The formula is Revenue / Average Headcount - reported in currency per unit. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures revenue divided by headcount as the standard productivity comparator. It enables cross-company and cross-time efficiency comparison. Averages blend functions; segment views carry more insight. Read with revenue per FTE (Deep Dive) and profit per employee (Deep Dive).

## Formula

```
RPEDD = Revenue / Average Headcount
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** standard_workforce_pay_metrics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4119 (batch 9)
