# dea:metric-mean-time-to-detect

Candidate Performance Metric record for **Mean Time to Detect** (MTTD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-detect`
- **Name:** Mean Time to Detect
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTTD

## 2. Definition

Mean Time to Detect (MTTD) addresses exposure to adverse outcomes and is a fixture of cybersecurity reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Total Detection Time / Security Incidents; the result is stated in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The average time from the start of an incident or intrusion to its discovery - the first half of the security response equation, and statistically the more consequential one: the breach-cost research tradition has consistently found that the longer an intruder operates undetected, the deeper the access and the higher the eventual cost, which makes detection speed the strongest lever in the entire incident economics stack. Its strategic role is directional truth about security posture, since prevention metrics count attacks stopped while detection time measures what happens when prevention fails - and prevention always eventually fails. The relevant comparisons are by attack class: malware may be detected in minutes while credential-based intrusions run for months, so a healthy mean conceals the tail where the catastrophic cases live.

## Formula

```
MTTD = Total Detection Time / Security Incidents
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 319 (batch 1)
