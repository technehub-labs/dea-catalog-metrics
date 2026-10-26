# dea:metric-ibnr-accuracy-ratio

Candidate Performance Metric record for **IBNR Accuracy Ratio** (IBNR-AR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ibnr-accuracy-ratio`
- **Name:** IBNR Accuracy Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IBNR-AR

## 2. Definition

IBNR Accuracy Ratio (IBNR-AR) captures the quality of outputs and outcomes for organizations tracking actuarial & reserving. The formula is Actual IBNR / Estimated IBNR - reported in ratio (x:1 or x). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It is a standard measure in the Insurance sector.

## 3. Context

Measures how accurately incurred-but-not-reported reserves were estimated against subsequently emerged losses. IBNR is the most judgment-heavy and manipulable reserve component, and its accuracy is a proxy for actuarial and data quality together. Assess by line and maturity vintage, since late-reporting lines and young books carry structural noise. Read with reserve development ratio and loss trend estimation error for systematic bias.

## Formula

```
Actual IBNR / Estimated IBNR
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1526 (batch 6)
