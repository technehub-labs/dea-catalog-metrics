# dea:metric-data-lineage-documentation-rate

Candidate Performance Metric record for **Data Lineage Documentation Rate** (DLDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-lineage-documentation-rate`
- **Name:** Data Lineage Documentation Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DLDR

## 2. Definition

Data Lineage Documentation Rate (DLDR) addresses the quality of outputs and outcomes and is a fixture of data governance & stewardship reporting. Its calculation is Critical Elements with End-to-End Lineage / Critical Elements, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how much of the data pipeline has documented lineage from source to consumption. Lineage is what makes impact analysis and issue tracing possible. Lineage generated but unverified against reality drifts into fiction. Read with critical data element governance coverage and data pipeline observability coverage.

## Formula

```
Critical Elements with End-to-End Lineage / Critical Elements
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_governance_stewardship

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3600 (batch 8)
