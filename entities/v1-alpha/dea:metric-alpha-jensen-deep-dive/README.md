# dea:metric-alpha-jensen-deep-dive

Candidate Performance Metric record for **Alpha (Jensen) (Deep Dive)** (AJDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alpha-jensen-deep-dive`
- **Name:** Alpha (Jensen) (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AJDD

## 2. Definition

Alpha (Jensen) (Deep Dive) (AJDD) measures the economic value created or preserved in the Investment Performance Measurement domain. The formula is Portfolio Return above CAPM-Predicted Return - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Investment management sector.

## 3. Context

Jensen's alpha, from Michael C. Jensen (1968), is the return above what CAPM says the portfolio should earn given its beta - the residual intercept in a market regression. Positive alpha means the manager beat risk-adjusted expectations, the number pension consultants used for decades to grade active skill. Its modern caveats: it is single-factor, so it mistakes factor tilts (size, value, momentum) for skill; and it is sample-dependent. Today it is best used alongside multi-factor attribution rather than alone.

## Formula

```
AJDD = Portfolio Return above CAPM-Predicted Return
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Michael C. Jensen, 1968

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3439 (batch 7)
