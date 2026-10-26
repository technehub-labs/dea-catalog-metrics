# dea:metric-schedule-performance-index-programs

Candidate Performance Metric record for **Schedule Performance Index (Programs)** (SPI-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-schedule-performance-index-programs`
- **Name:** Schedule Performance Index (Programs)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SPI-P

## 2. Definition

Schedule Performance Index (Programs) (SPI-P) addresses how efficiently resources are converted into outputs and is a fixture of aerospace & defense program management reporting. Its calculation is EV / PV, measured in ratio (x:1 or x). It originates from and is most used in Aerospace & Defense practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures schedule efficiency through earned value - work performed against work scheduled. SPI deterioration propagates directly to delivery dates and often to cost via resource extension, and like CPI it rarely self-heals in execution. Watch SPI computed against the current baseline, which flattering rebaselines obscure. Read with milestone achievement confidence and critical-path float trends.

## Formula

```
EV / PV
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** aerospace_defense_program_management
- **Sector:** aerospace_defense

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1781 (batch 6)
