# dea:metric-claims-frequency-rate

Candidate Performance Metric record for **Claims Frequency Rate** (CFR-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claims-frequency-rate`
- **Name:** Claims Frequency Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CFR-C

## 2. Definition

Claims Frequency Rate (CFR-C) measures exposure to adverse outcomes in the Claims Operations (Insurance) domain. Its calculation is Claims Filed / Policies In Force, measured in ratio (x:1 or x). It originates from and is most used in Insurance practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Claims frequency measures how often insured events occur per exposure unit (policies, vehicle-years, payroll), and it is the first half of the loss-cost equation (frequency times severity) that drives insurance pricing. Frequency trends carry distinct intelligence: rising frequency in property often reflects climate-driven event patterns, while rising liability frequency may reflect litigation environment or claims consciousness rather than underlying risk. The measurement discipline is exposure-base integrity - frequency without accurate denominators (vehicle counts, payroll, insured values) is meaningless, and exposure data is frequently stale. Read with severity trend separately (the two can move opposite directions and offset or compound), mix shifts in the insured book (aging vehicle fleets change frequency mechanically), and frequency by per-cause decomposition to find drivers.

## Formula

```
CFR-C = Claims Filed / Policies In Force
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 846 (batch 3)
