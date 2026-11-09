# dea:metric-attendance-rate-venue-capacity

Candidate Performance Metric record for **Attendance Rate (Venue Capacity)** (ARVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-attendance-rate-venue-capacity`
- **Name:** Attendance Rate (Venue Capacity)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ARVC

## 2. Definition

Attendance Rate (Venue Capacity) (ARVC) measures the utilization or availability of capacity in the Sports & Events domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Attendees / Venue Capacity - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Sports & events sector.

## 3. Context

Attendance rate measures filled seats against venue capacity, and it is the live-events metric that drives everything else - concessions, merchandise, parking, and atmosphere all scale with butts in seats, while the fixed costs of opening (staffing, security, utilities) are largely invariant. The nuance is distributed versus papered attendance: free ticketing to fill venues inflates attendance while destroying pricing power and season-ticket value, so the honest measure counts paid attendance separately. Sport-specific dynamics matter: attendance correlates with team performance with elasticity that varies by market loyalty and by win-streak timing. Read with paid versus comp ratio, no-show rate among ticketed fans (turnstile counts versus sold), and attendance trend by day-of-week and opponent tier.

## Formula

```
ARVC = Attendees / Venue Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 946 (batch 3)
