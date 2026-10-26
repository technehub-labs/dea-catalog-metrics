# dea:metric-chaos-experiment-execution-rate

Candidate Performance Metric record for **Chaos Experiment Execution Rate** (CEER-SRE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-chaos-experiment-execution-rate`
- **Name:** Chaos Experiment Execution Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CEER-SRE

## 2. Definition

Within Observability & Site Reliability Engineering, Chaos Experiment Execution Rate (CEER-SRE) is used to gauge capability maturity or development. The formula is Chaos Experiments Run per Period / Planned - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how regularly controlled failure experiments run against critical services. Chaos engineering verifies redundancy assumptions before production does it involuntarily. Experiments without automated abort conditions create self-inflicted outages. Read with availability zone redundancy compliance and error budget consumption rate.

## Formula

```
Chaos Experiments Run per Period / Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2878 (batch 7)
