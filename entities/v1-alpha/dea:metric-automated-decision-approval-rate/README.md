# dea:metric-automated-decision-approval-rate

Candidate Performance Metric record for **Automated Decision Approval Rate** (ADAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-automated-decision-approval-rate`
- **Name:** Automated Decision Approval Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ADAR

## 2. Definition

Within Automation & Robotic Process Automation, Automated Decision Approval Rate (ADAR) is used to gauge the quality of outputs and outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Automated Decisions Upheld on Review / Automated Decisions Sampled, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of automated decisions - credit, claims, pricing, underwriting - that pass without human review. Rising rates mean the rules and models are trusted; rising rates with rising overturns on audit mean confidence has outrun accuracy. Track approval and override together, and by decision class, since blanket rates conceal the decision types where automation quietly fails. Read with override rates and downstream loss or complaint outcomes for those decisions.

## Formula

```
Automated Decisions Upheld on Review / Automated Decisions Sampled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automation_robotic_process_automation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1331 (batch 5)
