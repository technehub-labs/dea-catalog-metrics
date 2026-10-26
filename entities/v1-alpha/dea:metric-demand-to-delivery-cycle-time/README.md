# dea:metric-demand-to-delivery-cycle-time

Candidate Performance Metric record for **Demand-to-Delivery Cycle Time** (DDCT-PPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-demand-to-delivery-cycle-time`
- **Name:** Demand-to-Delivery Cycle Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DDCT-PPM

## 2. Definition

Demand-to-Delivery Cycle Time (DDCT-PPM) addresses how efficiently resources are converted into outputs and is a fixture of program & portfolio management reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Days from Demand Intake to Initiative Start - reported in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures elapsed time from demand intake to delivered capability. Long queue times signal portfolio intake and capacity problems, not just slow projects. Cycle time is the portfolio's lead-time metric and the input for flow analysis. Read with portfolio capacity utilization and time to market.

## Formula

```
Days from Demand Intake to Initiative Start
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** program_portfolio_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2966 (batch 7)
