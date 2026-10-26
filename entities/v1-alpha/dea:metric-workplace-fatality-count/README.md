# dea:metric-workplace-fatality-count

Candidate Performance Metric record for **Workplace Fatality Count** (WFC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-workplace-fatality-count`
- **Name:** Workplace Fatality Count
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WFC

## 2. Definition

Workplace Fatality Count (WFC) captures exposure to adverse outcomes for organizations tracking health & safety. The formula is Work-Related Fatalities per Period - reported in count (items per period). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The absolute number of work-related deaths in the period - the one safety metric with no normalization and no acceptable rate, since the argument that deaths are proportional to size is the argument safety management exists to reject. Its strategic weight is everything that follows: in most jurisdictions a fatality triggers regulatory investigation with potential personal liability for officers, criminal exposure in some regimes, and an organizational reckoning that no other event produces. This is the metric that defines safety leadership - the organizations that genuinely operate on zero-harm commitments treat any fatality as a system failure requiring deep-root redesign rather than an unlucky tail event. Trend analysis of a low absolute count is statistically meaningless, which is precisely the point: it is a governance metric, not a statistical one.

## Formula

```
Work-Related Fatalities per Period
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** health_safety

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 403 (batch 1)
