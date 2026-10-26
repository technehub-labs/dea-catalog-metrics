# dea:metric-on-time-departure-rate-airport

Candidate Performance Metric record for **On-Time Departure Rate (Airport)** (OTDA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-departure-rate-airport`
- **Name:** On-Time Departure Rate (Airport)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** OTDA

## 2. Definition

Within Airport Operations, On-Time Departure Rate (Airport) (OTDA) is used to gauge the quality of outputs and outcomes. The formula is Flights Departing within Threshold / Scheduled Departures - reported in percent (%). It is a standard measure in the Airports sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

On-time departure rate measures flights pushing back within 15 minutes of schedule, and it is the punctuality baseline of airport operations - departures drive the day: a late departure becomes a late arrival feeding the next rotation, so departure discipline prevents the cascading delay that consumes airspace capacity. The airport-versus-airline attribution is the central measurement question: departure delay traces to airlines (turnaround, crew) and airports (gate availability, deicing, security flow) jointly, and the accountability metric separates airport-caused from airline-caused delay. Peak-hour scheduling saturation is the structural driver: airports scheduling beyond runway capacity guarantee delay regardless of operational quality. Read with departure-versus-arrival punctuality (the pair), airport-caused versus carrier-caused delay split, CDM (collaborative decision making) data quality, and peak-period demand versus declared capacity.

## Formula

```
Flights Departing within Threshold / Scheduled Departures
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations
- **Sector:** airports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1174 (batch 4)
