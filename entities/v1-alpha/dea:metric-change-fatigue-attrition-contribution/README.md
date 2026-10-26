# dea:metric-change-fatigue-attrition-contribution

Candidate Performance Metric record for **Change Fatigue Attrition Contribution** (CFAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-change-fatigue-attrition-contribution`
- **Name:** Change Fatigue Attrition Contribution
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CFAC

## 2. Definition

Change Fatigue Attrition Contribution (CFAC) measures exposure to adverse outcomes in the Change Management domain. Its calculation is Voluntary Exits Citing Change Overload / Voluntary Exits, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Estimates the share of attrition attributable to cumulative change load - too many simultaneous initiatives, unclear priorities, exhaustion. It makes the hidden tax of over-initiated organizations visible in workforce terms. Attribution is genuinely hard: exit coding is blunt and employees rarely name change fatigue directly, so triangulate surveys with attrition clustering around initiative-intensive units. Read with change readiness score and the initiative count per employee.

## Formula

```
Voluntary Exits Citing Change Overload / Voluntary Exits
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** change_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1386 (batch 5)
