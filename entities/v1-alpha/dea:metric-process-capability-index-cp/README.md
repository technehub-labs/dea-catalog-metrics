# dea:metric-process-capability-index-cp

Candidate Performance Metric record for **Process Capability Index (Cp)** (CPSIX) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-capability-index-cp`
- **Name:** Process Capability Index (Cp)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPSIX

## 2. Definition

Process Capability Index (Cp) (CPSIX) measures the quality of outputs and outcomes in the Process Capability & Six Sigma (Deep Dive) domain. Its calculation is (Upper Spec - Lower Spec) / (6 x Within-Group Std Dev), measured in ratio (x:1 or x). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Manufacturing practice.

## 3. Context

Cp, from the statistical process control tradition, is the specification width divided by the process width (six within-group standard deviations) - potential capability if the process were perfectly centered. Cp 1.0 means the process just fits the specs; 1.33 has been the historical minimum for capable processes, 1.67 for safety-critical. Crucially Cp ignores centering: a Cp of 2 with the mean parked at a spec limit still makes defects. Always read it with Cpk, which applies the same arithmetic to the nearest limit.

## Formula

```
CPSIX = (Upper Spec - Lower Spec) / (6 x Within-Group Std Dev)
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4075 (batch 9)
