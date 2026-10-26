# dea:metric-complaints-per-1-000-customers-utilities

Candidate Performance Metric record for **Complaints per 1,000 Customers (Utilities)** (CPCU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-complaints-per-1-000-customers-utilities`
- **Name:** Complaints per 1,000 Customers (Utilities)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPCU

## 2. Definition

Complaints per 1,000 Customers (Utilities) (CPCU) measures the quality of outputs and outcomes in the Utilities Customer Operations domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Complaints / Customers x 1,000, expressed in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Utilities.

## 3. Context

Complaints per 1,000 customers measures complaint volume against customer base, and it is the utility sector's regulated service-quality metric - regulators in many jurisdictions track and benchmark it, and utilities defend themselves against rate-case criticism using it. The metric's structural challenge is that utilities provide an essential service with no exit option, so complaint rates reflect frustration without market consequences, meaning satisfaction scores understate dissatisfaction relative to competitive industries. Complaints concentrate in specific triggers: billing errors, outage communication during storms, and estimated-read billing. Read with complaint resolution timeliness, repeat-complaint rate (the true dissatisfaction signal), complaint rate by customer segment and channel, and regulator complaint escalation counts as the public-facing version.

## Formula

```
Complaints / Customers x 1,000
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** utilities_customer_operations
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 959 (batch 3)
