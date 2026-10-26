# dea:metric-automation-downtime-cost

Candidate Performance Metric record for **Automation Downtime Cost** (ADC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automation-downtime-cost`
- **Name:** Automation Downtime Cost
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ADC

## 2. Definition

Automation Downtime Cost (ADC) captures exposure to adverse outcomes for organizations tracking industrial automation & robotics. Its calculation is Lost Output Value from Automation Unavailability per Period, measured in currency value. It originates from and is most used in Manufacturing practice. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the production cost of automated system outages. It matters because automation concentrates risk; when it fails, it fails expensively. Downtime cost can be understated by allocating failures to manual-workaround cost lines. Read with Robot Mean Time between Failures and Maintenance Cost per Asset to confirm downtime economics are visible.

## Formula

```
Lost Output Value from Automation Unavailability per Period
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** industrial_automation_robotics
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1340 (batch 5)
