# dea:metric-human-review-coverage-of-automated-decisions

Candidate Performance Metric record for **Human Review Coverage of Automated Decisions** (HRCAD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-human-review-coverage-of-automated-decisions`
- **Name:** Human Review Coverage of Automated Decisions
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** HRCAD

## 2. Definition

Human Review Coverage of Automated Decisions (HRCAD) addresses exposure to adverse outcomes and is a fixture of ai ethics, fairness & responsible ai reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Automated Decisions Subject to Human Review / Eligible Decisions, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of consequential automated decisions subject to human review before taking effect. It is the contestability control under emerging AI regulation: consequential decisions (credit, employment, benefits) increasingly require meaningful human involvement, and coverage determines the compliance posture. Review quality is the honest-read question - reviewer override rates near zero indicate procedural review. Read with human-in-the-loop coverage for high-risk decisions (Deep Dive) and override-rate distributions.

## Formula

```
Automated Decisions Subject to Human Review / Eligible Decisions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_ethics_fairness_responsible_ai

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2569 (batch 7)
