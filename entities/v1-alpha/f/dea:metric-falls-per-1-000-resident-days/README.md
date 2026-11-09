# dea:metric-falls-per-1-000-resident-days

Candidate Performance Metric record for **Falls per 1,000 Resident Days** (FPRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-falls-per-1-000-resident-days`
- **Name:** Falls per 1,000 Resident Days
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FPRD

## 2. Definition

Falls per 1,000 Resident Days (FPRD) measures exposure to adverse outcomes in the Elder & Social Care domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Falls / Resident Days x 1,000, measured in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Social care practice.

## 3. Context

Falls per 1,000 resident days measures fall incidence normalized to exposure, and in elder care it is the signature harm event - falls cause injury (fracture, head trauma), trigger hospitalization, drive litigation, and are a regulatory survey focus with fall-related citations common. The metric's honest reading distinguishes expected from preventable: some falls reflect inevitable mobility risk in a frail population pursuing autonomy, and an unrealistically low rate can signal restraint overuse or activity restriction, which is its own harm (immobility deconditioning is a documented fall risk factor in a paradoxical cycle). The evidence-based intervention set is known: strength and balance programs, environment modification, medication review (sedatives and psychotropics are fall-risk drivers), and post-fall root-cause analysis. Read with injurious-fall rate specifically, antipsychotic and sedative use trend, restraint and bed-rail usage (their own harms), and repeat-fall resident analysis.

## Formula

```
FPRD = Falls / Resident Days x 1,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** elder_social_care
- **Sector:** social_care

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1196 (batch 4)
