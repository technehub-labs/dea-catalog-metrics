# dea:metric-revenue-per-available-unit-yield-management

Candidate Performance Metric record for **Revenue per Available Unit (Yield Management)** (RevPAU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-available-unit-yield-management`
- **Name:** Revenue per Available Unit (Yield Management)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RevPAU

## 2. Definition

Revenue per Available Unit (Yield Management) (RevPAU) addresses the economic value created or preserved and is a fixture of pricing & revenue management reporting. Its calculation is Revenue / Available Units per Period, measured in currency per unit. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Revenue per available unit is the yield-management master metric - total revenue divided by capacity available to sell - and it is the calculation that transformed industries where fixed capacity meets variable demand (hotels, airlines, rental cars): RevPAR in hospitality and RASK in aviation are both this same construction. Its power is decomposition: RevPAR equals occupancy times average daily rate, so a hotel can grow RevPAR by filling more rooms at lower rates or fewer at higher ones - and the strategy choice matters because each path has different cost and guest-quality implications. Because it prices the asset rather than the transaction, it enables honest comparison across properties with different occupancy patterns. Read with occupancy and ADR separately (the decomposition is the strategy), competitive RevPAR index, and cost structure changes since revenue growth via occupancy raises variable cost while rate growth does not.

## Formula

```
RevPAU = Revenue / Available Units per Period
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1066 (batch 4)
