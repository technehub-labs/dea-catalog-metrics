# dea:metric-revenue-per-strategic-business-unit

Candidate Performance Metric record for **Revenue per Strategic Business Unit** (RPSBU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-strategic-business-unit`
- **Name:** Revenue per Strategic Business Unit
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPSBU

## 2. Definition

Revenue per Strategic Business Unit (RPSBU) addresses the economic value created or preserved and is a fixture of strategy & portfolio reporting. Its calculation is Total Revenue / Number of Business Units, measured in currency value. It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The topline of each business unit - the decomposition metric of the corporate portfolio, which gains strategic meaning only through comparison: against the unit's capital employed, against its growth market, and against its sibling units competing for the same allocation budget. Its use is in the portfolio conversation every corporate center runs: units by revenue share reveal the concentration of the enterprise, and the revenue-versus-capital-consumed map is the first-draft of an allocate-or-divest debate. The definitional care is transfer pricing, since internal flows can materially move unit revenue depending on convention, and any unit revenue compared across time needs the price-quantity split before it means anything. As a standalone number it is inert; paired with profitability and growth, it is the basic unit of corporate strategy arithmetic.

## Formula

```
RPSBU = Total Revenue / Number of Business Units
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 368 (batch 1)
