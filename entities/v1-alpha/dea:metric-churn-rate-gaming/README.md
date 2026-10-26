# dea:metric-churn-rate-gaming

Candidate Performance Metric record for **Churn Rate (Gaming)** (CHR-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-churn-rate-gaming`
- **Name:** Churn Rate (Gaming)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CHR-G

## 2. Definition

Churn Rate (Gaming) (CHR-G) addresses exposure to adverse outcomes and is a fixture of gaming reporting. It is computed as Players Lost during Period / Players at Start, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Gaming.

## 3. Context

The share of the player base lost per period - the decay-rate metric of the live-game economy, and the complement of the retention checkpoints: where cohort checkpoints diagnose the acquisition experience, churn measures the ongoing operation - whether the live service holds the population it paid for. Its strategic significance is the content-flywheel coupling: live games lose players between content updates by design, so churn is managed against the content cadence - and measuring churn against the update calendar (post-patch spikes, inter-patch decay) is the live-ops diagnostic that separates controllable decay from structural decline. The honest read is by player-segment and tenure: churn of new players (acquisition-fit problem), churn of mid-progression players (content-velocity problem), and churn of endgame players (live-ops depth problem) are different failures, and the blended rate prescribes nothing. Read with reactivation: gaming churn is uniquely reversible, and returning-player programs mean the metric should always be paired with win-back data.

## Formula

```
Players Lost during Period / Players at Start
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 710 (batch 2)
