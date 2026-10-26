# dea:metric-gross-margin-return-on-inventory

Candidate Performance Metric record for **Gross Margin Return on Inventory** (GMROI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-margin-return-on-inventory`
- **Name:** Gross Margin Return on Inventory
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GMROI

## 2. Definition

Within Retail & E-commerce, Gross Margin Return on Inventory (GMROI) is used to gauge the economic value created or preserved. Its calculation is Gross Margin / Average Inventory Cost, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Retail practice.

## 3. Context

Gross margin dollars returned per dollar of average inventory investment - the retail metric that fuses profitability and velocity into one return number, answering the investor's question about merchandise: how much margin does each inventory dollar generate while it sits. Its strategic significance is the capital lens on merchandising: two assortments with identical margins and identical inventory levels can differ enormously in GMROI if their sell-through speeds differ, and the metric makes slow, capital-hogging categories visible in a way margin percentage never does. Category management runs on it: GMROI by category, class, and vendor is the standard assortment-review table, and decisions to expand or kill a category are argued in these terms. Read with turn and margin separately, since the composite cannot say which lever moved, and the remediation differs completely.

## Formula

```
GMROI = Gross Margin / Average Inventory Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 491 (batch 1)
