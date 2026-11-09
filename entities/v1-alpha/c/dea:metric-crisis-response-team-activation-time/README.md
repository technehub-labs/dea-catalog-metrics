# dea:metric-crisis-response-team-activation-time

Candidate Performance Metric record for **Crisis Response Team Activation Time** (CRTAT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-crisis-response-team-activation-time`
- **Name:** Crisis Response Team Activation Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRTAT

## 2. Definition

A Crisis Management & Emergency Response indicator, Crisis Response Team Activation Time (CRTAT) quantifies how efficiently resources are converted into outputs. It is computed as Minutes from Trigger to Crisis Team Convened, expressed in minutes. It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures elapsed time from crisis declaration to the response team being operational. The first hour of a crisis disproportionately determines its cost. Activation delayed by unclear trigger criteria is the common failure. Read with crisis simulation cadence compliance and incident command structure deployment rate.

## Formula

```
CRTAT = Minutes from Trigger to Crisis Team Convened
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** governance
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** crisis_management_emergency_response

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3535 (batch 8)
