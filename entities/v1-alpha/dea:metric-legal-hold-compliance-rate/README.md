# dea:metric-legal-hold-compliance-rate

Candidate Performance Metric record for **Legal Hold Compliance Rate** (LHCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-legal-hold-compliance-rate`
- **Name:** Legal Hold Compliance Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LHCR

## 2. Definition

Legal Hold Compliance Rate (LHCR) captures conformance to standards, plans, or obligations for organizations tracking legal operations. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Holds Implemented and Acknowledged on Time / Holds Issued - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether custodians under legal hold suspend destruction and confirm acknowledgment. Holds are where e-discovery sanctions originate, and a single compliance gap can cost more than years of legal budget. Sample-test actual preservation (not just acknowledgments), since custodians confirm and delete anyway. Read with hold-release discipline and spoliation findings in discovery.

## Formula

```
Holds Implemented and Acknowledged on Time / Holds Issued
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** legal_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1678 (batch 6)
