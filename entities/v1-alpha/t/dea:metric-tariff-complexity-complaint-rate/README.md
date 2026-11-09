# dea:metric-tariff-complexity-complaint-rate

Candidate Performance Metric record for **Tariff Complexity Complaint Rate** (TCCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tariff-complexity-complaint-rate`
- **Name:** Tariff Complexity Complaint Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TCCR

## 2. Definition

Tariff Complexity Complaint Rate (TCCR) measures the quality of outputs and outcomes in the Telecom Product & Bundle Management domain. The formula is Pricing Complaints / 1,000 Customers - reported in events per thousand or million (scaled). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. It is a standard measure in the Telecommunications sector.

## 3. Context

Measures complaints driven by confusing tariff or bundle structures. It matters because complexity is a churn and regulator-magnet in telecom. Complaint channels can be tuned to miss complexity-specific wording. Read with Dispute Rate (Billing) and Churn Reasons analysis to confirm simplification reduces real harm.

## Formula

```
TCCR = Pricing Complaints / 1,000 Customers
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecom_product_bundle_management
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1444 (batch 5)
