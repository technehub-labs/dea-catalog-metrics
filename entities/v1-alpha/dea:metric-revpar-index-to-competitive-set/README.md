# dea:metric-revpar-index-to-competitive-set

Candidate Performance Metric record for **RevPAR Index to Competitive Set** (RPI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revpar-index-to-competitive-set`
- **Name:** RevPAR Index to Competitive Set
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RPI

## 2. Definition

A Hotel & Resort Operations (Deep Dive) indicator, RevPAR Index to Competitive Set (RPI) quantifies how effectively a process or entity achieves its intended outcome. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Hotel RevPAR / Compset RevPAR; the result is stated in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. In Hospitality, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures revenue per available room performance relative to a defined competitive set, indexed to 100. It is the market-share metric of hotels, since absolute RevPAR moves with the market while the index reveals whether the property is winning or losing. Competitive set definition is the honest-read battleground: an easy comp set flatters the index. Read with guest satisfaction index (Deep Dive) and rate positioning data.

## Formula

```
RPI = Hotel RevPAR / Compset RevPAR
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** hotel_resort_operations_deep_dive
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1897 (batch 6)
