# dea:metric-supply-plan-attainment

Candidate Performance Metric record for **Supply Plan Attainment** (SPA-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supply-plan-attainment`
- **Name:** Supply Plan Attainment
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SPA-S

## 2. Definition

Supply Plan Attainment (SPA-S) captures conformance to standards, plans, or obligations for organizations tracking sales & operations planning. Its calculation is Volume Supplied per Plan / Volume Planned, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how well executed supply matched the agreed S&OP supply plan. It matters because broken supply plans convert into expedites and stockouts. Plans can be revised mid-period to match actuals, laundering attainment. Read with Production Plan Attainment and Schedule Adherence to confirm attainment is measured against the original plan.

## Formula

```
Volume Supplied per Plan / Volume Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales_operations_planning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1291 (batch 5)
