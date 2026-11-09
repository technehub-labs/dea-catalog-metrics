# dea:metric-advisor-productivity

Candidate Performance Metric record for **Advisor Productivity** (ADPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-advisor-productivity`
- **Name:** Advisor Productivity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ADPR

## 2. Definition

Advisor Productivity (ADPR) measures how efficiently resources are converted into outputs in the Wealth Management domain. It is computed as Revenue per Financial Advisor per Period, expressed in currency value. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Wealth management.

## 3. Context

Advisor productivity measures revenue (and often households served) per advisor, and it is the operating-leverage metric of wealth management - the business is a people business with high compensation costs, so revenue per advisor determines margin structure. Productivity decomposes into client load (how many relationships), average account size (which segments), and service model mix (advisors bogged down in administrative work sell less). The strategic lever is leverage: teaming models and delegate-to-specialist structures let advisors spend more hours on revenue-generating client work. Read with client-per-advisor trend, admin-hour ratio, advisor retention (productivity hollows if top advisors churn), and the tenure-productivity curve since ramp time is real.

## Formula

```
ADPR = Revenue per Financial Advisor per Period
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** wealth_management
- **Sector:** wealth_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1135 (batch 4)
