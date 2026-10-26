# dea:metric-dispute-rate-billing

Candidate Performance Metric record for **Dispute Rate (Billing)** (DRB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dispute-rate-billing`
- **Name:** Dispute Rate (Billing)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DRB

## 2. Definition

Dispute Rate (Billing) (DRB) measures exposure to adverse outcomes in the Telecom Customer Experience & Billing domain. It is computed as Disputed Charges / Total Billed Amount Events, expressed in percent (%). Its use is concentrated in Telecommunications. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures billing disputes per account or invoice in telecom. It matters because disputes signal billing complexity and drive churn through frustration. Dispute channels can be made difficult, suppressing the numerator. Read with First Bill Right Rate and churn-attributable-to-billing data to confirm disputes are resolved, not deterred.

## Formula

```
Disputed Charges / Total Billed Amount Events
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** telecom_customer_experience_billing
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1267 (batch 5)
