# dea:metric-average-minute-audience

Candidate Performance Metric record for **Average Minute Audience** (AMA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-minute-audience`
- **Name:** Average Minute Audience
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AMA

## 2. Definition

Average Minute Audience (AMA) measures the engagement or satisfaction of the people involved in the Media & Entertainment domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Average Viewers or Listeners Watching per Minute, measured in count (items per period). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Media & entertainment practice.

## 3. Context

The average number of viewers or listeners per minute across a broadcast period - the audience metric that broadcast economics is actually built on, and deliberately unlike reach or total audience: it measures the average simultaneous attention, which is the number advertisers buy against and the one that prices commercial inventory. Its strategic significance is the currency status: television and radio markets historically transact on average-minute-audience (and its rating-point form), which means the metric is not just measurement but money - a share point of AMA in a key demographic is a price list entry. The measurement shift is the strategic story: panel-based audience measurement is being displaced by large-return-path datasets and streaming data, changing what the number is built from, and the transition is contested because it changes the money. Read with the demographic split, since advertising value concentrates in the age segments buyers pay for, and a stable headline AMA with demographic decay is a revenue problem the total never shows.

## Formula

```
AMA = Average Viewers or Listeners Watching per Minute
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** media_entertainment
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 690 (batch 2)
