# dea:metric-process-capability-index-cpk

Candidate Performance Metric record for **Process Capability Index (Cpk)** (CPKS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-capability-index-cpk`
- **Name:** Process Capability Index (Cpk)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPKS

## 2. Definition

A Process Capability & Six Sigma (Deep Dive) indicator, Process Capability Index (Cpk) (CPKS) quantifies the quality of outputs and outcomes. It is computed as Min Distance of Mean to Spec Limit / (3 x Std Dev), expressed in ratio (x:1 or x). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Manufacturing.

## 3. Context

Cpk is Cp adjusted for centering - the distance from the process mean to the nearest specification limit, divided by three standard deviations. It is the realistic capability number: Cpk 1.33 leaves about 32 defects per million, 1.67 about 0.6, and the gap between Cp and Cpk quantifies exactly how much is lost to off-center operation, which makes the offset a direct work order. Note that Cp/Cpk assume stability and normality - check control charts first, because capability math on an unstable process is arithmetic on noise.

## Formula

```
Min Distance of Mean to Spec Limit / (3 x Std Dev)
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Statistical process control tradition (Juran / SQC)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4076 (batch 9)
