# dea:metric-sponsorship-revenue-growth

Candidate Performance Metric record for **Sponsorship Revenue Growth** (SRG-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sponsorship-revenue-growth`
- **Name:** Sponsorship Revenue Growth
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SRG-S

## 2. Definition

Sponsorship Revenue Growth (SRG-S) measures growth over time in the Sports & Events domain. Its calculation is (Sponsorship Revenue_current - Revenue_prior) / Revenue_prior, measured in percent (%). It originates from and is most used in Sports & events practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Sponsorship revenue growth measures the expansion of partnership income - jersey patches, naming rights, media placement - and it is the margin-expansion channel of sports business because sponsorship carries near-100 percent margin, flows to the bottom line in ways ticket revenue (with its cost of goods) cannot. The growth driver is the shift from logo-placement deals to integrated partnerships, where sponsors buy engagement assets and data access rather than signage, enabling premium pricing. The measurement honesty issue is activation: sponsorship value without sponsor activation underdelivers for partners and suppresses renewal economics. Inventory depletion is the strategic constraint - there are only so many premium placements before dilution sets in. Read with sponsorship revenue per attendance-hour, renewal rates by partner tier, share of revenue from sponsorship, and non-endemic sponsor share as diversification signal.

## Formula

```
SRG-S = (Sponsorship Revenue_current - Revenue_prior) / Revenue_prior
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** sports_events
- **Sector:** sports_events

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 949 (batch 3)
