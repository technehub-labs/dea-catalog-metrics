# dea:metric-net-promoter-score-contact-center

Candidate Performance Metric record for **Net Promoter Score (Contact Center)** (NPS-CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-promoter-score-contact-center`
- **Name:** Net Promoter Score (Contact Center)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NPS-CC

## 2. Definition

Net Promoter Score (Contact Center) (NPS-CC) captures the engagement or satisfaction of the people involved for organizations tracking contact center. Its calculation is % Promoters - % Detractors among Contact Center Customers, measured in score (points). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The recommend metric measured on contact-center interactions - the transactional NPS variant that asks the question immediately after a support or service call, and thereby measures the service event rather than the brand relationship. Its strategic significance is the service-recovery economics it exposes: response quality in a moment of need predicts loyalty movement more strongly than almost any other touchpoint, and a contact-center NPS that trails the brand NPS identifies the service experience as value destruction. The operational value is driver-level analysis: verbatim comments and reason codes attach to specific queues, scripts, and resolution types, which converts the score into a routing, training, and escalation agenda. Read with first-contact resolution: resolution quality and effort drive the score far more than speed past a threshold, and centers that chase the score with callbacks and politeness while leaving problems unresolved improve the metric and worsen the churn.

## Formula

```
NPS-CC = % Promoters - % Detractors among Contact Center Customers
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 577 (batch 2)
