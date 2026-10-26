# dea:metric-voice-quality-mos-score

Candidate Performance Metric record for **Voice Quality MOS Score** (VQMS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-voice-quality-mos-score`
- **Name:** Voice Quality MOS Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VQMS

## 2. Definition

Voice Quality MOS Score (VQMS) addresses the quality of outputs and outcomes and is a fixture of network performance & capacity reporting. It is defined as Mean Opinion Score for Voice Sessions; the result is stated in score (points). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The Mean Opinion Score, standardized in ITU-T P.800, is the voice quality rating scale from 1 (bad) to 5 (excellent) originally gathered from human listening panels. Modern networks estimate MOS from network metrics (latency, jitter, loss, codec) via models like E-model because live panels are impractical. Above 4.0 is toll-quality; below 3.6 and users start abandoning calls. The catch: MOS estimates are codec- and model-sensitive, so compare only scores from the same measurement method, and always investigate the underlying jitter and loss rather than the score alone.

## Formula

```
Mean Opinion Score for Voice Sessions
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** ITU-T Recommendation P.800

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3345 (batch 7)
