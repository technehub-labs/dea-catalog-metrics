# dea:metric-recurring-incident-ratio

Candidate Performance Metric record for **Recurring Incident Ratio** (RIR-IT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recurring-incident-ratio`
- **Name:** Recurring Incident Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RIR-IT

## 2. Definition

A IT Incident & Major Problem Management indicator, Recurring Incident Ratio (RIR-IT) quantifies the quality of outputs and outcomes. It is defined as Incidents Repeating within 30 Days / Incidents; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of incidents matching previously seen symptoms or root causes. Recurrence is the scar tissue of unfinished problem management. Broad matching criteria can inflate it; overly narrow criteria hide it. Read with problem record creation rate and root cause analysis completion rate.

## Formula

```
RIR-IT = Incidents Repeating within 30 Days / Incidents
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2896 (batch 7)
