# dea:metric-catheter-associated-urinary-tract-infection-rate

Candidate Performance Metric record for **Catheter-Associated Urinary Tract Infection Rate** (CAUTI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-catheter-associated-urinary-tract-infection-rate`
- **Name:** Catheter-Associated Urinary Tract Infection Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CAUTI

## 2. Definition

Catheter-Associated Urinary Tract Infection Rate (CAUTI) addresses exposure to adverse outcomes and is a fixture of healthcare quality & patient safety standard measures reporting. It is computed as CAUTI Events / 1,000 Catheter Days, expressed in events per thousand or million (scaled). Its use is concentrated in Healthcare. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures CAUTI events per catheter-day. CAUTI is a preventable-harm measure driven by device avoidance discipline. Rates influenced by culturing practice as well as insertion practice. Read with central line-associated bloodstream infection rate and device utilization ratio.

## Formula

```
CAUTI Events / 1,000 Catheter Days
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** healthcare_quality_patient_safety_standard_measures
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4240 (batch 10)
