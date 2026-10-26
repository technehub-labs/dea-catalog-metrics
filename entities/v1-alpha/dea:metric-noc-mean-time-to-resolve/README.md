# dea:metric-noc-mean-time-to-resolve

Candidate Performance Metric record for **NOC Mean Time to Resolve** (NOMTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-noc-mean-time-to-resolve`
- **Name:** NOC Mean Time to Resolve
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NOMTR

## 2. Definition

NOC Mean Time to Resolve (NOMTR) addresses how efficiently resources are converted into outputs and is a fixture of network operations center (deep dive) reporting. Its calculation is Hours from Acknowledgment to Resolution, measured in hours. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures average time from ticket open to resolution in network operations. Resolution speed translates directly to restored business capacity. MTTR cut by premature closure and reopening hides real performance. Read with proactive versus reactive ticket ratio and auto-remediation execution rate.

## Formula

```
Hours from Acknowledgment to Resolution
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2839 (batch 7)
