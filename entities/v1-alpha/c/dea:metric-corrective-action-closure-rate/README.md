# dea:metric-corrective-action-closure-rate

Candidate Performance Metric record for **Corrective Action Closure Rate** (CACR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-corrective-action-closure-rate`
- **Name:** Corrective Action Closure Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CACR

## 2. Definition

Corrective Action Closure Rate (CACR) measures conformance to standards, plans, or obligations in the Health & Safety domain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Safety Corrective Actions Closed on Time / Actions Opened, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of safety corrective actions closed within target time. It matters because open actions are unmitigated hazards with a known address. Closures can be administratively completed while the physical fix is unfinished. Read with Near Miss Reporting Rate and Recordable Incident Rate to confirm closure pace tracks real hazard reduction.

## Formula

```
CACR = Safety Corrective Actions Closed on Time / Actions Opened
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** health_safety

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 407 (batch 1)
