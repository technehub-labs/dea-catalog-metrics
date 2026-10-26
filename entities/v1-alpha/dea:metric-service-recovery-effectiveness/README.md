# dea:metric-service-recovery-effectiveness

Candidate Performance Metric record for **Service Recovery Effectiveness** (SRE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-recovery-effectiveness`
- **Name:** Service Recovery Effectiveness
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SRE

## 2. Definition

Service Recovery Effectiveness (SRE) addresses the quality of outputs and outcomes and is a fixture of customer journey & experience reporting. It is computed as Recovered Customers after Service Failure / Service Failure Cases, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how well failures are converted into retained, even strengthened, relationships. It matters because recovery is the single biggest lever on post-failure loyalty. Recovery scores can look strong when only trivial failures are recovered. Read with Churn after Service Failure and Complaint Rate trends to confirm recovery effectiveness at serious failures.

## Formula

```
Recovered Customers after Service Failure / Service Failure Cases
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1255 (batch 4)
