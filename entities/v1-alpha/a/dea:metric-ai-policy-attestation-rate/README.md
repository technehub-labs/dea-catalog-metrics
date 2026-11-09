# dea:metric-ai-policy-attestation-rate

Candidate Performance Metric record for **AI Policy Attestation Rate** (AIPAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ai-policy-attestation-rate`
- **Name:** AI Policy Attestation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AIPAR

## 2. Definition

A AI Governance & Model Risk Management indicator, AI Policy Attestation Rate (AIPAR) quantifies conformance to standards, plans, or obligations. It is computed as Staff Attesting to AI Usage Policy / Staff in Scope, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
AIPAR = Staff Attesting to AI Usage Policy / Staff in Scope
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_governance_model_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2494 (batch 7)
