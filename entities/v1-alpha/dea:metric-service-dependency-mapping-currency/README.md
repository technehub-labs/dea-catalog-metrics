# dea:metric-service-dependency-mapping-currency

Candidate Performance Metric record for **Service Dependency Mapping Currency** (SDMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-dependency-mapping-currency`
- **Name:** Service Dependency Mapping Currency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SDMC

## 2. Definition

Service Dependency Mapping Currency (SDMC) addresses the quality of outputs and outcomes and is a fixture of sre & observability standard measures reporting. Its calculation is Dependencies Verified in Last Quarter / Mapped Dependencies, measured in percent (%). It originates from and is most used in Software practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether service dependency maps reflect the current architecture. Stale maps send incident response in wrong directions during outages. Currency measured as documentation date rather than verified discovery is nominal. Read with observability coverage and incident detection via monitoring ratio.

## Formula

```
SDMC = Dependencies Verified in Last Quarter / Mapped Dependencies
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4387 (batch 11)
