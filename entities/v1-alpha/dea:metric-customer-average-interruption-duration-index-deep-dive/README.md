# dea:metric-customer-average-interruption-duration-index-deep-dive

Candidate Performance Metric record for **Customer Average Interruption Duration Index (Deep Dive)** (CAIDI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-average-interruption-duration-index-deep-dive`
- **Name:** Customer Average Interruption Duration Index (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CAIDI

## 2. Definition

Customer Average Interruption Duration Index (Deep Dive) (CAIDI) captures the quality of outputs and outcomes for organizations tracking utilities field operations & grid. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is SAIDI / SAIFI, measured in minutes. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Utilities practice.

## 3. Context

CAIDI, from IEEE Std 1366, is SAIDI divided by SAIFI - the average duration of an interruption, in minutes, experienced by customers who actually had one. It isolates restoration performance from outage frequency, which makes it the utility's crew-response KPI. Note the subtlety: improving the number by restoring some customers quickly can appear while overall reliability worsens; always read the trio SAIDI, SAIFI, CAIDI together.

## Formula

```
SAIDI / SAIFI
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** IEEE Std 1366 reliability indices

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1884 (batch 6)
