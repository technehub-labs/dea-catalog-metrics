# dea:metric-lifetime-value-per-player

Candidate Performance Metric record for **Lifetime Value per Player** (LTV-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-lifetime-value-per-player`
- **Name:** Lifetime Value per Player
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LTV-G

## 2. Definition

Within Gaming, Lifetime Value per Player (LTV-G) is used to gauge the economic value created or preserved. It is computed as Average Lifetime Revenue per Player, expressed in currency value. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Gaming.

## 3. Context

The projected total revenue a player generates - the unit-economics foundation of the gaming business model, because user acquisition is a bidding market: studios buy installs through ad networks against predicted LTV, and the LTV-to-CAC margin is the growth engine's profit margin - misestimate LTV and the entire acquisition program buys losses at scale. Its strategic significance is the model-dependence honesty: LTV is projected from early-cohort behavior (day-1/7/30 retention and early spend patterns), which means it inherits every retention-analysis confound - source mix, seasonality, creative quality - and updating the model from realized cohorts is what separates a bidding engine from a loss engine. The measurement discipline is per-segment: LTV by acquisition source, geography, and platform differ enormously, so a blended LTV is a marketing-mix average, not a price. Read with payback period: LTV realized over 18 months cannot fund acquisition spend on 30-day cash cycles, which is why payback-window LTV is the operative number.

## Formula

```
Average Lifetime Revenue per Player
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 711 (batch 2)
