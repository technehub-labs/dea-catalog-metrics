# dea:metric-cost-to-serve-per-customer-deep-dive

Candidate Performance Metric record for **Cost to Serve per Customer (Deep Dive)** (CTSCD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-to-serve-per-customer-deep-dive`
- **Name:** Cost to Serve per Customer (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CTSCD

## 2. Definition

Within Unit Economics & Growth (Deep Dive), Cost to Serve per Customer (Deep Dive) (CTSCD) is used to gauge how efficiently resources are converted into outputs. Its calculation is Service and Support Cost / Customers, measured in currency per unit. It originates from and is most used in Software practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the full ongoing cost of supporting each customer. Cost-to-serve determines which customers the growth engine actually profits from. Costs allocated at the average hide the expensive tail. Read with customer profitability segmentation index and blended gross margin (Deep Dive).

## Formula

```
CTSCD = Service and Support Cost / Customers
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4173 (batch 9)
