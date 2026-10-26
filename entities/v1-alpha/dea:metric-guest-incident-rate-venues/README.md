# dea:metric-guest-incident-rate-venues

Candidate Performance Metric record for **Guest Incident Rate (Venues)** (GIR-V) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-guest-incident-rate-venues`
- **Name:** Guest Incident Rate (Venues)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GIR-V

## 2. Definition

Within Entertainment Venues & Attractions, Guest Incident Rate (Venues) (GIR-V) is used to gauge exposure to adverse outcomes. The formula is Reportable Guest Incidents / Attendance - reported in events per thousand or million (scaled). It is a standard measure in the Media & Entertainment sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures guest injuries and safety incidents against attendance. Venues are experience businesses whose brand value collapses with safety failures, so this metric is both duty-of-care and reputational. Normalize by guest-hours and segment by incident type and location, since crowds, rides, and concourses have different risk profiles. Read with near-miss reporting and crowd-management compliance.

## Formula

```
Reportable Guest Incidents / Attendance
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** entertainment_venues_attractions
- **Sector:** media_entertainment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1950 (batch 6)
