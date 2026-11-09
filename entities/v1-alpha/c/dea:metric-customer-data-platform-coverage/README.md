# dea:metric-customer-data-platform-coverage

Candidate Performance Metric record for **Customer Data Platform Coverage** (CDPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-data-platform-coverage`
- **Name:** Customer Data Platform Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDPC

## 2. Definition

Within Customer Analytics & Insights, Customer Data Platform Coverage (CDPC) is used to gauge capability maturity or development. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Profiles Unified in CDP / Known Customer Profiles, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of customers, interactions, or data sources unified with identity resolution into the CDP. Coverage below the level needed for personalization use cases makes downstream investments moot. Beware two inflations: counting onboarded-but-stale data sources as covered, and defining coverage by available records rather than usable, consented profiles. Read with privacy consent compliance rate and activation rates from CDP segments.

## Formula

```
CDPC = Profiles Unified in CDP / Known Customer Profiles
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** customer_analytics_insights

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1424 (batch 5)
