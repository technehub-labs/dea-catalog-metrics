# dea:metric-collection-rate-utilities

Candidate Performance Metric record for **Collection Rate (Utilities)** (CLR-U) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-collection-rate-utilities`
- **Name:** Collection Rate (Utilities)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CLR-U

## 2. Definition

Collection Rate (Utilities) (CLR-U) addresses the economic value created or preserved and is a fixture of utilities customer operations reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Revenue Collected / Revenue Billed, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Utilities practice.

## 3. Context

Collection rate measures the share of billed revenue actually collected, and it is the bad-debt metric of a sector with distinctive features: utilities are often legally required to serve customers who cannot pay (winter moratoria on shutoffs), making collections management a social-policy interface as much as a finance function. The receivable dynamics are unusual - regulated tariffs allow bad-debt recovery from ratepayers in many jurisdictions, which weakens the natural incentive to collect aggressively. Arrears aging matters more than the blended rate: payments accumulating across multiple months signal escalating hardship and eventual write-off concentration. Read with arrears aging distribution, disconnection and reconnection rates (as enforcement and social-harm indicators), payment-plan enrollment and completion, and LIHEAP/assistance program capture rates.

## Formula

```
Revenue Collected / Revenue Billed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** utilities_customer_operations
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 965 (batch 3)
