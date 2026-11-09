# dea:metric-daily-active-users

Candidate Performance Metric record for **Daily Active Users** (DAU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-daily-active-users`
- **Name:** Daily Active Users
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DAU

## 2. Definition

Daily Active Users (DAU) captures the engagement or satisfaction of the people involved for organizations tracking product management. Its calculation is Unique Active Users per Day, measured in count (items per period). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The count of unique users engaging with the product in a day - the engagement metric that became the default heartbeat of consumer software, and strategically the number that distinguishes a product people have from a product people use. Its significance is the habit argument: daily frequency implies the product occupies a routine slot, which predicts both retention and monetization far better than registered counts, and the entire advertising model prices daily attention. The definitional battleground is what counts as active - any open, meaningful session, or completing a core action - and the honest choice is the action definition, since open-based DAU rewards notification spam. Read with the cohort split: blended DAU moves with acquisition mix and seasonality, and the cohort-level DAU trend is where genuine engagement change is visible, as is the weekday-weekend pattern that reveals whether the product is a work tool or a leisure one.

## Formula

```
DAU = Unique Active Users per Day
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 550 (batch 1)
