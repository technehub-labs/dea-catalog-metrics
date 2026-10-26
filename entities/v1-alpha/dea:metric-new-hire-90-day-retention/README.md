# dea:metric-new-hire-90-day-retention

Candidate Performance Metric record for **New Hire 90-Day Retention** (NH90) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-new-hire-90-day-retention`
- **Name:** New Hire 90-Day Retention
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NH90

## 2. Definition

New Hire 90-Day Retention (NH90) captures the quality of outputs and outcomes for organizations tracking human resources. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Hires Retained at 90 Days / Total Hires; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of new hires still employed after 90 days. It matters because early attrition signals hiring or onboarding failure at the cheapest possible point to fix it. Gaming risk includes stretching the window or converting would-be leavers into unpaid leave so they count as retained. Read with Time to Productivity and Offer Acceptance Rate to trace whether early retention reflects genuine fit.

## Formula

```
NH90 = Hires Retained at 90 Days / Total Hires
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 128 (batch 1)
