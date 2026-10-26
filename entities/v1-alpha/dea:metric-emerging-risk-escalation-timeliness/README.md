# dea:metric-emerging-risk-escalation-timeliness

Candidate Performance Metric record for **Emerging Risk Escalation Timeliness** (ERET) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emerging-risk-escalation-timeliness`
- **Name:** Emerging Risk Escalation Timeliness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ERET

## 2. Definition

A Emerging Risk & Horizon Scanning indicator, Emerging Risk Escalation Timeliness (ERET) quantifies conformance to standards, plans, or obligations. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Emerging Risks Escalated within Threshold / Risks Meeting Criteria - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether assessed emerging risks reach decision-makers within required windows. Late escalation converts manageable risks into arrived ones. Timeliness measured from assessment completion rather than identification underreports. Read with emerging risk escalation rate and decision cycle time - strategic decisions.

## Formula

```
ERET = Emerging Risks Escalated within Threshold / Risks Meeting Criteria
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** emerging_risk_horizon_scanning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3998 (batch 8)
