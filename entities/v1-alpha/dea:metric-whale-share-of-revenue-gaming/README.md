# dea:metric-whale-share-of-revenue-gaming

Candidate Performance Metric record for **Whale Share of Revenue (Gaming)** (WSR-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-whale-share-of-revenue-gaming`
- **Name:** Whale Share of Revenue (Gaming)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WSR-G

## 2. Definition

Whale Share of Revenue (Gaming) (WSR-G) captures exposure to adverse outcomes for organizations tracking gaming development & live operations. The formula is Top Spender Cohort Revenue / Total Revenue - reported in percent (%). It is a standard measure in the Gaming sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the concentration of revenue in top-spending players. Live-service economics often rest on a small spending minority, and this metric makes the fragility explicit: whale churn moves revenue materially, and concentration invites regulatory and reputational scrutiny of monetization design. Track cohort stability over time, since transient whales are a different risk than durable ones. Read with D30 retention (Deep Dive) and spending-distribution Lorenz curves.

## Formula

```
Top Spender Cohort Revenue / Total Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming_development_live_operations
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1987 (batch 6)
