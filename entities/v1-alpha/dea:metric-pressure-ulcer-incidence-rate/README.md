# dea:metric-pressure-ulcer-incidence-rate

Candidate Performance Metric record for **Pressure Ulcer Incidence Rate** (PUIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pressure-ulcer-incidence-rate`
- **Name:** Pressure Ulcer Incidence Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PUIR

## 2. Definition

A Elder & Social Care indicator, Pressure Ulcer Incidence Rate (PUIR) quantifies the quality of outputs and outcomes. It is computed as New Pressure Ulcers / Resident Days x 1,000, expressed in events per thousand or million (scaled). Its use is concentrated in Social care. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Pressure ulcer incidence measures new pressure injuries developing in the facility, and in elder care it is the sentinel quality event - a stage-3 or 4 ulcer signals sustained care failure over time (these wounds take days to develop, meaning assessment gaps and repositioning failures), and regulators cite it, litigators pursue it, and payers increasingly penalize it. The incidence-versus-prevalence distinction matters: prevalence includes ulcers present on admission (often hospital-acquired), so incidence isolates facility-caused harm. The intervention evidence base is strong: risk assessment on admission (Braden and similar scales), repositioning schedules, nutrition support, and surface selection - and measurement of compliance with those upstream processes is the honest management view. Read with stage distribution (severity weighting), assessment-timeliness compliance, weight-loss and malnutrition trend (the nutritional driver), and unit-level clustering which points at staffing.

## Formula

```
New Pressure Ulcers / Resident Days x 1,000
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1201 (batch 4)
