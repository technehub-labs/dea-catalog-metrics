# dea:metric-time-to-hire

Candidate Performance Metric record for **Time to Hire** (TTH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-to-hire`
- **Name:** Time to Hire
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TTH

## 2. Definition

Within Human Resources, Time to Hire (TTH) is used to gauge how efficiently resources are converted into outputs. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Days from Candidate Application to Offer Acceptance, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures days from candidate application (or first interview) to offer acceptance. It matters as the candidate-experience half of recruiting speed, where slow processes lose top talent. It can be gamed by delaying the application timestamp or racing only pre-vetted candidates. Read with Offer Acceptance Rate and Time to Fill to see whether process speed or candidate quality is driving the number.

## Formula

```
Days from Candidate Application to Offer Acceptance
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 133 (batch 1)
