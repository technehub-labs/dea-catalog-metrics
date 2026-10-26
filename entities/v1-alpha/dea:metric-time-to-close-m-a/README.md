# dea:metric-time-to-close-m-a

Candidate Performance Metric record for **Time to Close (M&A)** (TTC-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-close-m-a`
- **Name:** Time to Close (M&A)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TTC-M

## 2. Definition

Time to Close (M&A) (TTC-M) addresses how efficiently resources are converted into outputs and is a fixture of mergers & acquisitions reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Days from Term Sheet to Deal Close - reported in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures elapsed time from term sheet or diligence start to closing. Speed matters for value capture (deal fatigue, market movement, employee flight risk) and for integration planning stability. Fast closes from thin diligence are false wins: uncovered liabilities surface later at multiples of the weeks saved. Read with integration cost overrun rate and post-merger synergy realization trajectory.

## Formula

```
Days from Term Sheet to Deal Close
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** strategy
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** mergers_acquisitions

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1692 (batch 6)
