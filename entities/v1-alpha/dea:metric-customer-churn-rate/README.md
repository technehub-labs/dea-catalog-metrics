# dea:metric-customer-churn-rate

Candidate Performance Metric record for **Customer Churn Rate** (CCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-churn-rate`
- **Name:** Customer Churn Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCR

## 2. Definition

Customer Churn Rate (CCR) addresses exposure to adverse outcomes and is a fixture of customer reporting. It is computed as Customers Lost during Period / Customers at Start, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The share of customers lost over a period - the decay constant of any subscription business, and the number that converts directly into average customer lifetime (one over the churn rate). A few points of churn difference is what separates a company that compounds from one that treads water: acquiring customers to replace leavers is the treadmill, and gross-adds minus churn is the only real growth. Read the decomposition before acting: downgrading customers are not gone, involuntary churn from failed payments often looks like quiet quitting, and logo churn versus revenue churn diverge when big customers stay and small ones leave. Churn measured over too short a window with cohort mix noise produces trends that are actually seasonality.

## Formula

```
Customers Lost during Period / Customers at Start
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 70 (batch 1)
