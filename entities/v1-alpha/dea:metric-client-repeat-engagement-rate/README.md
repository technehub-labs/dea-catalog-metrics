# dea:metric-client-repeat-engagement-rate

Candidate Performance Metric record for **Client Repeat Engagement Rate** (CRER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-client-repeat-engagement-rate`
- **Name:** Client Repeat Engagement Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CRER

## 2. Definition

A Staffing & Recruiting indicator, Client Repeat Engagement Rate (CRER) quantifies the retention of customers, users, or assets over time. Its calculation is Clients with Repeat Mandates / Clients Served, measured in percent (%). It originates from and is most used in Staffing & recruiting practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Client repeat engagement measures the share of clients returning with subsequent staffing orders, and it is the durable-growth metric that reveals whether an agency delivers quality or just volume - in an industry where anyone can source candidates, repeat business is the market's certification of placement quality. The measurement honesty issue is timeframe and order-type normalization: a client with seasonal hiring needs returns on a different cycle than a client with one annual executive search, so repeat rates need cohort treatment. Repeat engagement also carries forward the retention signal directly: clients do not return when placements quit. Read with placement retention at 90 days (its upstream driver), share of revenue from repeat clients, and order-depth growth within accounts (clients expanding from one role type into many).

## Formula

```
Clients with Repeat Mandates / Clients Served
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** staffing_recruiting
- **Sector:** staffing_recruiting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1029 (batch 3)
