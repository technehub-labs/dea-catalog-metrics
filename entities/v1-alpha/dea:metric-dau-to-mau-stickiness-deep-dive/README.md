# dea:metric-dau-to-mau-stickiness-deep-dive

Candidate Performance Metric record for **DAU-to-MAU Stickiness (Deep Dive)** (DMS-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dau-to-mau-stickiness-deep-dive`
- **Name:** DAU-to-MAU Stickiness (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DMS-D

## 2. Definition

DAU-to-MAU Stickiness (Deep Dive) (DMS-D) addresses the engagement or satisfaction of the people involved and is a fixture of gaming development & live operations reporting. Its calculation is DAU / MAU, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Gaming practice.

## 3. Context

Measures daily actives as a share of monthly actives, the standard stickiness ratio of engaged communities. High stickiness (habits formed) predicts long-term retention and monetization depth, while low stickiness signals event-driven audiences that churn with content cadence. Genre norms differ enormously, so benchmark within genre, not across the industry. Read with session-frequency distributions and whale share of revenue (Gaming).

## Formula

```
DAU / MAU
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming_development_live_operations
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1981 (batch 6)
