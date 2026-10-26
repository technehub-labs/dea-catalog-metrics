# dea:metric-injury-burden-rate-deep-dive

Candidate Performance Metric record for **Injury Burden Rate (Deep Dive)** (IBR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-injury-burden-rate-deep-dive`
- **Name:** Injury Burden Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IBR-D

## 2. Definition

Within Sports Clubs & Leagues (Deep Dive), Injury Burden Rate (Deep Dive) (IBR-D) is used to gauge exposure to adverse outcomes. It is computed as Days Lost to Injury / Squad Player Days, expressed in percent (%). Its use is concentrated in Sports. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures injury incidence and days lost against player-exposure hours. It is the occupational-health metric of professional sport, and it is both a duty-of-care measure and an economics one: injury burden correlates with availability, wage waste, and performance. Standardize against exposure (training plus match minutes), or workload is invisible. Read with athlete availability rate (Deep Dive) and load-management compliance.

## Formula

```
IBR-D = Days Lost to Injury / Squad Player Days
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** sports_clubs_leagues_deep_dive
- **Sector:** sports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1998 (batch 6)
