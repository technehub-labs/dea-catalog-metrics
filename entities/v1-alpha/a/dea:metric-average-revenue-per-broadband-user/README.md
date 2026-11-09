# dea:metric-average-revenue-per-broadband-user

Candidate Performance Metric record for **Average Revenue per Broadband User** (ARPBU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-revenue-per-broadband-user`
- **Name:** Average Revenue per Broadband User
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ARPBU

## 2. Definition

Average Revenue per Broadband User (ARPBU) addresses the economic value created or preserved and is a fixture of telecommunications reporting. It is computed as Broadband Revenue / Broadband Subscribers, expressed in currency per unit. Its use is concentrated in Telecommunications. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Broadband revenue per broadband subscriber - the ARPU refinement for the fixed-access business, and the metric through which the access-layer economics became strategic: as connectivity commoditizes, broadband ARPU is where operators harvest the value of ever-faster infrastructure, through speed-tier pricing that converts capacity investment into revenue. Its strategic significance is the upgrade cycle it measures: households migrate upward through speed tiers over years, and the ARPU trend tracks whether the operator monetizes its fiber build or delivers it as an unpaid social good. Read with penetration and mix: ARPU flat while average delivered speed rises is a price-capture failure, and the gap between speed delivered and revenue per megabit is the metric of infrastructure monetization. In fiber-upgrade programs, this is the number the business case is written on.

## Formula

```
ARPBU = Broadband Revenue / Broadband Subscribers
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecommunications
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 531 (batch 1)
