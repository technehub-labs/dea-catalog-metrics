# dea:metric-repeat-contact-rate

Candidate Performance Metric record for **Repeat Contact Rate** (RCR-CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-repeat-contact-rate`
- **Name:** Repeat Contact Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCR-CC

## 2. Definition

Within Contact Center, Repeat Contact Rate (RCR-CC) is used to gauge the quality of outputs and outcomes. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Contacts Requiring More than One Interaction / Total Contact Reasons, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of customers contacting again about the same issue within a window. It matters because repeat contacts expose failed resolutions and multiply cost. Agents can suppress it by closing tickets before confirming the customer is satisfied. Read with First Contact Resolution and Customer Effort Score to confirm fewer repeats mean better outcomes, not discouraged customers.

## Formula

```
RCR-CC = Contacts Requiring More than One Interaction / Total Contact Reasons
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 570 (batch 2)
