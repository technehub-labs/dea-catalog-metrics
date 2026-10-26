# dea:metric-complaint-rate-distribution

Candidate Performance Metric record for **Complaint Rate (Distribution)** (CORD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-complaint-rate-distribution`
- **Name:** Complaint Rate (Distribution)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CORD

## 2. Definition

Complaint Rate (Distribution) (CORD) measures the quality of outputs and outcomes in the Insurance Distribution & Brokerage domain. It is defined as Complaints / 1,000 Policies Serviced; the result is stated in events per thousand or million (scaled). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. In Insurance distribution, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures complaints relative to policies or clients in distribution channels. It matters because complaints are the regulator's window into sales conduct. Complaints can be deterred rather than resolved to shrink the rate. Read with Complaint Root Cause analysis and regulator interaction history to confirm the falling rate reflects conduct improvement.

## Formula

```
Complaints / 1,000 Policies Serviced
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_brokerage
- **Sector:** insurance_distribution

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1163 (batch 4)
