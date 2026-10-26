# dea:metric-driver-based-planning-coverage

Candidate Performance Metric record for **Driver-Based Planning Coverage** (DBPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-driver-based-planning-coverage`
- **Name:** Driver-Based Planning Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DBPC

## 2. Definition

Driver-Based Planning Coverage (DBPC) captures how efficiently resources are converted into outputs for organizations tracking financial planning & analysis. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Plan Lines Built from Documented Drivers / Plan Lines, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how much of the plan is built from operational drivers rather than last year plus growth. Driver-based plans explain themselves and re-forecast quickly when drivers move. Coverage measured by spreadsheet sophistication rather than genuine driver linkage is nominal. Read with scenario analysis coverage and forecast accuracy (Revenue).

## Formula

```
DBPC = Plan Lines Built from Documented Drivers / Plan Lines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** financial_planning_analysis

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3778 (batch 8)
