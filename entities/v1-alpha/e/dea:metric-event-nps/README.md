# dea:metric-event-nps

Candidate Performance Metric record for **Event NPS** (NPS-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-event-nps`
- **Name:** Event NPS
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NPS-E

## 2. Definition

A Sports & Events indicator, Event NPS (NPS-E) quantifies the engagement or satisfaction of the people involved. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is % Promoters - % Detractors among Event Attendees - reported in score (points). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Sports & events sector.

## 3. Context

Event NPS measures net promoter score for a specific event - would attendees recommend this experience - and it is the forward-looking satisfaction metric that captures what satisfaction scores miss: the advocacy intention that predicts future attendance, word-of-mouth growth, and sponsor value perception. The event-specific measurement has an advantage over brand-level NPS: the experience is recent and bounded, so responses are concrete rather than brand-image impressions. The structural insight from NPS methodology applies with full force: detractors drag more than promoters lift (the asymmetric scoring), so a small share of serious problems can dominate the score. Read with NPS by audience segment (attendees versus suites versus staff), specific-experience drivers (entry process, restroom lines, exit flow), repeat-attendance correlation by score band, and open-text theme analysis for root causes.

## Formula

```
NPS-E = % Promoters - % Detractors among Event Attendees
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** sports_events
- **Sector:** sports_events

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 951 (batch 3)
