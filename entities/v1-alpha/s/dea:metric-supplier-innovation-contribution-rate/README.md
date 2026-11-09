# dea:metric-supplier-innovation-contribution-rate

Candidate Performance Metric record for **Supplier Innovation Contribution Rate** (SICR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-innovation-contribution-rate`
- **Name:** Supplier Innovation Contribution Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SICR

## 2. Definition

Supplier Innovation Contribution Rate (SICR) captures the economic value created or preserved for organizations tracking strategic sourcing & supplier performance (deep dive). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Accepted Supplier-Initiated Innovations / Sourcing Cycle, measured in count (items per period). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how much measurable innovation (product, process, cost) suppliers contribute. Suppliers hold capabilities no customer can replicate internally. Contributions counted as ideas submitted rather than implemented value is activity, not innovation. Read with supplier development program yield and supplier-enabled innovation revenue.

## Formula

```
SICR = Accepted Supplier-Initiated Innovations / Sourcing Cycle
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** strategic_sourcing_supplier_performance_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3749 (batch 8)
