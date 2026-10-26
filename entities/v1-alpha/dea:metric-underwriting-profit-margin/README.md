# dea:metric-underwriting-profit-margin

Candidate Performance Metric record for **Underwriting Profit Margin** (UPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-underwriting-profit-margin`
- **Name:** Underwriting Profit Margin
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** UPM

## 2. Definition

Underwriting Profit Margin (UPM) addresses the economic value created or preserved and is a fixture of insurance reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as (Earned Premiums - Incurred Losses - Underwriting Expenses) / Earned Premiums, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Insurance.

## 3. Context

Premium minus claims minus expenses, as a share of premium - the margin the underwriting itself earns before any investment income, the number that answers whether the insurer is a risk-manager or merely a float-borrower. When it is positive, the insurer is paid to hold the float; when negative, it pays for the privilege and must out-earn the shortfall in investment returns - a strategy that works until rates fall. The strategic use is cycle reading: markets that compete margins below zero in soft years and rebuild in hard years reveal whether management is compounding capital or chasing volume. It is the combined ratio viewed as a margin, and the two tell the same story with different arithmetic.

## Formula

```
(Earned Premiums - Incurred Losses - Underwriting Expenses) / Earned Premiums
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 64 (batch 1)
