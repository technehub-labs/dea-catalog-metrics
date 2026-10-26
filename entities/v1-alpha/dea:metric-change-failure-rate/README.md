# dea:metric-change-failure-rate

Candidate Performance Metric record for **Change Failure Rate** (CFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-change-failure-rate`
- **Name:** Change Failure Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CFR

## 2. Definition

Change Failure Rate (CFR) addresses the quality of outputs and outcomes and is a fixture of software engineering reporting. It is computed as Deployments Causing Failure / Total Deployments, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Change failure rate, a DORA metric, is the share of production changes that cause degraded service or require remediation - rollback, hotfix, patch. Elite teams sit under 15%; high performers up to about a quarter. Read it jointly with deployment frequency: deploying rarely and still failing is the worst quadrant, while high frequency with low failure rate is the elite profile. The main measurement pitfall is inconsistent definitions of failure - agree once on what counts (rollback, incident, emergency fix) and keep that definition stable.

## Formula

```
Deployments Causing Failure / Total Deployments
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** DORA research program (DevOps Research and Assessment)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 279 (batch 1)
