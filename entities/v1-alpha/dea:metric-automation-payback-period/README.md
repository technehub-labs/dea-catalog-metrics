# dea:metric-automation-payback-period

Candidate Performance Metric record for **Automation Payback Period** (APP-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automation-payback-period`
- **Name:** Automation Payback Period
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APP-A

## 2. Definition

Within Automation & Robotic Process Automation, Automation Payback Period (APP-A) is used to gauge the economic value created or preserved. The formula is Implementation Cost / Monthly Cost Avoidance - reported in days. It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how long an automation investment takes to return its cost through realized savings or margin. It disciplines automation programs that drift into tech-led builds with soft benefits. The main honesty issues are savings counted at peak rather than average steady state, and bot maintenance costs excluded from the equation - fragile automations can carry permanent ownership cost. Read with straight-through processing rate (Automation) and exception rates post-deployment.

## Formula

```
Implementation Cost / Monthly Cost Avoidance
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automation_robotic_process_automation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1329 (batch 5)
