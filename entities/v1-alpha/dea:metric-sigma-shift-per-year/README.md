# dea:metric-sigma-shift-per-year

Candidate Performance Metric record for **Sigma Shift per Year** (SSPY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sigma-shift-per-year`
- **Name:** Sigma Shift per Year
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSPY

## 2. Definition

Within Process Excellence (Lean Six Sigma), Sigma Shift per Year (SSPY) is used to gauge the quality of outputs and outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Change in Process Sigma Level Year over Year, measured in score (points). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Sigma shift per year measures annual improvement in process capability (sigma level), and it is the Six Sigma program's progress metric - the framework's aspiration is defect-rate reduction measured in sigma capability, with 6 sigma (3.4 defects per million opportunities) as the reference standard. The metric's honesty problems are structural: sigma-level calculations depend entirely on defect-opportunity definitions (more opportunities per unit flatter the measure), and sigma-shift arithmetic can produce impressive-sounding numbers with modest operational meaning. The strategic value of the metric is directional: capability improvement compounds, and a portfolio of projects that moves key processes half a sigma per year is genuine progress if opportunity definitions stay consistent. Read with the underlying defect-rate trends (the untransformed truth), first-pass-yield changes, and project-benefit validation as the financial cross-check.

## Formula

```
Change in Process Sigma Level Year over Year
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_excellence_lean_six_sigma

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1117 (batch 4)
