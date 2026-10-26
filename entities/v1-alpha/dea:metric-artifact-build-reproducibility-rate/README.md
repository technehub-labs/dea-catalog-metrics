# dea:metric-artifact-build-reproducibility-rate

Candidate Performance Metric record for **Artifact Build Reproducibility Rate** (ABRR-CI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-artifact-build-reproducibility-rate`
- **Name:** Artifact Build Reproducibility Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ABRR-CI

## 2. Definition

Artifact Build Reproducibility Rate (ABRR-CI) addresses the quality of outputs and outcomes and is a fixture of continuous integration reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Builds Producing Identical Artifacts from Same Input / Sampled, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether builds produce bit-identical (or verified-equivalent) artifacts from the same source. Reproducibility is the supply-chain integrity foundation of CI: it enables provenance verification, protects against compromised build systems, and eliminates the works-on-my-machine class of defects. Signed provenance attestation extends reproducibility into verifiable trust. Read with dependency-lockfile discipline and supply-chain attestation coverage.

## Formula

```
Builds Producing Identical Artifacts from Same Input / Sampled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2669 (batch 7)
