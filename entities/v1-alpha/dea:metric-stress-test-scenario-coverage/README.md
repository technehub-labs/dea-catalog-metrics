# dea:metric-stress-test-scenario-coverage

Candidate Performance Metric record for **Stress Test Scenario Coverage** (STSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stress-test-scenario-coverage`
- **Name:** Stress Test Scenario Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** STSC

## 2. Definition

Within Investment Risk & Middle Office Operations, Stress Test Scenario Coverage (STSC) is used to gauge conformance to standards, plans, or obligations. It is computed as Mandated Scenarios Executed / Required Scenarios, expressed in percent (%). Its use is concentrated in Investment management. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how completely the risk model portfolio covers the scenarios that could break the fund. Scenario gaps are blind spots by definition. Coverage weighted toward comfortable scenarios is a design choice, not readiness. Read with expected shortfall estimate stability and liquidity coverage ratio (Fund Ops).

## Formula

```
Mandated Scenarios Executed / Required Scenarios
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3460 (batch 7)
