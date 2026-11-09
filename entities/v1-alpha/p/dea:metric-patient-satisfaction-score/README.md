# dea:metric-patient-satisfaction-score

Candidate Performance Metric record for **Patient Satisfaction Score** (PSS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-patient-satisfaction-score`
- **Name:** Patient Satisfaction Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PSS

## 2. Definition

Patient Satisfaction Score (PSS) measures the engagement or satisfaction of the people involved in the Healthcare domain. Its calculation is Satisfied Patient Survey Responses / Responses, measured in percent (%). It originates from and is most used in Healthcare practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The aggregate of patient-reported experience across care episodes - conventionally through standardized survey instruments (the HCAHPS family in the US and analogues elsewhere), because unstandardized satisfaction measurement is opinion-gathering rather than measurement. Its strategic significance is reimbursement linkage: value-based payment regimes in several countries attach a share of payment to experience performance, which converts the score from a reputation number into a revenue variable. The honest read separates experience from outcome: satisfaction tracks communication, responsiveness, and environment more strongly than clinical results (which patients judge partly on trust), so the metric measures service quality alongside care quality, and the two can diverge. Read the domain-level cuts: discharge communication and care-transition items tend to score lowest across systems, which is why transition programs, not amenity programs, are the evidence-backed route to improving this metric.

## Formula

```
PSS = Satisfied Patient Survey Responses / Responses
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 466 (batch 1)
