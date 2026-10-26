# dea:metric-liquidity-buffer-compliance

Candidate Performance Metric record for **Liquidity Buffer Compliance** (LBC-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-liquidity-buffer-compliance`
- **Name:** Liquidity Buffer Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LBC-T

## 2. Definition

Liquidity Buffer Compliance (LBC-T) captures exposure to adverse outcomes for organizations tracking corporate treasury (deep dive). Its calculation is Days Buffer Meets Policy / Days in Period, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures whether liquid asset buffers meet policy minimums (coverage days, ratios) at all times. Buffers are the survival metric of corporate finance: compliance breaches during stress are how survivable downturns become insolvencies, so test against stressed outflow scenarios, not steady state. Buffer composition matters - level two assets convert with haircuts precisely when needed. Read with committed facility availability and covenant headroom.

## Formula

```
Days Buffer Meets Policy / Days in Period
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_treasury_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2188 (batch 6)
