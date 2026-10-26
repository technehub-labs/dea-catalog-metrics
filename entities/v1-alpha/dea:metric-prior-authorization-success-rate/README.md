# dea:metric-prior-authorization-success-rate

Candidate Performance Metric record for **Prior Authorization Success Rate** (PASR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-prior-authorization-success-rate`
- **Name:** Prior Authorization Success Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PASR

## 2. Definition

Prior Authorization Success Rate (PASR) captures how efficiently resources are converted into outputs for organizations tracking healthcare revenue cycle. It is computed as Services Authorized on Request / Services Requiring Authorization, expressed in percent (%). Its use is concentrated in Healthcare. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of prior authorization requests approved by payers. It matters because failed authorizations delay care and drive denials. Success can be raised by avoiding medically complex cases that need authorization. Read with Denial Overturn Rate and Care Delay metrics to confirm access is improving, not being rationed.

## Formula

```
Services Authorized on Request / Services Requiring Authorization
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** healthcare_revenue_cycle
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 879 (batch 3)
