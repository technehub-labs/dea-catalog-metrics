# dea:metric-app-store-rating

Candidate Performance Metric record for **App Store Rating** (ASR-MOB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-app-store-rating`
- **Name:** App Store Rating
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ASR-MOB

## 2. Definition

App Store Rating (ASR-MOB) measures the economic value created or preserved in the Mobile & Client Development domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Average User Rating across App Stores - reported in score (points). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Software sector.

## 3. Context

Measures the average user rating of the mobile app in public stores. It is the most visible public quality scoreboard for mobile products. Recent-version filtering matters: lifetime averages mask current releases. Read with app uninstall rate and mobile app crash-free session rate.

## Formula

```
Average User Rating across App Stores
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mobile_client_development
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3248 (batch 7)
