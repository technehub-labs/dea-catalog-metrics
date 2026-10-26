# dea:metric-daily-active-users-gaming

Candidate Performance Metric record for **Daily Active Users (Gaming)** (DAU-G) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-daily-active-users-gaming`
- **Name:** Daily Active Users (Gaming)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DAU-G

## 2. Definition

Daily Active Users (Gaming) (DAU-G) captures the engagement or satisfaction of the people involved for organizations tracking gaming. Its calculation is Unique Players Active per Day, measured in count (items per period). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Gaming practice.

## 3. Context

Unique players active per day - the engagement heartbeat of a live game, and the number the entire live-service model runs on: content cadence, monetization design, and operational investment are all sized against DAU, because the daily population is the audience every update and event monetizes. Its strategic significance is the habit reality of gaming: games that occupy a daily routine (the session-based loop) sustain monetization and content economics, while games played episodically behave more like premium products with a launch spike - and DAU trend reveals which product the studio actually has. The definitional honesty is platform breadth: cross-platform player de-duplication and account-merging conventions move the number materially in titles spanning console, PC, and mobile. Read with cohort and market splits: DAU blended across a soft-launched and a global region, or across an aging launch cohort and new acquisition, hides the direction of each, and it is the per-cohort DAU curve that predicts where the game is in its lifecycle.

## Formula

```
Unique Players Active per Day
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
- **Domain:** gaming
- **Sector:** gaming

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 702 (batch 2)
