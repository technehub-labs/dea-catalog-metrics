# dea:metric-fourth-party-visibility-rate

Candidate Performance Metric record for **Fourth-Party Visibility Rate** (FPVR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fourth-party-visibility-rate`
- **Name:** Fourth-Party Visibility Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FPVR

## 2. Definition

Fourth-Party Visibility Rate (FPVR) captures exposure to adverse outcomes for organizations tracking third-party risk management. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Critical Subprocessors Disclosed and Assessed / Subprocessors Identified, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how well critical vendors' own critical subcontractors are known and assessed. Your fourth parties are where your vendor's failure modes originate. Visibility claimed from attestation rather than evidence is assumed, not known. Read with concentration risk ratio and critical vendor assessment coverage.

## Formula

```
Critical Subprocessors Disclosed and Assessed / Subprocessors Identified
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** third_party_risk_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3722 (batch 8)
