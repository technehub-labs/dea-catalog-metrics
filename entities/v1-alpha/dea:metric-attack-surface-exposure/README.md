# dea:metric-attack-surface-exposure

Candidate Performance Metric record for **Attack Surface Exposure** (ASE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attack-surface-exposure`
- **Name:** Attack Surface Exposure
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ASE

## 2. Definition

Attack Surface Exposure (ASE) addresses exposure to adverse outcomes and is a fixture of cybersecurity reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Internet-Exposed Assets Requiring Remediation, expressed in count (items per period). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the count and severity of internet-facing exposures across ports, services, and assets. It matters because attackers scan continuously, so unneeded exposure is eventual compromise. Gaming risk includes narrowing the definition of exposure to exclude legacy or shadow-IT assets. Read with Critical Patch Compliance and Vulnerability Remediation Time to track whether exposure is shrinking and being fixed faster.

## Formula

```
Internet-Exposed Assets Requiring Remediation
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 328 (batch 1)
