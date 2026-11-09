# dea:metric-revenue-per-salesperson

Candidate Performance Metric record for **Revenue per Salesperson** (RPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-salesperson`
- **Name:** Revenue per Salesperson
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPS

## 2. Definition

Revenue per Salesperson (RPS) captures how efficiently resources are converted into outputs for organizations tracking sales. It is computed as Total Revenue / Number of Salespeople, expressed in currency value. It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures average bookings or revenue generated per quota-carrying rep. It matters as the core productivity read for sales capacity and cost structure. It can be gamed by keeping only senior territories staffed or by assigning house accounts to a few reps. Read with Quota Attainment and Sales Ramp Time to judge whether productivity is real or a favorable-territory artifact.

## Formula

```
RPS = Total Revenue / Number of Salespeople
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 94 (batch 1)
