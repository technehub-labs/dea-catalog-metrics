# dea:metric-patent-grant-rate

Candidate Performance Metric record for **Patent Grant Rate** (PGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-patent-grant-rate`
- **Name:** Patent Grant Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PGR

## 2. Definition

Patent Grant Rate (PGR) captures how effectively a process or entity achieves its intended outcome for organizations tracking r&d and innovation. It is defined as Patents Granted / Applications Filed; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of applications that mature to granted patents over time - the conversion metric of the IP pipeline, measuring whether filing strategy produces enforceable claims. Its strategic significance is asset formation: a granted patent is property with litigation, licensing, and collateral value that an application does not have, and conversion is where filing activity becomes portfolio value. The analysis of a falling grant rate runs through the standard suspects: drafting quality, claim scope ambition (aggressive claims fail examination more), art-unit shifts as examiners tighten on software and other contested classes, and prior-art crowding in maturing technology fields. Read with the timing dimension - grants arrive years after filing, so a current grant rate describes the filing strategy of several years ago, and current filing decisions will move it with the same lag - which is why portfolio metrics are always a rear-view mirror with a long focal length.

## Formula

```
Patents Granted / Applications Filed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** r_d_and_innovation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 540 (batch 1)
