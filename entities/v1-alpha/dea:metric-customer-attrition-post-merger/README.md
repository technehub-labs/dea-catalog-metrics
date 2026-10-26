# dea:metric-customer-attrition-post-merger

Candidate Performance Metric record for **Customer Attrition Post-Merger** (CAPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-attrition-post-merger`
- **Name:** Customer Attrition Post-Merger
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CAPM

## 2. Definition

Customer Attrition Post-Merger (CAPM) measures the retention of customers, users, or assets over time in the Mergers & Acquisitions domain. Its calculation is Customers Lost in Year One / Customers at Close, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures customer losses following integration - a direct test of whether disruption (pricing changes, channel conflicts, service gaps) destroyed acquired value. Acquired books routinely churn several points post-close, which erodes the revenue side of the deal model. Separate merger-caused churn from background churn with cohort comparisons, and watch revenue concentration in the leavers. Read with NPS trends in acquired accounts and synergy realization on the revenue side.

## Formula

```
Customers Lost in Year One / Customers at Close
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** retention
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1699 (batch 6)
