# dea:metric-sigma-level

Candidate Performance Metric record for **Sigma Level** (SIG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sigma-level`
- **Name:** Sigma Level
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SIG

## 2. Definition

Within Quality Management, Sigma Level (SIG) is used to gauge the quality of outputs and outcomes. Its calculation is Normal Inverse CDF of (1 - DPMO/1,000,000) + 1.5 Shift, measured in score (points). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Process quality expressed in standard deviations of capability between the process center and the nearest specification limit - the Six Sigma movement's universal quality scale. The scale's strategic contribution is the nonlinearity it exposes: moving from three sigma (about 67,000 DPMO) to four (about 6,200) removes an order of magnitude of defects, and the last steps to six sigma (3.4) demand a different kind of control, which is why sigma levels map naturally to maturity stages rather than being one continuous improvement gradient. The movement's famous 1.5-sigma shift - assuming long-term drift from short-term capability - is a convention, not physics, and different shops quote sigma with and without it, so comparisons require matching convention. A sigma level is only as meaningful as the data behind it, and control-chart stability is the prerequisite.

## Formula

```
SIG = Normal Inverse CDF of (1 - DPMO/1,000,000) + 1.5 Shift
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 234 (batch 1)
