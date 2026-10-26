# dea:metric-self-service-channel-adoption-utilities

Candidate Performance Metric record for **Self-Service Channel Adoption (Utilities)** (SSA-U) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-self-service-channel-adoption-utilities`
- **Name:** Self-Service Channel Adoption (Utilities)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSA-U

## 2. Definition

Self-Service Channel Adoption (Utilities) (SSA-U) captures how efficiently resources are converted into outputs for organizations tracking utilities customer operations. It is defined as Self-Service Transactions / Total Transactions; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Utilities, it is a recognized element of the standard performance toolkit.

## 3. Context

Self-service channel adoption measures the share of customer interactions handled through digital self-service rather than live agents, and it is the cost-transformation metric of utility customer operations - a live service call costs several dollars while an app or web session costs cents, making adoption the mechanism that funds service-model transformation. The critical honesty test is channel quality: adoption achieved by degrading phone support (long holds, hidden numbers) inflates adoption while pushing frustrated customers through worse experiences, and the counter-metric is containment failure - customers who try self-service and then call anyway. Outage events are the adoption stress test: digital channels must handle surge communication when it matters most. Read with containment rate (self-service resolved without escalation), digital-versus-phone satisfaction scores by interaction type, and adoption by customer age segment.

## Formula

```
Self-Service Transactions / Total Transactions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** utilities_customer_operations
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 962 (batch 3)
