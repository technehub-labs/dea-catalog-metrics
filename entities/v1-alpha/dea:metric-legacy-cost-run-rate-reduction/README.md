# dea:metric-legacy-cost-run-rate-reduction

Candidate Performance Metric record for **Legacy Cost Run-Rate Reduction** (LCRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-legacy-cost-run-rate-reduction`
- **Name:** Legacy Cost Run-Rate Reduction
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LCRR

## 2. Definition

Legacy Cost Run-Rate Reduction (LCRR) addresses the economic value created or preserved and is a fixture of digital transformation reporting. Its calculation is (Legacy Cost_prior - Legacy Cost_current) / Legacy Cost_prior, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the sustained reduction in run-rate cost of legacy systems, infrastructure, and processes, the proof that migration is paying for itself. It matters because transformations are funded on the promise of this curve, and it often arrives slower than planned as parallel running lingers. Guard against savings from deferred maintenance being booked as reduction, and against cost that moved to a different budget line rather than disappearing. Read with legacy system migration progress and total IT cost trend.

## Formula

```
(Legacy Cost_prior - Legacy Cost_current) / Legacy Cost_prior
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** digital_transformation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1321 (batch 5)
