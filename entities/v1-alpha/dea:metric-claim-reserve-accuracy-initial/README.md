# dea:metric-claim-reserve-accuracy-initial

Candidate Performance Metric record for **Claim Reserve Accuracy (Initial)** (CRAI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claim-reserve-accuracy-initial`
- **Name:** Claim Reserve Accuracy (Initial)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRAI

## 2. Definition

Within Insurance Claims Deep Dive, Claim Reserve Accuracy (Initial) (CRAI) is used to gauge the quality of outputs and outcomes. It is computed as Ultimate Claim Cost / Initial Reserve, expressed in ratio (x:1 or x). Its use is concentrated in Insurance. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Values outside the intended band, on either side, warrant investigation.

## Formula

```
CRAI = Ultimate Claim Cost / Initial Reserve
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_claims_deep_dive
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1549 (batch 6)
