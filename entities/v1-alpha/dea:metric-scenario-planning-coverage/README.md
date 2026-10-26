# dea:metric-scenario-planning-coverage

Candidate Performance Metric record for **Scenario Planning Coverage** (SPC-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-scenario-planning-coverage`
- **Name:** Scenario Planning Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SPC-S

## 2. Definition

Scenario Planning Coverage (SPC-S) measures capability maturity or development in the Sales & Operations Planning domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Plans with Documented Demand Scenarios / Plans - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of material demand or supply uncertainties with modeled scenarios. It matters because S&OP value comes from rehearsed responses, not just accurate numbers. Coverage can be claimed with trivial scenarios that are never used in decisions. Read with Capacity Decision Cycle Time and demand-signal response speed to confirm scenarios inform real choices.

## Formula

```
Plans with Documented Demand Scenarios / Plans
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capability
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1298 (batch 5)
