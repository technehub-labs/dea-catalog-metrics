# dea:metric-gross-operating-profit-per-available-room

Candidate Performance Metric record for **Gross Operating Profit per Available Room** (GOPPAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-operating-profit-per-available-room`
- **Name:** Gross Operating Profit per Available Room
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GOPPAR

## 2. Definition

Gross Operating Profit per Available Room (GOPPAR) captures the economic value created or preserved for organizations tracking hospitality & food service. It is computed as Gross Operating Profit / Rooms Available, expressed in currency value. Its use is concentrated in Hospitality. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Gross operating profit per available room - the metric that extends RevPAR from revenue to profit, answering the question RevPAR cannot: whether the topline was bought at a cost that consumed it. GOPPAR matters because hotels routinely trade occupancy for revenue with costs attached - breakfast packages, distribution commissions, loyalty discounts - and RevPAR growth achieved through those channels can arrive with GOPPAR flat, which the revenue metric would call success. Its strategic significance is the owner's currency: asset valuation and lender analysis conventionally run on profit metrics, so GOPPAR is the number that connects operating decisions to what the hotel is worth. Read with the flow-through rate (the share of incremental revenue that reaches GOP), since flow-through below the typical band signals the revenue was bought with margin.

## Formula

```
GOPPAR = Gross Operating Profit / Rooms Available
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** hospitality_food_service
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 507 (batch 1)
