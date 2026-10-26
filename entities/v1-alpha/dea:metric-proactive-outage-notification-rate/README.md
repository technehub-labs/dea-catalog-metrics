# dea:metric-proactive-outage-notification-rate

Candidate Performance Metric record for **Proactive Outage Notification Rate** (PONR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-proactive-outage-notification-rate`
- **Name:** Proactive Outage Notification Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PONR

## 2. Definition

Proactive Outage Notification Rate (PONR) captures the quality of outputs and outcomes for organizations tracking telecom customer experience & billing. The formula is Outages with Customer Notification before Contact / Outages - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Telecommunications sector.

## 3. Context

Measures the share of outages communicated to customers before they discover them. It matters because proactive notice preserves trust and cuts inbound call cost. Notifications can be sent but late, technically proactive but practically useless. Read with Call Volume during outages and Customer Satisfaction post-outage to confirm notification timing is genuine.

## Formula

```
Outages with Customer Notification before Contact / Outages
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** telecom_customer_experience_billing
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1273 (batch 5)
