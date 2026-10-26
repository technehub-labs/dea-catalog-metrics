# dea:metric-cac-payback-period-unit-economics

Candidate Performance Metric record for **CAC Payback Period (Unit Economics)** (CACPPD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cac-payback-period-unit-economics`
- **Name:** CAC Payback Period (Unit Economics)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CACPPD

## 2. Definition

Within Unit Economics & Growth (Deep Dive), CAC Payback Period (Unit Economics) (CACPPD) is used to gauge how efficiently resources are converted into outputs. It is computed as CAC / Monthly Contribution Margin per Customer, expressed in months. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## 3. Context

Measures months for a customer's contribution to repay acquisition cost. Payback converts the LTV/CAC theory into a cash-timing constraint. Payback computed on gross margin rather than contribution margin understates. Read with LTV-to-CAC ratio (Deep Dive) and blended gross margin (Deep Dive).

## Formula

```
CAC / Monthly Contribution Margin per Customer
```

## Unit

- **Unit reference:** `dea:unit-month`
- **Unit:** month
- **Unit label (as published):** months

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4158 (batch 9)
