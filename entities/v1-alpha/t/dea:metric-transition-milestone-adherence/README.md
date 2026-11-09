# dea:metric-transition-milestone-adherence

Candidate Performance Metric record for **Transition Milestone Adherence** (TMA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-transition-milestone-adherence`
- **Name:** Transition Milestone Adherence
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TMA

## 2. Definition

A Outsourcing & Vendor Management indicator, Transition Milestone Adherence (TMA) quantifies conformance to standards, plans, or obligations. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Outsourcing Transition Milestones Met on Time / Milestones, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Transition milestone adherence measures on-time completion of the defined milestones in an outsourcing or transformation transition - knowledge transfer, process migration, go-live phases - and it is the risk-exposure metric of the most dangerous period in outsourcing: the transition, when both sides of the relationship carry cost and neither has full capability. Transitions fail in well-documented patterns (scope creep, knowledge-transfer gaps, parallel-run overrun, key-person attrition), and milestone adherence is the early-warning system. The measurement discipline is milestone-definition honesty: milestones defined loosely (knowledge transfer complete without a completeness test) create green dashboards while capability quietly hollows. Read with knowledge-retention validation (can the receiving team actually run the process without the sender?), parallel-run duration against plan, and post-transition steady-state performance against baseline as the ultimate verdict.

## Formula

```
TMA = Outsourcing Transition Milestones Met on Time / Milestones
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** outsourcing_vendor_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1129 (batch 4)
