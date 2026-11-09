# dea:metric-catalog-adoption-rate

Candidate Performance Metric record for **Catalog Adoption Rate** (CAR-GBS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-catalog-adoption-rate`
- **Name:** Catalog Adoption Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CAR-GBS

## 2. Definition

Within Shared Services & Global Business Services, Catalog Adoption Rate (CAR-GBS) is used to gauge how efficiently resources are converted into outputs. Its calculation is Requests via Service Catalog / Total Requests, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of services consumed via shared service catalogs rather than bespoke requests. It matters because catalog consumption is what makes shared services scalable and measurable. Adoption can be inflated by cataloging trivial services while the valuable work stays bespoke. Read with Service Level Attainment (GBS) and Internal Customer Satisfaction (GBS) to confirm adoption is delivering value.

## Formula

```
CAR-GBS = Requests via Service Catalog / Total Requests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** shared_services_global_business_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1055 (batch 4)
