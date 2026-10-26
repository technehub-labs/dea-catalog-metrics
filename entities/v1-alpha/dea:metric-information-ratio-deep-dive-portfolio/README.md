# dea:metric-information-ratio-deep-dive-portfolio

Candidate Performance Metric record for **Information Ratio (Deep Dive - Portfolio)** (IRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-information-ratio-deep-dive-portfolio`
- **Name:** Information Ratio (Deep Dive - Portfolio)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IRDD

## 2. Definition

Within Investment Performance Measurement, Information Ratio (Deep Dive - Portfolio) (IRDD) is used to gauge the economic value created or preserved. The formula is Excess Return / Tracking Error - reported in ratio (x:1 or x). It is a standard measure in the Investment management sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The information ratio, central to the active-management tradition of Grinold and Kahn, divides excess return over the benchmark by tracking error - the quality of active bets rather than their size. An IR of 0.5 sustained is good, above 1.0 exceptional; Grinold's fundamental law (IR = skill x sqrt(breadth)) links it to how many independent bets a manager can make. Use it when the benchmark is a genuine mandate (it is meaningless without one), and compare only managers against the same index.

## Formula

```
Excess Return / Tracking Error
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Active management tradition (Grinold & Kahn)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3437 (batch 7)
