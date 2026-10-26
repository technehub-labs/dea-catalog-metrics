# dea:metric-weekly-retention-cohort-curve

Candidate Performance Metric record for **Weekly Retention Cohort Curve** (WRCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-weekly-retention-cohort-curve`
- **Name:** Weekly Retention Cohort Curve
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WRCC

## 2. Definition

Weekly Retention Cohort Curve (WRCC) addresses the retention of customers, users, or assets over time and is a fixture of web & digital analytics standard measures reporting. Its calculation is Active Users in Week N / Cohort Size, measured in percent (%). It originates from and is most used in Digital product practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures week-by-week retention of each signup cohort. Cohort curves expose whether engagement stabilizes or decays. Curves dominated by a viral one-off cohort distort the picture. Read with DAU/MAU stickiness ratio and cohort retention curve stability.

## Formula

```
WRCC = Active Users in Week N / Cohort Size
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** web_digital_analytics_standard_measures
- **Sector:** digital_product

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4359 (batch 11)
