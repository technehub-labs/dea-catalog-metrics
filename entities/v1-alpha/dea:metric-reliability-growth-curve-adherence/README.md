# dea:metric-reliability-growth-curve-adherence

Candidate Performance Metric record for **Reliability Growth Curve Adherence** (RGCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reliability-growth-curve-adherence`
- **Name:** Reliability Growth Curve Adherence
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RGCA

## 2. Definition

Reliability Growth Curve Adherence (RGCA) addresses the quality of outputs and outcomes and is a fixture of aerospace & defense program management reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Actual MTBF vs Planned Growth Curve, measured in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Aerospace & Defense practice.

## 3. Context

Measures whether demonstrated reliability of the system is tracking the planned growth curve across test events. Defense and aerospace reliability grows through finding and fixing failure modes, so adherence is the honest measure of whether test-find-fix is working or whether failures are being deferred. Compare against the idealized growth curve, and beware reliability demonstrated in benign test conditions. Read with mean time between failures trends and failure-mode closure rates.

## Formula

```
Actual MTBF vs Planned Growth Curve
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** aerospace_defense_program_management
- **Sector:** aerospace_defense

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1789 (batch 6)
