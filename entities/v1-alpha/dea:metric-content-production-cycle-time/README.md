# dea:metric-content-production-cycle-time

Candidate Performance Metric record for **Content Production Cycle Time** (CPCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-content-production-cycle-time`
- **Name:** Content Production Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CPCT

## 2. Definition

Content Production Cycle Time (CPCT) captures how efficiently resources are converted into outputs for organizations tracking media & entertainment. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Days from Greenlight to Release - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Media & entertainment sector.

## 3. Context

Elapsed time from greenlight to release - the velocity metric of content businesses, and strategically the one that connects creative decisions to capital efficiency: production capital is tied up from first spend to first revenue, and cycle-time compression releases it faster across the slate, which is why studios and platforms measure it by content type. Its significance is the window economics: release dates are strategic (awards windows, seasonality, platform-event coordination), and cycle-time overruns consume the flexibility that scheduling strategy depends on. The honest read is by content class: scripted series, unscripted formats, film, and live events have structurally different cycle physics (scripted pipeline is years, unscripted can be months), and the actionable analysis is within class. Read with the parallel-production dimension: the real capacity question is how many productions run simultaneously per executive producer and development team, since sequential cycle time is not the constraint - throughput is.

## Formula

```
CPCT = Days from Greenlight to Release
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** media_entertainment
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 699 (batch 2)
