# dea:metric-care-worker-turnover

Candidate Performance Metric record for **Care Worker Turnover** (CWT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-care-worker-turnover`
- **Name:** Care Worker Turnover
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CWT

## 2. Definition

Care Worker Turnover (CWT) measures exposure to adverse outcomes in the Elder & Social Care domain. It is defined as Care Worker Departures / Average Care Workforce; the result is stated in percent (%). In Social care, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Care worker turnover measures the annualized separation rate of direct-care staff, and in elder care it runs structurally high (industry surveys commonly report annual rates above 70 percent for nursing staff) - and it is the root-cause metric for much else: continuity of care drives resident outcomes (agitation, pressure ulcers, falls), and every departure costs real money in recruiting, onboarding, and agency backfill. The driver structure is well documented: wages relative to competing employers (retail, hospitality), workload from understaffing (a self-reinforcing cycle where turnover causes the understaffing that causes turnover), and career-ladder absence. The honest measurement is unit-level since a few hard units can dominate facility averages. Read with turnover by unit and shift, agency-utilization cost trend, tenure distribution (early-tenure churn is a distinct fixable problem), and exit-interview reason clustering.

## Formula

```
Care Worker Departures / Average Care Workforce
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** elder_social_care
- **Sector:** social_care

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1200 (batch 4)
