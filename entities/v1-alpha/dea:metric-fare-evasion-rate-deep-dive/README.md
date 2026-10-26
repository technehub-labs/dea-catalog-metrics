# dea:metric-fare-evasion-rate-deep-dive

Candidate Performance Metric record for **Fare Evasion Rate (Deep Dive)** (FER-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fare-evasion-rate-deep-dive`
- **Name:** Fare Evasion Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FER-D

## 2. Definition

Within Public Transit (Deep Dive), Fare Evasion Rate (Deep Dive) (FER-D) is used to gauge the economic value created or preserved. It is computed as Unpaid Journeys / Total Journeys, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Public Transit.

## 3. Context

Measures uncollected rides against total ridership, usually via survey and inspection sampling. It is the revenue-integrity metric of fare systems, and it carries a fairness dimension: evasion tolerated unevenly erodes both revenue and paying-rider trust. Estimation methodology (inspectors concentrate where evasion is high) biases rates, so sampling design determines credibility. Read with fare-inspection coverage and barrier or proof-of-payment design changes.

## Formula

```
Unpaid Journeys / Total Journeys
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit_deep_dive
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2418 (batch 6)
