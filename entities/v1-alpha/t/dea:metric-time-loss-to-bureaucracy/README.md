# dea:metric-time-loss-to-bureaucracy

Candidate Performance Metric record for **Time Loss to Bureaucracy** (TLB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-loss-to-bureaucracy`
- **Name:** Time Loss to Bureaucracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TLB

## 2. Definition

Time Loss to Bureaucracy (TLB) measures how efficiently resources are converted into outputs in the Culture & Employee Experience domain. The formula is Hours Spent on Approvals and Coordination per Employee per Week - reported in hours. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures hours employees lose to low-value internal process - approvals, status reporting, duplicate data entry, compliance theater. It converts organizational friction into the language leadership understands: capacity and cost. Self-report estimates run high and need calibration against process observation, and the metric improves fastest when the same leaders who own the processes sponsor its measurement. Read with decision cycle time and meeting hours per employee per week.

## Formula

```
TLB = Hours Spent on Approvals and Coordination per Employee per Week
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** culture_employee_experience

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1365 (batch 5)
