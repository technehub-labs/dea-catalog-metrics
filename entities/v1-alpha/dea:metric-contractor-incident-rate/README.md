# dea:metric-contractor-incident-rate

Candidate Performance Metric record for **Contractor Incident Rate** (CIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-contractor-incident-rate`
- **Name:** Contractor Incident Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CIR

## 2. Definition

Contractor Incident Rate (CIR) captures exposure to adverse outcomes for organizations tracking health & safety. The formula is (Contractor Recordable Incidents x 200,000) / Contractor Hours - reported in ratio (x:1 or x). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures incidents involving contractors per contractor hours worked. It matters because contractor safety is legally and morally the host's responsibility, not a separate category. Gaming risk includes offloading contractor incidents to the contractor firm so they vanish from host metrics. Read with Safety Audit Compliance Score and contractor onboarding safety verification to confirm parity of protection.

## Formula

```
(Contractor Recordable Incidents x 200,000) / Contractor Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** health_safety

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 408 (batch 1)
