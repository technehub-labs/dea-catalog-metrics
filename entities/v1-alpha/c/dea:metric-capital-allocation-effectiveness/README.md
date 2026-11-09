# dea:metric-capital-allocation-effectiveness

Candidate Performance Metric record for **Capital Allocation Effectiveness** (CAE2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capital-allocation-effectiveness`
- **Name:** Capital Allocation Effectiveness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CAE2

## 2. Definition

Within Strategy & Portfolio, Capital Allocation Effectiveness (CAE2) is used to gauge the economic value created or preserved. It is computed as Returns from New Investments / Cost of Capital, expressed in ratio (x:1 or x). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

A composite judgment of whether capital flows to its highest-value uses - measured by tracking where capital actually went against the value delivered, and conventionally assessed through reallocation rate (the share of capital that moves between units over time) and the return spread of reallocated versus steady-state capital. The research tradition behind it (McKinsey's longitudinal work) found that companies reallocating more capital across units early in a disruption outperformed peers - the empirical case that allocation speed, not just allocation choice, drives value. The strategic diagnostic is stickiness: capital that has not moved across units in years indicates budgets are entitlements, and the annual process is a negotiation over increments rather than an allocation. Read with the portfolio balance ratio, since both describe whether capital follows strategy or history.

## Formula

```
CAE2 = Returns from New Investments / Cost of Capital
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** strategy_portfolio

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 373 (batch 1)
