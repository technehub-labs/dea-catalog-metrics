# dea:metric-third-party-compliance-attestation-rate

Candidate Performance Metric record for **Third-Party Compliance Attestation Rate** (TPCAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-third-party-compliance-attestation-rate`
- **Name:** Third-Party Compliance Attestation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TPCAR

## 2. Definition

Third-Party Compliance Attestation Rate (TPCAR) addresses conformance to standards, plans, or obligations and is a fixture of compliance monitoring & testing reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Vendors Submitting Compliance Attestations / Vendors in Scope, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
TPCAR = Vendors Submitting Compliance Attestations / Vendors in Scope
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** compliance_monitoring_testing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3574 (batch 8)
