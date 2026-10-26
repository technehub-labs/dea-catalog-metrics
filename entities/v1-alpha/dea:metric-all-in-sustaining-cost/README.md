# dea:metric-all-in-sustaining-cost

Candidate Performance Metric record for **All-In Sustaining Cost** (AISC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-all-in-sustaining-cost`
- **Name:** All-In Sustaining Cost
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AISC

## 2. Definition

All-In Sustaining Cost (AISC) addresses the economic value created or preserved and is a fixture of mining & metals reporting. The formula is Total Sustaining Production Cost / Unit of Metal Produced - reported in currency per unit. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Mining & metals sector.

## 3. Context

All-In Sustaining Cost (AISC), standardized by the World Gold Council in 2013, aggregates operating costs, sustaining capital, and corporate overheads into one figure per ounce, finally making gold mines comparable after years of selective cash-cost reporting. Its honest value depends on the sustaining-versus-growth capital boundary: classifying development spend as growth is the classic way to depress AISC while still spending heavily. Because it excludes growth and exploration capital, AISC understates total cost of ownership. Pair with all-in cost for the full picture and with the gold-to-AISC margin, which is the real revenue signal.

## Formula

```
Total Sustaining Production Cost / Unit of Metal Produced
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** mining_metals
- **Sector:** mining_metals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 718 (batch 2)
