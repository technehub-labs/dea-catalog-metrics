# dea:metric-total-landed-cost

Candidate Performance Metric record for **Total Landed Cost** (TLC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-total-landed-cost`
- **Name:** Total Landed Cost
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TLC

## 2. Definition

Total Landed Cost (TLC) measures the economic value created or preserved in the Supply Chain domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Product Cost + Freight + Duties + Insurance + Handling - reported in currency value. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the full cost of a delivered product including freight, duties, insurance, and handling. It matters because it is the true comparison basis for sourcing decisions, not unit price. Estimates can be gamed by allocating logistics overhead optimistically to favored suppliers. Read with Purchase Price Variance and Freight Cost per Unit to check that low quoted prices survive full landed cost.

## Formula

```
Product Cost + Freight + Duties + Insurance + Handling
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 182 (batch 1)
