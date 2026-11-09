# dea:metric-workforce-diversity-representation-by-level

Candidate Performance Metric record for **Workforce Diversity Representation by Level** (WDRL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-workforce-diversity-representation-by-level`
- **Name:** Workforce Diversity Representation by Level
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WDRL

## 2. Definition

Workforce Diversity Representation by Level (WDRL) captures conformance to standards, plans, or obligations for organizations tracking diversity, equity & inclusion. Its calculation is Underrepresented Group Members at Level / Total at Level, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the demographic composition of the workforce at each organizational level. Level-cut data is the honest version of diversity reporting: many organizations are diverse at entry and monolithic at leadership, which aggregate ratios hide. Read pipelines rather than snapshots - representation plus hiring, promotion, and exit parity together reveal whether gaps are legacy or actively maintained. Read with promotion parity ratio and leadership diversity representation.

## Formula

```
WDRL = Underrepresented Group Members at Level / Total at Level
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** diversity_equity_inclusion

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1366 (batch 5)
