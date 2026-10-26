# dea:metric-cyclomatic-complexity-deep-dive

Candidate Performance Metric record for **Cyclomatic Complexity (Deep Dive)** (CYCD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cyclomatic-complexity-deep-dive`
- **Name:** Cyclomatic Complexity (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CYCD

## 2. Definition

A Code Quality & Static Analysis indicator, Cyclomatic Complexity (Deep Dive) (CYCD) quantifies the quality of outputs and outcomes. Its calculation is Count of Independent Paths through Code Unit, measured in count (items per period). It originates from and is most used in Software practice. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Cyclomatic complexity, introduced by Thomas J. McCabe Sr. (1976), counts the independent paths through a unit of code - effectively decision points plus one. It is the number of test cases needed for branch coverage, which is why it became the industry's structural-complexity yardstick: above 10 per function review is advised, above 20 refactoring. Its blind spot is that it counts decisions, not their arrangement - deeply nested code is harder than a flat chain of the same count - which is what the newer cognitive complexity measure addresses. Use it as a gate in code review, not a proxy for all maintainability.

## Formula

```
Count of Independent Paths through Code Unit
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Thomas J. McCabe Sr., 1976

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4175 (batch 9)
