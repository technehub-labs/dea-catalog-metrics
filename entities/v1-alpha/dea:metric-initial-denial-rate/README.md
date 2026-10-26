# dea:metric-initial-denial-rate

Candidate Performance Metric record for **Initial Denial Rate** (IDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-initial-denial-rate`
- **Name:** Initial Denial Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IDR

## 2. Definition

Within Healthcare Revenue Cycle, Initial Denial Rate (IDR) is used to gauge exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Claims Denied on First Pass / Claims Submitted, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Healthcare practice.

## 3. Context

Initial denial rate measures the share of claims denied on first adjudication, and it is the payer-quality signal in healthcare revenue cycle - some payer behavior is systematic (denials as a cash-flow strategy for payers who know providers will under-appeal), and denial patterns by payer are strategic knowledge worth maintaining. The response economics matter: a large share of denials are never appealed despite decent overturn rates, which means denial rate without appeal-outcome tracking understates recoverable revenue. Denials also split into prevention-eligible (front-end errors) versus clinical-judgment denials (medical necessity), which need entirely different fixes. Read with denial rate by payer and reason code, overturn rate on appeal, write-off rate on unappealed denials, and payer-specific trend as negotiation leverage.

## Formula

```
Claims Denied on First Pass / Claims Submitted
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** healthcare_revenue_cycle
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 873 (batch 3)
