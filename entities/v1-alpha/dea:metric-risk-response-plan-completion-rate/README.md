# dea:metric-risk-response-plan-completion-rate

Candidate Performance Metric record for **Risk Response Plan Completion Rate** (RRPCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-risk-response-plan-completion-rate`
- **Name:** Risk Response Plan Completion Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RRPCR

## 2. Definition

Risk Response Plan Completion Rate (RRPCR) captures exposure to adverse outcomes for organizations tracking project management (deep dive). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Mitigation Plans Implemented for Red Risks / Red Risks - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of identified significant risks with funded, owned response plans. Identified-but-unmanaged risk is just documented failure. Completion of plans without trigger conditions and owners is paperwork. Read with risk exposure trend index and benefits realization rate.

## Formula

```
Mitigation Plans Implemented for Red Risks / Red Risks
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** project_management_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2940 (batch 7)
