# dea:metric-reserve-release-accuracy

Candidate Performance Metric record for **Reserve Release Accuracy** (RRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reserve-release-accuracy`
- **Name:** Reserve Release Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRA

## 2. Definition

Within Actuarial & Reserving, Reserve Release Accuracy (RRA) is used to gauge exposure to adverse outcomes. It is computed as Reserve Releases Justified by Experience / Total Releases, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Insurance.

## 3. Context

Measures how accurately deliberate reserve releases (or strengthening) matched subsequent emergence. Releases are the most scrutinized actuarial act in earnings management debates, and this metric makes them accountable rather than merely disclosed. Be alert to releases concentrated in loss-adequate quarters, and to asymmetric accuracy where releases prove wrong more often than strengthenings. Read with reserve development ratio and external auditor and regulator challenge history.

## Formula

```
RRA = Reserve Releases Justified by Experience / Total Releases
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** actuarial_reserving
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1539 (batch 6)
