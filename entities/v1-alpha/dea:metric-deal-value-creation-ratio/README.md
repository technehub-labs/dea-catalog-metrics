# dea:metric-deal-value-creation-ratio

Candidate Performance Metric record for **Deal Value Creation Ratio** (DVCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deal-value-creation-ratio`
- **Name:** Deal Value Creation Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DVCR

## 2. Definition

Within Mergers & Acquisitions, Deal Value Creation Ratio (DVCR) is used to gauge the economic value created or preserved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Acquired Enterprise Value Change / Purchase Price, measured in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Compares value created (shareholder return over benchmark, or realized value over price paid) against the acquisition cost. It is the long-horizon truth metric for M&A programs, immune to closing-day optimism. Attribution over multi-year windows is genuinely hard, and holding-company effects are real, so apply consistent benchmark conventions across deals. Read with post-merger synergy realization rate and customer attrition post-merger.

## Formula

```
Acquired Enterprise Value Change / Purchase Price
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** mergers_acquisitions

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1694 (batch 6)
