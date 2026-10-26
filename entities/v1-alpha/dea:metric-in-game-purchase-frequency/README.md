# dea:metric-in-game-purchase-frequency

Candidate Performance Metric record for **In-Game Purchase Frequency** (IGPF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-in-game-purchase-frequency`
- **Name:** In-Game Purchase Frequency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IGPF

## 2. Definition

Within Gaming, In-Game Purchase Frequency (IGPF) is used to gauge the economic value created or preserved. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Purchases / Active Players per Period - reported in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Gaming sector.

## 3. Context

Measures how often players make in-game purchases per period. It matters because monetization in gaming depends on repeat spend, not first conversion. Frequency can be driven by pay-to-win mechanics that lift short-term revenue while burning the player base. Read with Player Retention (D1/D7/D30) and churn sentiment to confirm monetization coexists with a healthy community.

## Formula

```
Purchases / Active Players per Period
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 712 (batch 2)
