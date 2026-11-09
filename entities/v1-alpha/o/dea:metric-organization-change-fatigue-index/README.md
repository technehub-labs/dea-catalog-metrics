# dea:metric-organization-change-fatigue-index

Candidate Performance Metric record for **Organization Change Fatigue Index** (OCFI-OM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-organization-change-fatigue-index`
- **Name:** Organization Change Fatigue Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OCFI-OM

## 2. Definition

Organization Change Fatigue Index (OCFI-OM) captures exposure to adverse outcomes for organizations tracking operating model monitoring & design effectiveness. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Concurrent Major Changes per Unit, expressed in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
OCFI-OM = Concurrent Major Changes per Unit
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_monitoring_design_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3130 (batch 7)
