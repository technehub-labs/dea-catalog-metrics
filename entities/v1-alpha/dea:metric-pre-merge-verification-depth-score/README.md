# dea:metric-pre-merge-verification-depth-score

Candidate Performance Metric record for **Pre-Merge Verification Depth Score** (PMVDS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pre-merge-verification-depth-score`
- **Name:** Pre-Merge Verification Depth Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PMVDS

## 2. Definition

Pre-Merge Verification Depth Score (PMVDS) captures the quality of outputs and outcomes for organizations tracking continuous integration. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Composite Gate Strength Score for Merge Checks, expressed in index (0-100 or normalized). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the rigor of automated verification required before code merges - test coverage gates, static analysis, security scans, review requirements. Pre-merge verification is the cheapest defect interception point in the entire delivery pipeline, and depth here is the strongest predictor of downstream change-failure rates. Depth must be tuned by change risk, since uniform heavyweight gates encourage process bypass. Read with change failure rate (Deep Dive) and escaped-defect trends.

## Formula

```
PMVDS = Composite Gate Strength Score for Merge Checks
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2681 (batch 7)
