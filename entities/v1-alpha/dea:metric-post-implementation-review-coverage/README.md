# dea:metric-post-implementation-review-coverage

Candidate Performance Metric record for **Post-Implementation Review Coverage** (PIRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-post-implementation-review-coverage`
- **Name:** Post-Implementation Review Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PIRC

## 2. Definition

Post-Implementation Review Coverage (PIRC) addresses the economic value created or preserved and is a fixture of pmo & portfolio governance reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Closed Initiatives with PIR / Closed Initiatives - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of completed initiatives undergoing structured post-implementation review. PIRs close the learning loop that feeds estimation and business case quality. Reviews without honest benefit assessment are file closure. Read with benefits realization rate and lessons learned capture rate.

## Formula

```
Closed Initiatives with PIR / Closed Initiatives
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pmo_portfolio_governance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3413 (batch 7)
