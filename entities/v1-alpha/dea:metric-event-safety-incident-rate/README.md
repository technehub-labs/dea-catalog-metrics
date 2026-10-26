# dea:metric-event-safety-incident-rate

Candidate Performance Metric record for **Event Safety Incident Rate** (ESIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-event-safety-incident-rate`
- **Name:** Event Safety Incident Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ESIR

## 2. Definition

Within Sports & Events, Event Safety Incident Rate (ESIR) is used to gauge exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Safety Incidents / Attendees x 1,000, expressed in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Sports & events.

## 3. Context

Event safety incident rate measures injuries, security events, and medical responses per attendee or per event, and in live entertainment it is the metric whose failure mode is catastrophic and public - crowd crushes and structural failures have shaped the industry's regulatory environment (event licensing, crowd management plans). The measurement needs severity weighting: medical transports and arrests are different risk classes than minor first-aid visits, and alcohol-related incidents follow distinct patterns tied to service cutoff policies. The operational leading indicators are crowd-density monitoring (real-time sensor and video analytics), entry-flow management, and weather protocol adherence. Read with incident severity distribution, near-miss reporting, crowd-density peak readings versus thresholds, and evacuation drill performance.

## Formula

```
Safety Incidents / Attendees x 1,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** sports_events
- **Sector:** sports_events

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 954 (batch 3)
