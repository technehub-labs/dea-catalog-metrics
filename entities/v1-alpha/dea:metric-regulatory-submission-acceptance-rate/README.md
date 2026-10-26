# dea:metric-regulatory-submission-acceptance-rate

Candidate Performance Metric record for **Regulatory Submission Acceptance Rate** (RSAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-regulatory-submission-acceptance-rate`
- **Name:** Regulatory Submission Acceptance Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RSAR

## 2. Definition

Regulatory Submission Acceptance Rate (RSAR) measures the quality of outputs and outcomes in the Pharma R&D & Clinical Trials domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Submissions Accepted First Time / Submissions, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Pharmaceuticals practice.

## 3. Context

Measures the share of regulatory submissions accepted for review on first filing, without refusal-to-file. First-cycle acceptance protects launch timelines, and refusals signal deeper quality problems in the evidence package or CMC. Track acceptance without major information requests separately from formal refusals, since near-misses reveal the same weaknesses. Read with database lock cycle time and time to regulatory decision.

## Formula

```
RSAR = Submissions Accepted First Time / Submissions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** pharma_r_d_clinical_trials
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1619 (batch 6)
