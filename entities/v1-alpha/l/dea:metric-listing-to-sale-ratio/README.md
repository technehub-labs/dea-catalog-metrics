# dea:metric-listing-to-sale-ratio

Candidate Performance Metric record for **Listing to Sale Ratio** (LSR-RE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-listing-to-sale-ratio`
- **Name:** Listing to Sale Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LSR-RE

## 2. Definition

Within Real Estate Brokerage, Listing to Sale Ratio (LSR-RE) is used to gauge how effectively a process or entity achieves its intended outcome. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Listings Sold within Period / Listings Taken - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Real estate sector.

## 3. Context

The listing to sale ratio measures homes sold against homes listed, and it is the market-temperature metric of real estate brokerage - a high ratio signals a seller's market with listings moving to contract quickly, while a low ratio signals overpricing, weakening demand, or both. Because it is market-level rather than company-level, brokers use it as context, not performance. Its predictive content is real but lagging: by the time the ratio turns, price momentum has already begun to shift. Submarket variation is extreme - the same metro can have a hot submarket and a cold one simultaneously, so composite ratios conceal what matters for pricing decisions. Read with days on market (its speed companion), sale-to-list price ratio (pricing-received measure), and months-of-inventory as the balance indicator.

## Formula

```
LSR-RE = Listings Sold within Period / Listings Taken
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** real_estate_brokerage
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1010 (batch 3)
