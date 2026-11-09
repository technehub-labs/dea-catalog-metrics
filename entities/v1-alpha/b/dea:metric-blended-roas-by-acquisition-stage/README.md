# dea:metric-blended-roas-by-acquisition-stage

Candidate Performance Metric record for **Blended ROAS by Acquisition Stage** (BRAS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-blended-roas-by-acquisition-stage`
- **Name:** Blended ROAS by Acquisition Stage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BRAS

## 2. Definition

Blended ROAS by Acquisition Stage (BRAS) addresses the economic value created or preserved and is a fixture of marketing & advertising standard measures (deep dive) reporting. The formula is Revenue / Spend across New versus Retention Activity - reported in ratio (x:1 or x). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures ROAS separated by funnel stage (awareness, consideration, conversion). Stage-blended views prevent upper-funnel investment from being judged by direct-response arithmetic. Stage attribution across long cycles is inherently modeled. Read with marketing mix model validation accuracy and return on advertising spend (Deep Dive).

## Formula

```
BRAS = Revenue / Spend across New versus Retention Activity
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** marketing_advertising_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4337 (batch 11)
