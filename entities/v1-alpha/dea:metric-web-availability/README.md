# dea:metric-web-availability

Candidate Performance Metric record for **Web Availability** (WA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-web-availability`
- **Name:** Web Availability
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WA

## 2. Definition

Web Availability (WA) measures the quality of outputs and outcomes in the Digital Product & Web Operations domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Successful Requests or Uptime / Total Monitoring Window - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Web availability measures the share of time a web service is up and serving correctly, and it is the baseline reliability metric of digital operations - the 99.9 percent versus 99.99 percent thresholds translate to minutes and seconds of tolerable downtime per month, and consumer-facing brands treat outages as public failures with measurable revenue and reputation cost. The metric's sophistication is in what counts as available: a site that serves errors to 10 percent of users in one region while appearing green globally is effectively down for those users, so modern measurement is availability from the user's perspective (synthetic monitoring from real geographies, real-user monitoring of actual sessions), not server uptime. Read with error-rate and latency-percentile metrics (slow-but-up is degraded service), regional availability decomposition, and error-budget consumption which is the SRE framework for balancing reliability against release velocity.

## Formula

```
Successful Requests or Uptime / Total Monitoring Window
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** digital_product_web_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1076 (batch 4)
