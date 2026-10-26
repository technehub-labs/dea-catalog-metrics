# dea:metric-counterparty-exposure-concentration

Candidate Performance Metric record for **Counterparty Exposure Concentration** (CPEC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-counterparty-exposure-concentration`
- **Name:** Counterparty Exposure Concentration
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPEC

## 2. Definition

Counterparty Exposure Concentration (CPEC) captures exposure to adverse outcomes for organizations tracking investment risk & middle office operations. It is computed as Largest Counterparty Exposure / Total Exposure, expressed in percent (%). Its use is concentrated in Investment management. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how much exposure rests with any single counterparty or small group. Concentration converts counterparty default from diversifiable to existential. Exposure netted optimistically against collateral overstates safety. Read with counterparty credit rating distribution and risk concentration index.

## Formula

```
Largest Counterparty Exposure / Total Exposure
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3466 (batch 7)
