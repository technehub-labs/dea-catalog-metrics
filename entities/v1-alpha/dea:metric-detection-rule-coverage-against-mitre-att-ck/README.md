# dea:metric-detection-rule-coverage-against-mitre-att-ck

Candidate Performance Metric record for **Detection Rule Coverage against MITRE ATT&CK** (DRCMA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-detection-rule-coverage-against-mitre-att-ck`
- **Name:** Detection Rule Coverage against MITRE ATT&CK
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DRCMA

## 2. Definition

Within SecOps & Security Operations Center, Detection Rule Coverage against MITRE ATT&CK (DRCMA) is used to gauge capability maturity or development. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as ATT&CK Techniques with Detection Coverage / Applicable Techniques; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how broadly SOC detections map to MITRE ATT&CK techniques. It exposes the techniques adversaries can use against you without tripping a single alert. Mapping that asserts theoretical coverage without validated rule tests (atomic tests) overstates readiness. Read with purple team exercise improvement rate and detection rule health.

## Formula

```
ATT&CK Techniques with Detection Coverage / Applicable Techniques
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2781 (batch 7)
