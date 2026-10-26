# dea:metric-resistance-escalation-rate

Candidate Performance Metric record for **Resistance Escalation Rate** (RER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-resistance-escalation-rate`
- **Name:** Resistance Escalation Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RER

## 2. Definition

Resistance Escalation Rate (RER) measures exposure to adverse outcomes in the Change Management domain. It is defined as Resistance Cases Escalated / Resistance Cases Identified; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how often change resistance escalates beyond local management. It matters because escalations signal engagement gaps that were not addressed early. Escalations can be suppressed by discouraging dissent rather than resolving it. Read with Change Adoption Rate and Pulse Survey sentiment to confirm resistance is falling for the right reasons.

## Formula

```
Resistance Cases Escalated / Resistance Cases Identified
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** transformation
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** change_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1381 (batch 5)
