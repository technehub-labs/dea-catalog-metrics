# dea:metric-model-robustness-test-pass-rate

Candidate Performance Metric record for **Model Robustness Test Pass Rate** (MRTPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-robustness-test-pass-rate`
- **Name:** Model Robustness Test Pass Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MRTPR

## 2. Definition

Model Robustness Test Pass Rate (MRTPR) captures exposure to adverse outcomes for organizations tracking ai ethics, fairness & responsible ai. It is computed as Adversarial and Edge Case Tests Passed / Tests, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how models perform under adversarial, edge-case, and distribution-shift testing. Robustness is the security-and-reliability gate for deployed models: production inputs are messier than test sets, and pass rates on adversarial suites predict field behavior better than clean benchmarks. Test suites must evolve with the threat landscape, since last year's suite measures last year's risks. Read with production incident rates and red-team coverage.

## Formula

```
MRTPR = Adversarial and Edge Case Tests Passed / Tests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2580 (batch 7)
