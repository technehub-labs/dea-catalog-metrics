# dea:metric-burn-multiple

Candidate Performance Metric record for **Burn Multiple** (BM-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-burn-multiple`
- **Name:** Burn Multiple
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BM-S

## 2. Definition

A Startup & Venture-Backed Business indicator, Burn Multiple (BM-S) quantifies how efficiently resources are converted into outputs. Its calculation is Net Burn / Net New ARR, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The burn multiple, coined by David Sacks (Craft Ventures), is net burn divided by net new ARR - how many dollars of burn each dollar of new recurring revenue costs. Under 1x is excellent, 1-2x healthy, above 3x a red flag, and above 5x a signal the business may be fundamentally unprofitable in growth. Its value is capital-efficiency honesty: two companies can grow 100% while burning wildly different amounts. It degrades as a metric when net new ARR is near zero (the ratio explodes) and it is sensitive to ARR definition - use it for Series A-C software, not for pre-revenue teams.

## Formula

```
Net Burn / Net New ARR
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** startup_venture_backed_business

## Attribution

- **Source credit:** David Sacks (Craft Ventures)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2441 (batch 6)
