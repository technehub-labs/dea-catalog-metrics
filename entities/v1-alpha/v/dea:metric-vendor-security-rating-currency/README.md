# dea:metric-vendor-security-rating-currency

Candidate Performance Metric record for **Vendor Security Rating Currency** (VSRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vendor-security-rating-currency`
- **Name:** Vendor Security Rating Currency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VSRC

## 2. Definition

Vendor Security Rating Currency (VSRC) addresses exposure to adverse outcomes and is a fixture of third-party risk management reporting. It is defined as Ratings Refreshed within Cycle / Rated Vendors; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
VSRC = Ratings Refreshed within Cycle / Rated Vendors
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** third_party_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3719 (batch 8)
