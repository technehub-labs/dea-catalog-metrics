# dea:metric-mean-opinion-score

Candidate Performance Metric record for **Mean Opinion Score** (MOS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-opinion-score`
- **Name:** Mean Opinion Score
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MOS

## 2. Definition

Mean Opinion Score (MOS) captures the quality of outputs and outcomes for organizations tracking telecommunications. Its calculation is Average Subjective Voice or Video Quality Rating, measured in score (points). It originates from and is most used in Telecommunications practice. Its value drives prioritization and resource reallocation among competing initiatives. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the average human-rated quality of voice or video transmissions on a five-point scale. It matters because it captures actual perceived quality that network counters cannot. Sampling easy call types or favorable codecs can flatter the average. Read with Call Drop Rate and Latency/Jitter metrics to align perceived quality with engineered quality.

## Formula

```
Average Subjective Voice or Video Quality Rating
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecommunications
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 529 (batch 1)
