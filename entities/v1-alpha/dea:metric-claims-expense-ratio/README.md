# dea:metric-claims-expense-ratio

Candidate Performance Metric record for **Claims Expense Ratio** (CER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claims-expense-ratio`
- **Name:** Claims Expense Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CER

## 2. Definition

Within Insurance Claims Deep Dive, Claims Expense Ratio (CER) is used to gauge how efficiently resources are converted into outputs. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Claims Handling Expenses / Earned Premium, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Insurance.

## 3. Context

Measures loss adjustment expense against earned premium or claims volume. Claims expense is the controllable half of the combined ratio equation, and it balloons through outsourced adjusters, litigation, and legacy processes. Beware ratios improved by deferring spend - unstaffed complex desks reappear as leakage and cycle time later. Read with claims cycle time (Deep Dive) and LAE per claim by complexity band.

## Formula

```
CER = Claims Handling Expenses / Earned Premium
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1561 (batch 6)
