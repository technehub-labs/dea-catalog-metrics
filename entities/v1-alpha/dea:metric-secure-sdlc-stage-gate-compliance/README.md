# dea:metric-secure-sdlc-stage-gate-compliance

Candidate Performance Metric record for **Secure SDLC Stage Gate Compliance** (SSDLC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-secure-sdlc-stage-gate-compliance`
- **Name:** Secure SDLC Stage Gate Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SSDLC

## 2. Definition

A Application Security (AppSec) indicator, Secure SDLC Stage Gate Compliance (SSDLC) quantifies conformance to standards, plans, or obligations. The formula is Projects Passing Security Gates at Each Stage / Projects - reported in percent (%). It is a standard measure in the Software sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether security activities are performed and passed at each SDLC stage. Gates embedded in the lifecycle are how security becomes non-optional. Compliance by waiver is compliance in name only. Read with security gate enforcement rate and secure SDLC stage gate compliance (DevSecOps variants).

## Formula

```
Projects Passing Security Gates at Each Stage / Projects
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** application_security_appsec
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3337 (batch 7)
