# dea:metric-change-order-rate

Candidate Performance Metric record for **Change Order Rate** (COR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-change-order-rate`
- **Name:** Change Order Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** COR-C

## 2. Definition

Change Order Rate (COR-C) captures exposure to adverse outcomes for organizations tracking construction & engineering. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Change Order Value / Original Contract Value, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Construction & engineering.

## 3. Context

Measures the frequency or value of change orders relative to the base contract. It matters because excessive change orders signal poor scoping, estimation, or requirements discipline. Contractors can underbid the base scope, planning to recover margin through change orders. Read with Cost Variance in Construction and Design Change Frequency to distinguish legitimate change from scoping strategy.

## Formula

```
Change Order Value / Original Contract Value
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_engineering
- **Sector:** construction_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 667 (batch 2)
