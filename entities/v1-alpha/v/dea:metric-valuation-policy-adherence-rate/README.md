# dea:metric-valuation-policy-adherence-rate

Candidate Performance Metric record for **Valuation Policy Adherence Rate** (VPAR-IM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-valuation-policy-adherence-rate`
- **Name:** Valuation Policy Adherence Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VPAR-IM

## 2. Definition

Within Investment Management - Portfolio Operations, Valuation Policy Adherence Rate (VPAR-IM) is used to gauge conformance to standards, plans, or obligations. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Valuations per Approved Methodology / Valuations, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Financial Services.

## 3. Context

Measures compliance with the fund's valuation policy, including pricing sources, frequency, and committee oversight. Valuation is where private markets performance becomes subjective; policy discipline is the control. Adherence measured as sign-off presence rather than independent price verification is weak. Read with NAV calculation accuracy rate and TVPI.

## Formula

```
VPAR-IM = Valuations per Approved Methodology / Valuations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3028 (batch 7)
