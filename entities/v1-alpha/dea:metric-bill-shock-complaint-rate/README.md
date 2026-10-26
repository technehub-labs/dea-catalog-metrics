# dea:metric-bill-shock-complaint-rate

Candidate Performance Metric record for **Bill Shock Complaint Rate** (BSCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bill-shock-complaint-rate`
- **Name:** Bill Shock Complaint Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BSCR

## 2. Definition

Bill Shock Complaint Rate (BSCR) addresses exposure to adverse outcomes and is a fixture of telecom customer experience & billing reporting. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Bill Shock Complaints / Customers x 1,000; the result is stated in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. In Telecommunications, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures complaints about unexpectedly high bills. It matters because bill shock is a top churn driver and regulator concern in telecom. Usage alerts can be technically sent while remaining hard to understand. Read with First Bill Right Rate and Churn Rate among complainers to confirm shock reduction is customer-felt.

## Formula

```
Bill Shock Complaints / Customers x 1,000
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** telecom_customer_experience_billing
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1275 (batch 5)
