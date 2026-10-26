# dea:metric-system-interoperability-certification-rate

Candidate Performance Metric record for **System Interoperability Certification Rate** (SICR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-system-interoperability-certification-rate`
- **Name:** System Interoperability Certification Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SICR

## 2. Definition

System Interoperability Certification Rate (SICR) captures conformance to standards, plans, or obligations for organizations tracking defense & aerospace. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Systems Certified Interoperable / Systems Requiring Certification, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Defense & aerospace practice.

## 3. Context

Measures the share of systems certified as interoperable with required interfaces and standards. It matters because joint operations fail on integration seams more than on platform performance. Certification can be achieved in test environments that never replicate operational load. Read with Integration Test findings and exercises-driven interface failure reports to confirm certification holds under real conditions.

## Formula

```
Systems Certified Interoperable / Systems Requiring Certification
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** defense_aerospace
- **Sector:** defense_aerospace

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 974 (batch 3)
