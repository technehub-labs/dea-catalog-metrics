# dea:metric-emergency-assistance-disbursement-time

Candidate Performance Metric record for **Emergency Assistance Disbursement Time** (EADT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emergency-assistance-disbursement-time`
- **Name:** Emergency Assistance Disbursement Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EADT

## 2. Definition

Emergency Assistance Disbursement Time (EADT) addresses how efficiently resources are converted into outputs and is a fixture of public sector & citizen service standard measures (deep dive) reporting. The formula is Days from Eligibility Confirmed to Funds Received - reported in days. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Public sector sector.

## 3. Context

Measures elapsed time from application to funds reaching the person in crisis. In emergency assistance, delay equals harm. Times measured from approval rather than application start hide the queue. Read with crisis fund disbursement time and benefit processing cycle time.

## Formula

```
Days from Eligibility Confirmed to Funds Received
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** public_sector_citizen_service_standard_measures_deep_dive
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4430 (batch 11)
