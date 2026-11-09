# dea:metric-budget-execution-rate-government

Candidate Performance Metric record for **Budget Execution Rate (Government)** (BER-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-budget-execution-rate-government`
- **Name:** Budget Execution Rate (Government)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BER-G

## 2. Definition

Budget Execution Rate (Government) (BER-G) measures conformance to standards, plans, or obligations in the Government & Public Administration domain. Its calculation is Actual Spend / Approved Budget, measured in percent (%). It originates from and is most used in Public Sector practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures actual spending against approved budget within the fiscal period. It is the basic credibility metric of public administration, revealing both underspend (planning or procurement failure) and overspend (control failure). The honest read distinguishes underspend from deliberately unexecutable programs and end-year spending surges that convert budget discipline into waste. Read with program outcome attainment rate, since money moved is not value delivered.

## Formula

```
BER-G = Actual Spend / Approved Budget
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** government_public_administration
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1568 (batch 6)
