# dea:metric-span-of-control

Candidate Performance Metric record for **Span of Control** (SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-span-of-control`
- **Name:** Span of Control
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SOC

## 2. Definition

A Operating Model & Decision Effectiveness indicator, Span of Control (SOC) quantifies the utilization or availability of capacity. It is computed as Direct Reports / Manager, Averaged, expressed in ratio (x:1 or x). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the average number of direct reports per manager. It is the structural lever behind cost, speed, and career pathing: narrow spans bloat management cost and slow decisions, while very wide spans thin coaching and oversight. Optimal span varies by work complexity - a number that is healthy in routine operations is reckless in ambiguous knowledge work. Read as a distribution, not an average, paired with organizational layers, since restructuring often trades one against the other.

## Formula

```
Direct Reports / Manager, Averaged
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_decision_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1306 (batch 5)
