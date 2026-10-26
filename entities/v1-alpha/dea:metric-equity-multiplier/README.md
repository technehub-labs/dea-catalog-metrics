# dea:metric-equity-multiplier

Candidate Performance Metric record for **Equity Multiplier** (EQMUL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-equity-multiplier`
- **Name:** Equity Multiplier
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EQMUL

## 2. Definition

Equity Multiplier (EQMUL) addresses exposure to adverse outcomes and is a fixture of financial statement analysis ratios (deep dive) reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Total Assets / Total Equity; the result is stated in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures total assets per unit of equity, exposing leverage in DuPont-style decomposition. The multiplier is the leverage term that explains ROE decomposition. High multipliers show ROE built on debt rather than performance. Read with return on equity (Deep Dive) and debt-to-equity ratio (Deep Dive).

## Formula

```
Total Assets / Total Equity
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** financial_statement_analysis_ratios_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4022 (batch 9)
