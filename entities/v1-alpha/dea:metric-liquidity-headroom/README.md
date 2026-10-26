# dea:metric-liquidity-headroom

Candidate Performance Metric record for **Liquidity Headroom** (LHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-liquidity-headroom`
- **Name:** Liquidity Headroom
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LHR

## 2. Definition

Liquidity Headroom (LHR) captures exposure to adverse outcomes for organizations tracking treasury & cash management. Its calculation is (Available Liquidity - Projected Outflows) / Projected Outflows, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The surplus of available liquidity - cash plus undrawn committed facilities - over forecast requirements in the stress horizon, the metric that answers the question boards actually ask: how long could we operate if markets closed. Its strategic significance is optionality: headroom is the capacity to act without permission from lenders, and organizations that hold deliberate surplus are buying the right to invest countercyclically, which is where the best acquisitions and talent bargains historically appear. The measurement honesty requirement is conservative: undrawn lines must count only committed amounts (uncommitted facilities vanish exactly when needed), and the requirement side should be a stressed forecast, not the base case - the metric's value is as a bad-day number. Read with the covenant situation: headroom against facility headroom (can the revolver still be drawn if covenants are tight) is the question that separates real liquidity from illusory.

## Formula

```
LHR = (Available Liquidity - Projected Outflows) / Projected Outflows
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 593 (batch 2)
