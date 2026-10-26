# dea:metric-voice-of-customer-closed-loop-rate

Candidate Performance Metric record for **Voice of Customer Closed-Loop Rate** (VoCCL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-voice-of-customer-closed-loop-rate`
- **Name:** Voice of Customer Closed-Loop Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** VoCCL

## 2. Definition

Voice of Customer Closed-Loop Rate (VoCCL) measures the engagement or satisfaction of the people involved in the Customer Journey & Experience domain. It is computed as Survey Follow-ups Closed with Customer / Negative Surveys, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of customer feedback items formally closed with the customer informed of the response. It matters because feedback loops only improve loyalty when customers see action. Closure can be administrative acknowledgement without genuine resolution. Read with Repeat Feedback on the same theme and Customer Satisfaction trend to confirm loops close in substance.

## Formula

```
Survey Follow-ups Closed with Customer / Negative Surveys
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_journey_experience

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1253 (batch 4)
