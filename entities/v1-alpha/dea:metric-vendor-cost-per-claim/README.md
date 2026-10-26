# dea:metric-vendor-cost-per-claim

Candidate Performance Metric record for **Vendor Cost per Claim** (VCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vendor-cost-per-claim`
- **Name:** Vendor Cost per Claim
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** VCC

## 2. Definition

Vendor Cost per Claim (VCC) captures how efficiently resources are converted into outputs for organizations tracking insurance claims deep dive. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Third-Party Vendor Costs / Claims, expressed in currency value. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Insurance.

## Formula

```
Third-Party Vendor Costs / Claims
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1552 (batch 6)
