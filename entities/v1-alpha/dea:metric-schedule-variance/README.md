# dea:metric-schedule-variance

Candidate Performance Metric record for **Schedule Variance** (SV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-schedule-variance`
- **Name:** Schedule Variance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SV

## 2. Definition

Schedule Variance (SV) addresses conformance to standards, plans, or obligations and is a fixture of project management reporting. It is computed as Earned Value - Planned Value, expressed in currency value. It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

SV is earned value minus planned value - the budgeted worth of the schedule gap between work done and work planned. Negative means behind schedule; the number is expressed in currency, which lets managers compare schedule health across projects of different sizes. SV converges to zero at project end regardless of outcome, so a dying SV late in a project can be an artifact, not recovery; read the trend and the forecast, not just the point value.

## Formula

```
Earned Value - Planned Value
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** transformation
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management

## Attribution

- **Source credit:** Earned Value Management (DoD/NASA tradition)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 350 (batch 1)
