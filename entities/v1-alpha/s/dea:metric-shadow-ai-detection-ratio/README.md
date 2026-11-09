# dea:metric-shadow-ai-detection-ratio

Candidate Performance Metric record for **Shadow AI Detection Ratio** (SAIDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shadow-ai-detection-ratio`
- **Name:** Shadow AI Detection Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SAIDR

## 2. Definition

Shadow AI Detection Ratio (SAIDR) measures exposure to adverse outcomes in the AI Governance & Model Risk Management domain. It is defined as Unsanctioned AI Tools Discovered per Audit Cycle; the result is stated in count (items per period). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the discovery rate of unsanctioned AI usage (employee tools, unvetted vendors, departmental pilots) against known inventory. Shadow AI is the ungoverned exposure of AI adoption: business-led tools process enterprise data outside security, privacy, and quality controls, and detection ratio indicates whether governance sees reality or only its inventory. Detection must be active (network, procurement, attestation sweeps), not incidental. Read with model inventory completeness (Deep Dive) and sanctioned-alternative availability - shadow AI often signals an unmet legitimate need.

## Formula

```
SAIDR = Unsanctioned AI Tools Discovered per Audit Cycle
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** ai_governance_model_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2505 (batch 7)
