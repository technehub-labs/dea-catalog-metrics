# dea:metric-agency-audit-exception-rate

Candidate Performance Metric record for **Agency Audit Exception Rate** (AAER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-agency-audit-exception-rate`
- **Name:** Agency Audit Exception Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AAER

## 2. Definition

Agency Audit Exception Rate (AAER) addresses conformance to standards, plans, or obligations and is a fixture of insurance distribution & agency management reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Audit Exceptions / Audit Items Reviewed, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Insurance practice.

## Formula

```
Audit Exceptions / Audit Items Reviewed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_agency_management
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1733 (batch 6)
