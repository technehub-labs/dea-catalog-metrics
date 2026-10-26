# dea:metric-customs-data-error-rate

Candidate Performance Metric record for **Customs Data Error Rate** (CDER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customs-data-error-rate`
- **Name:** Customs Data Error Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CDER

## 2. Definition

Customs Data Error Rate (CDER) captures the quality of outputs and outcomes for organizations tracking international trade & customs. It is defined as Entry Data Errors Found / Entry Lines; the result is stated in events per thousand or million (scaled). In Logistics & Trade, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Entry Data Errors Found / Entry Lines
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** international_trade_customs
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1723 (batch 6)
