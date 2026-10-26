# dea:metric-net-additions

Candidate Performance Metric record for **Net Additions** (NADD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-net-additions`
- **Name:** Net Additions
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NADD

## 2. Definition

Net Additions (NADD) addresses growth over time and is a fixture of telecommunications reporting. It is defined as New Subscribers - Lost Subscribers; the result is stated in count (items per period). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Telecommunications, it is a recognized element of the standard performance toolkit.

## 3. Context

Gross additions minus disconnects over a period - the growth metric of subscriber businesses, and the more honest form of headline growth because it nets the two-way traffic: an operator can post impressive gross adds while losing the base through churn, and net additions are where the truth shows. Its strategic significance is the composition read: net adds split by postpaid-versus-prepaid and by consumer-versus-enterprise carry completely different value (a postpaid net add is worth several prepaid ones), so the blended number is a summary and the split is the analysis. Read against market saturation: net adds in a mature market come from competitors, price aggressively, and churn back - while net adds in an under-penetrated market come from conversion and are far cheaper and stickier. Subscriber growth bought with device subsidies is growth on borrowed economics.

## Formula

```
New Subscribers - Lost Subscribers
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecommunications
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 530 (batch 1)
