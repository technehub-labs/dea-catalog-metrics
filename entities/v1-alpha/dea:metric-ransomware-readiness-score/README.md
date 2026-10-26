# dea:metric-ransomware-readiness-score

Candidate Performance Metric record for **Ransomware Readiness Score** (RRS-TI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ransomware-readiness-score`
- **Name:** Ransomware Readiness Score
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRS-TI

## 2. Definition

Ransomware Readiness Score (RRS-TI) measures exposure to adverse outcomes in the Threat Intelligence & Red Team domain. The formula is Composite Score across Tabletop, Recovery and Detection Tests - reported in score (points). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures composite readiness across backups, detection, response, and recovery against ransomware scenarios. Ransomware is the dominant business-continuity threat of the current era. Scores that don't test actual restore capability from isolated backups are incomplete. Read with backup restore success rate and tabletop exercise completion rate.

## Formula

```
Composite Score across Tabletop, Recovery and Detection Tests
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** threat_intelligence_red_team

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3300 (batch 7)
