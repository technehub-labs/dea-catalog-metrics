# dea:metric-average-revenue-per-user-telecom

Candidate Performance Metric record for **Average Revenue per User (Telecom)** (ARPU-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-revenue-per-user-telecom`
- **Name:** Average Revenue per User (Telecom)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ARPU-T

## 2. Definition

Within Telecommunications, Average Revenue per User (Telecom) (ARPU-T) is used to gauge the economic value created or preserved. The formula is Service Revenue / Average Subscribers - reported in currency per unit. It is a standard measure in the Telecommunications sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Telecom service revenue divided by the average subscriber base - the unit-economics gauge of connectivity businesses, where the strategic drama is the migration customers make over decades: from voice to data, from basic to premium tiers, from owned-spectrum to MVNO economics, with ARPU tracking each transition. Its significance is the chess it plays against churn and subscriber growth: pricing that lifts ARPU feeds churn, and acquisition that lifts subscribers dilutes ARPU, so operators manage the triangle rather than any single metric. Read the decomposition: ARPU blended across prepaid and postpaid, consumer and enterprise moves with mix as much as with pricing, and the honest trend isolates like-for-like cohorts. In saturated markets, ARPU is essentially the only growth lever left, which is why it is the number telecom boards watch most closely.

## Formula

```
ARPU-T = Service Revenue / Average Subscribers
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecommunications
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 524 (batch 1)
