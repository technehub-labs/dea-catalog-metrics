# dea:metric-average-revenue-per-user

Candidate Performance Metric record for **Average Revenue per User** (ARPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-revenue-per-user`
- **Name:** Average Revenue per User
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ARPU

## 2. Definition

Average Revenue per User (ARPU) addresses the economic value created or preserved and is a fixture of banking & financial services reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Total Revenue / Average Active Users, measured in currency per unit. Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Financial services practice.

## 3. Context

Total revenue over the average user base - the canonical unit-economics lens for subscription and telecom businesses, where aggregate growth can mask the fact that each customer is worth less every year. Strategic attention falls on the decomposition: ARPU rises either because customers buy more (good), because prices rose and churn has not yet caught up (temporary), or because the mix shifted to premium segments (structural). Its dark companion is that ARPU can be maximized by shedding low-value customers, which helps the metric and shrinks the network - telecom operators manage this tension explicitly. Read with churn: ARPU times gross margin over churn rate is the per-user lifetime value that the whole subscription valuation rests on.

## Formula

```
Total Revenue / Average Active Users
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** banking_financial_services
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 52 (batch 1)
