# dea:metric-environmental-emissions-compliance-chemicals

Candidate Performance Metric record for **Environmental Emissions Compliance (Chemicals)** (EECC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-environmental-emissions-compliance-chemicals`
- **Name:** Environmental Emissions Compliance (Chemicals)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EECC

## 2. Definition

Environmental Emissions Compliance (Chemicals) (EECC) measures conformance to standards, plans, or obligations in the Chemicals & Specialty Materials domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Emission Tests within Permits / Tests, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Chemicals practice.

## 3. Context

Measures conformance with permitted emission limits - air, water, waste - across operating units. Compliance is the license to operate in chemicals, and exceedances trigger escalating enforcement up to shutdown in most jurisdictions. Read excursion patterns, not just pass-fail, since chronic near-limit operation is fragility without violation. Read with continuous monitoring system uptime and permit renewal risk.

## Formula

```
EECC = Emission Tests within Permits / Tests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** chemicals_specialty_materials
- **Sector:** chemicals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1813 (batch 6)
