# dea:metric-service-activation-time

Candidate Performance Metric record for **Service Activation Time** (SAT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-activation-time`
- **Name:** Service Activation Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SAT

## 2. Definition

A Telecommunications indicator, Service Activation Time (SAT) quantifies how efficiently resources are converted into outputs. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Days from Order to Service Activation; the result is stated in days. It should be driven down, since lower readings signal healthier performance. In Telecommunications, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures elapsed time from service order to fully activated telecom service. It matters because activation delay is where competitors steal customers who already chose you. It can be gamed by activating partial service while provisioning continues, or counting from install rather than order. Read with Order to Cash Cycle Time and Provisioning Error Rate to confirm speed coexists with quality.

## Formula

```
Days from Order to Service Activation
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecommunications
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 534 (batch 1)
