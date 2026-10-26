# dea:metric-crisis-decision-log-completeness

Candidate Performance Metric record for **Crisis Decision Log Completeness** (CDLC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-crisis-decision-log-completeness`
- **Name:** Crisis Decision Log Completeness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDLC

## 2. Definition

Crisis Decision Log Completeness (CDLC) captures conformance to standards, plans, or obligations for organizations tracking crisis management & emergency response. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Crisis Decisions with Documented Rationale / Decisions - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether crisis decisions, owners, and rationale are logged in real time. The log is both the legal record and the raw material for post-crisis learning. Reconstructed logs written after the fact are memoirs, not records. Read with crisis media response accuracy rate and post-incident review action closure rate.

## Formula

```
CDLC = Crisis Decisions with Documented Rationale / Decisions
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** crisis_management_emergency_response

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3536 (batch 8)
