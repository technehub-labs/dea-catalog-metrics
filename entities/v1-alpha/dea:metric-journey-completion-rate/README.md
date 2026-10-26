# dea:metric-journey-completion-rate

Candidate Performance Metric record for **Journey Completion Rate** (JCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-journey-completion-rate`
- **Name:** Journey Completion Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** JCR

## 2. Definition

Journey Completion Rate (JCR) captures how effectively a process or entity achieves its intended outcome for organizations tracking customer journey & experience. It is defined as Customers Completing Journey / Customers Starting Journey; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of customers who finish a defined end-to-end journey - onboarding, claims, checkout, renewal - without dropping out or needing a fallback channel. It converts experience quality into funnel arithmetic, linking friction directly to lost revenue. Honest reads require unambiguous journey boundaries: including rescue contacts inflates the rate, while strict channel-only definitions understate it. Segment by intent and cohort, since a blended rate hides the failure pockets that matter. Read with omnichannel consistency score and contact driver volume.

## Formula

```
Customers Completing Journey / Customers Starting Journey
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_journey_experience

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1248 (batch 4)
