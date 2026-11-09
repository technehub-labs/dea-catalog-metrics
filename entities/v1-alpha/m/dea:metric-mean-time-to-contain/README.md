# dea:metric-mean-time-to-contain

Candidate Performance Metric record for **Mean Time to Contain** (MTTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-contain`
- **Name:** Mean Time to Contain
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTTC

## 2. Definition

Mean Time to Contain (MTTC) measures exposure to adverse outcomes in the Cybersecurity domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Total Containment Time / Security Incidents - reported in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The average time from detection of a security incident to its containment - the second half of the response equation, measuring how fast the organization stops the bleeding once it knows it is bleeding. Containment is where incident cost is actually determined: the damage done before detection is sunk, and the damage done after detection is a function of this metric, which is why incident response maturity models all grade against it. Strategic use is the mean-plus-tail read: averages are dragged by routine malware events, while the scenario that matters - a sophisticated intruder in the crown-jewel systems - must be rehearsed through exercises, since its real containment time is unknowable until it happens. The metric also prices the automation question: containment that depends on paging a human is bounded below by human latency, which is the argument for automated response.

## Formula

```
MTTC = Total Containment Time / Security Incidents
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 320 (batch 1)
