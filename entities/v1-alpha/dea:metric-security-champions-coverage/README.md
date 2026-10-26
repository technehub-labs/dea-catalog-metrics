# dea:metric-security-champions-coverage

Candidate Performance Metric record for **Security Champions Coverage** (SECCO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-champions-coverage`
- **Name:** Security Champions Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SECCO

## 2. Definition

Security Champions Coverage (SECCO) addresses capability maturity or development and is a fixture of application security (appsec) reporting. It is computed as Teams with Designated Security Champion / Teams, expressed in percent (%). Its use is concentrated in Software. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the proportion of delivery teams with an embedded security advocate. Champions embed security judgment where code is written. Presence without allocated time produces nominal coverage. Read with security champion coverage per team and shift-left security scan coverage.

## Formula

```
Teams with Designated Security Champion / Teams
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** application_security_appsec
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3328 (batch 7)
