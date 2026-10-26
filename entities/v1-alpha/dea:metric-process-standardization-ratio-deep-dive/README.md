# dea:metric-process-standardization-ratio-deep-dive

Candidate Performance Metric record for **Process Standardization Ratio (Deep Dive)** (PSR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-standardization-ratio-deep-dive`
- **Name:** Process Standardization Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PSR-D

## 2. Definition

Within Balanced Scorecard - Internal Process Perspective, Process Standardization Ratio (Deep Dive) (PSR-D) is used to gauge capability maturity or development. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Processes Following Global Standard / Processes, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of process variants that follow the standardized design. Standardization is the precondition for automation and consistent customer experience. Standardization that ignores legitimate regional variation drives workarounds. Read with process compliance score and process automation ratio.

## Formula

```
PSR-D = Processes Following Global Standard / Processes
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_internal_process_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3094 (batch 7)
