# dea:metric-mean-distance-between-failures-rolling-stock

Candidate Performance Metric record for **Mean Distance between Failures (Rolling Stock)** (MDBF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-distance-between-failures-rolling-stock`
- **Name:** Mean Distance between Failures (Rolling Stock)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MDBF

## 2. Definition

Mean Distance between Failures (Rolling Stock) (MDBF) measures exposure to adverse outcomes in the Rail Transport domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Distance Operated / Service-Affecting Failures - reported in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Rail sector.

## 3. Context

Mean distance between failures for rolling stock measures reliability per kilometre operated, and it is the engineering quality metric that underlies fleet availability - each failure costs delay minutes, engineering response, and potentially a service cancellation, so MDBF is where rolling-stock design and maintenance show their quality. The definition matters enormously: what counts as a failure (service-affecting versus technical defect) varies across operators, making cross-comparison treacherous without definitional alignment. Failure distribution is the management information: door system failures typically dominate (they interact with station dwell and passenger behavior), and seasonal patterns (heating, air conditioning) shift failure modes. Read with MDBF by subsystem, failure Pareto over time, miles-accumulated per unit (failure rates rise with age and heavy-overhaul cycle position), and correlation with delay-minute attribution.

## Formula

```
MDBF = Distance Operated / Service-Affecting Failures
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_transport
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 995 (batch 3)
