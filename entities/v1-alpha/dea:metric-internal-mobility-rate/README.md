# dea:metric-internal-mobility-rate

Candidate Performance Metric record for **Internal Mobility Rate** (IMR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-internal-mobility-rate`
- **Name:** Internal Mobility Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IMR

## 2. Definition

A Human Resources indicator, Internal Mobility Rate (IMR) quantifies capability maturity or development. It is computed as Employees Moving to New Internal Roles / Headcount, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of roles filled by internal candidates - the metric that measures whether the organization is a career system or a collection of jobs. Its strategic weight is retention economics: employees who move internally stay measurably longer, and the flight risk of high performers with no visible next role is the classic regrettable-attrition pattern. A rate near zero means every promotion is a resignation trigger for whoever wanted the job, and every hire is a cultural import at full market price. The healthy pattern is mobility without blockage: cross-functional moves matter as much as vertical ones, and a rate that includes lateral development reads stronger than one counting only promotions. Read with succession coverage, which together describe whether talent is a pipeline or a series of external purchases.

## Formula

```
Employees Moving to New Internal Roles / Headcount
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** human_resources

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 151 (batch 1)
