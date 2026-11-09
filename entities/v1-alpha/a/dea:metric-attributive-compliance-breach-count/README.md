# dea:metric-attributive-compliance-breach-count

Candidate Performance Metric record for **Attributive Compliance Breach Count** (ACBC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attributive-compliance-breach-count`
- **Name:** Attributive Compliance Breach Count
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACBC

## 2. Definition

Attributive Compliance Breach Count (ACBC) measures exposure to adverse outcomes in the Compliance Monitoring & Testing domain. It is defined as Notifiable Breaches in Period; the result is stated in count (items per period). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures breaches attributable to a specific control or obligation failure. Attribution converts breach counts into fixable causes. Broad attribution (human error) fixes nothing. Read with key control operating effectiveness rate and compliance rule breach count.

## Formula

```
ACBC = Notifiable Breaches in Period
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** compliance_monitoring_testing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3565 (batch 8)
