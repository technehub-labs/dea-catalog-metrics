# dea:metric-audit-cycle-coverage

Candidate Performance Metric record for **Audit Cycle Coverage** (ACC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-audit-cycle-coverage`
- **Name:** Audit Cycle Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ACC

## 2. Definition

A Internal Audit indicator, Audit Cycle Coverage (ACC) quantifies conformance to standards, plans, or obligations. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Auditable Entities Audited within Cycle / Auditable Universe - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of the audit universe covered within the rotating cycle - the breadth metric that answers the completeness question of internal audit: not what was planned and done, but how much of the organization's auditable risk surface has been touched recently. Its strategic significance is the blind-spot control: functions that audit the same familiar areas repeatedly accumulate coverage percentages while the business changes underneath - new systems, new entities, new third parties - and this metric, built against a maintained audit universe, is what surfaces the drift. The honest construction requires the universe itself to be refreshed as the organization changes, since coverage against a stale universe is accurate arithmetic over the wrong denominator. Read with the risk-tiering: full-cycle coverage of low-risk areas is completeness theater, and the risk-weighted version - high-risk areas audited at the frequency their risk demands - is the number with governance meaning.

## Formula

```
Auditable Entities Audited within Cycle / Auditable Universe
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** internal_audit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 613 (batch 2)
