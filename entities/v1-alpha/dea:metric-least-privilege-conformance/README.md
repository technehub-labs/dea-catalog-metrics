# dea:metric-least-privilege-conformance

Candidate Performance Metric record for **Least Privilege Conformance** (LPC-CS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-least-privilege-conformance`
- **Name:** Least Privilege Conformance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LPC-CS

## 2. Definition

Least Privilege Conformance (LPC-CS) addresses exposure to adverse outcomes and is a fixture of cloud security posture management reporting. The formula is Identities within Least-Privilege Policy / Identities - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how well cloud identities and roles conform to least-privilege policy. Over-privileged cloud roles turn any compromise into blast radius. Conformance measured against permissive baselines is self-congratulation. Read with standing privilege reduction rate and CSPM policy coverage.

## Formula

```
Identities within Least-Privilege Policy / Identities
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3308 (batch 7)
