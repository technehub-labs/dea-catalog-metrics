# dea:metric-detection-rule-health-false-negative-rate

Candidate Performance Metric record for **Detection Rule Health - False Negative Rate** (DRHFN) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-detection-rule-health-false-negative-rate`
- **Name:** Detection Rule Health - False Negative Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DRHFN

## 2. Definition

Detection Rule Health - False Negative Rate (DRHFN) measures exposure to adverse outcomes in the SecOps & Security Operations Center domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Valid Threats Missed by Rules / Valid Threats in Test; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how often validated attacks evade existing detection rules during testing. False negatives are silent blindness: nobody sees what nobody alerts on. Regular atomic testing is required, since rules decay as infrastructure changes. Read with detection rule coverage against MITRE ATT&CK and purple team exercise improvement rate.

## Formula

```
DRHFN = Valid Threats Missed by Rules / Valid Threats in Test
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2782 (batch 7)
