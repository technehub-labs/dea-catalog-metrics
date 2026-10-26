# dea:metric-product-market-fit-survey-score

Candidate Performance Metric record for **Product-Market Fit Survey Score** (PMFS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-market-fit-survey-score`
- **Name:** Product-Market Fit Survey Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PMFS

## 2. Definition

Within Startup & Venture-Backed Business, Product-Market Fit Survey Score (PMFS) is used to gauge the engagement or satisfaction of the people involved. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Percent of Users Very Disappointed if Product Removed, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of users who would be very disappointed if the product disappeared, per the standard PMF survey methodology. It is the canonical demand-side evidence of product-market fit, and it is the gate metric between early iteration and scaling spend: pouring growth capital ahead of PMF is the classic startup capital incinerator. Survey sampling must include churned users, or the score is survivorship flattery. Read with retention curves and willingness-to-pay evidence.

## Formula

```
Percent of Users Very Disappointed if Product Removed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** startup_venture_backed_business

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2446 (batch 6)
