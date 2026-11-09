# dea:metric-cspm-policy-coverage

Candidate Performance Metric record for **CSPM Policy Coverage** (CSPMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cspm-policy-coverage`
- **Name:** CSPM Policy Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CSPMC

## 2. Definition

CSPM Policy Coverage (CSPMC) addresses conformance to standards, plans, or obligations and is a fixture of cloud security posture management reporting. The formula is Enforced Policies / Framework-Mapped Policies - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of cloud accounts and resources governed by CSPM policy rules. Unmanaged cloud resources are the default condition of cloud: coverage is what makes sprawl governable. Coverage without enforcement mode (detect-only) is observation, not control. Read with cloud compliance framework coverage and mean time to remediate - critical vulnerabilities.

## Formula

```
CSPMC = Enforced Policies / Framework-Mapped Policies
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
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3304 (batch 7)
