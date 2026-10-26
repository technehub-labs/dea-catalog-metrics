# dea:metric-revenue-per-employee

Candidate Performance Metric record for **Revenue per Employee** (RPE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-employee`
- **Name:** Revenue per Employee
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RPE

## 2. Definition

A Human Resources indicator, Revenue per Employee (RPE) quantifies the economic value created or preserved. Its calculation is Revenue / Average Headcount, measured in currency value. It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Revenue divided by headcount - the blunt but powerful productivity measure that works because labor is the one input every organization shares. Tech companies run well above half a million dollars per head; consulting and manufacturing run far lower, and both can be excellent, so the level is industry-bound and only the trend and peer gap carry meaning. Strategically it is the cleanest test of scaling: revenue growing faster than headcount means the operating model is compounding, while headcount growing with flat revenue means the company is buying growth with people - a model that eventually collides with margin arithmetic. The metric also disciplines automation decisions: any productivity investment should eventually be visible here, which makes it the scoreboard for the entire transformation portfolio.

## Formula

```
Revenue / Average Headcount
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** organization
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 136 (batch 1)
