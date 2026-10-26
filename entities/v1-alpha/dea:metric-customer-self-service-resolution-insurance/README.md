# dea:metric-customer-self-service-resolution-insurance

Candidate Performance Metric record for **Customer Self-Service Resolution (Insurance)** (CSSRI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-self-service-resolution-insurance`
- **Name:** Customer Self-Service Resolution (Insurance)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CSSRI

## 2. Definition

A Insurance Distribution - Direct & Digital indicator, Customer Self-Service Resolution (Insurance) (CSSRI) quantifies how efficiently resources are converted into outputs. Its calculation is Self-Service Resolutions / Service Requests, measured in percent (%). It originates from and is most used in Insurance practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of service requests (policy changes, documents, billing queries) resolved by customers digitally without contact center involvement. It is the cost-side payoff of digital insurance, and it pairs with retention: self-service that resolves quickly improves both economics and satisfaction, while self-service that dead-ends drives more expensive escalations than the original call. Read with containment-versus-escalation rates and satisfaction by resolution path.

## Formula

```
Self-Service Resolutions / Service Requests
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_direct_digital
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2214 (batch 6)
