# dea:metric-data-catalog-coverage

Candidate Performance Metric record for **Data Catalog Coverage** (DCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-catalog-coverage`
- **Name:** Data Catalog Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DCC

## 2. Definition

Data Catalog Coverage (DCC) addresses capability maturity or development and is a fixture of data management & analytics reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Documented Datasets / Total Datasets, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of data assets documented and discoverable in the catalog. It matters because undocumented data is effectively unusable and untrustworthy for new consumers. Coverage can be inflated with auto-generated stubs that have no real context or ownership. Read with Analytics Adoption Rate and Data Quality issue rates to confirm cataloged assets are actually trusted and used.

## Formula

```
Documented Datasets / Total Datasets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** data_management_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 347 (batch 1)
