# dea:metric-stage-gate-bypass-rate

Candidate Performance Metric record for **Stage Gate Bypass Rate** (SGBR-PPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stage-gate-bypass-rate`
- **Name:** Stage Gate Bypass Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SGBR-PPM

## 2. Definition

Within Program & Portfolio Management, Stage Gate Bypass Rate (SGBR-PPM) is used to gauge conformance to standards, plans, or obligations. Its calculation is Gates Approved with Exceptions or Waivers / Gates, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of initiatives passing through stage gates with waived requirements. Gates bypassed routinely are gates that exist on paper only. Bypass for genuinely urgent work is occasional; habitual bypass is governance failure. Read with baseline change approval compliance and project governance review compliance.

## Formula

```
Gates Approved with Exceptions or Waivers / Gates
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** program_portfolio_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2971 (batch 7)
