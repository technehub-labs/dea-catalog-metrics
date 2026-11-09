# dea:metric-operating-margin-deep-dive

Candidate Performance Metric record for **Operating Margin (Deep Dive)** (OPMDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-operating-margin-deep-dive`
- **Name:** Operating Margin (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OPMDD

## 2. Definition

Within Financial Statement Analysis Ratios (Deep Dive), Operating Margin (Deep Dive) (OPMDD) is used to gauge the economic value created or preserved. It is computed as Operating Income / Revenue, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures profitability after operating costs but before financing and tax. It isolates the core business from capital-structure and tax noise. Mix shifts between business lines can move the margin without any efficiency change. Read with EBITDA margin (Deep Dive) and operating margin trend (Deep Dive).

## Formula

```
OPMDD = Operating Income / Revenue
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
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** financial_statement_analysis_ratios_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4029 (batch 9)
