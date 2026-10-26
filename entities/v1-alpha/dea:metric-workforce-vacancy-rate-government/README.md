# dea:metric-workforce-vacancy-rate-government

Candidate Performance Metric record for **Workforce Vacancy Rate (Government)** (WVR-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-workforce-vacancy-rate-government`
- **Name:** Workforce Vacancy Rate (Government)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WVR-G

## 2. Definition

Workforce Vacancy Rate (Government) (WVR-G) captures the utilization or availability of capacity for organizations tracking government & public administration. Its calculation is Unfilled Positions / Funded Positions, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Public Sector practice.

## 3. Context

Measures unfilled positions against authorized establishment. Public-sector vacancies concentrate in the operational front line and specialized roles, directly degrading service delivery and overloading remaining staff. Long posting and clearance cycles make the rate partially structural, so pair with time-to-fill and critical-role cuts. Read with case backlog ratio (Government) and overtime spend as compensating signals.

## Formula

```
Unfilled Positions / Funded Positions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** government_public_administration
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1579 (batch 6)
