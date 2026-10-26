# dea:metric-tax-collection-effectiveness

Candidate Performance Metric record for **Tax Collection Effectiveness** (TCE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tax-collection-effectiveness`
- **Name:** Tax Collection Effectiveness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TCE

## 2. Definition

Within Public Sector & Government, Tax Collection Effectiveness (TCE) is used to gauge how effectively a process or entity achieves its intended outcome. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Taxes Collected / Taxes Assessed, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Public sector practice.

## 3. Context

Actual tax revenue against the theoretically collectible amount - the tax-gap form being the most rigorous: the gap between what the law would raise and what the administration collects, which turns collection performance from an administrative statistic into a measurable fiscal-asset question. Its strategic significance is revenue-honesty: the size of the tax gap is what separates countries with similar tax systems and radically different revenue, and closing a fraction of it is often worth more than legislating new taxes - which is why revenue bodies treat effectiveness programs as fiscal policy, not administration. The honest measurement is gap-estimation-dependent (audits, operational data, and macroeconomic modeling each produce different gaps), so the metric is most meaningful as a trend under a fixed method. Read with the compliance-by-segment split, since the effectiveness strategy for large-business, small-business, and individual taxpayers differs entirely, and a blended effectiveness rate optimizes none of them.

## Formula

```
Taxes Collected / Taxes Assessed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** effectiveness
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** public_sector_government
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 645 (batch 2)
