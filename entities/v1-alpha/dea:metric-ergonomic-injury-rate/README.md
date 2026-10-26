# dea:metric-ergonomic-injury-rate

Candidate Performance Metric record for **Ergonomic Injury Rate** (EIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ergonomic-injury-rate`
- **Name:** Ergonomic Injury Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EIR

## 2. Definition

Ergonomic Injury Rate (EIR) addresses exposure to adverse outcomes and is a fixture of health & safety reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Ergonomic-Related Injuries / Total Injuries, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures musculoskeletal injuries per worker or hours worked, often from repetitive or manual handling. It matters because ergonomic injuries are among the costliest and most preventable workplace injuries. Under-reporting is common when early symptoms are discouraged from formal logging. Read with Absence Rate and workers compensation claim trends to catch suppressed reporting before it becomes severe.

## Formula

```
Ergonomic-Related Injuries / Total Injuries
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** health_safety

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 404 (batch 1)
