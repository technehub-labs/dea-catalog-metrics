# dea:metric-cost-per-content-hour-gaming

Candidate Performance Metric record for **Cost per Content Hour (Gaming)** (CPCH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-content-hour-gaming`
- **Name:** Cost per Content Hour (Gaming)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPCH

## 2. Definition

Cost per Content Hour (Gaming) (CPCH) addresses how efficiently resources are converted into outputs and is a fixture of gaming development & live operations reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Development Cost / Playable Hours Delivered, measured in currency per unit. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Gaming practice.

## 3. Context

Measures development and live-ops cost per hour of player engagement delivered. It is the efficiency bridge between production spend and the engagement product players consume, and it disciplines the industry's habit of confusing content volume with content value. Compare within genre and monetization model, since live-service content amortizes differently than premium. Read with engagement-hour trends and content ROI by release.

## Formula

```
CPCH = Development Cost / Playable Hours Delivered
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming_development_live_operations
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1992 (batch 6)
