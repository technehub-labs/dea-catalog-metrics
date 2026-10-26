# dea:metric-daily-active-users-deep-dive

Candidate Performance Metric record for **Daily Active Users (Deep Dive)** (DAU-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-daily-active-users-deep-dive`
- **Name:** Daily Active Users (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DAU-D

## 2. Definition

A Gaming Development & Live Operations indicator, Daily Active Users (Deep Dive) (DAU-D) quantifies the engagement or satisfaction of the people involved. It is computed as Unique Active Players per Day, expressed in count (items per period). Its use is concentrated in Gaming. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of a game's player base active daily. DAU is the heartbeat of live-service gaming: monetization systems are tuned to engagement, and DAU trends precede revenue trends by weeks or months. Definition integrity matters - active means meaningful session, not login - and platform mix (mobile versus console) shifts baselines. Read with DAU-to-MAU stickiness (Deep Dive) and D1 / D7 / D30 retention (Deep Dive).

## Formula

```
Unique Active Players per Day
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** gaming_development_live_operations
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1980 (batch 6)
