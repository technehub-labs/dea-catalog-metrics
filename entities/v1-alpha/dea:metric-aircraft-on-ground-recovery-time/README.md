# dea:metric-aircraft-on-ground-recovery-time

Candidate Performance Metric record for **Aircraft on Ground Recovery Time** (AOGRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-aircraft-on-ground-recovery-time`
- **Name:** Aircraft on Ground Recovery Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AOGRT

## 2. Definition

Aircraft on Ground Recovery Time (AOGRT) addresses how efficiently resources are converted into outputs and is a fixture of aviation maintenance repair & overhaul reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Hours from AOG Event to Release to Service, expressed in hours. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Airlines & aviation.

## 3. Context

Aircraft on ground recovery time measures how quickly an unserviceable aircraft returns to service, and it is the disruption-cost metric of aviation maintenance - an AOG aircraft generates no revenue while costing ownership capital, crew, and schedule disruption, with the hourly exposure running into the tens of thousands of dollars for widebody fleets. AOG recovery decomposes into diagnosis speed, parts logistics (AOG parts shipping is a premium-priced industry of its own), and technician dispatch - and the recovery-time distribution is heavy-tailed, so mean recovery time understates the risk of the bad cases. The strategic lever is parts positioning: pre-positioning critical components by fleet base trades inventory cost against AOG exposure. Read with AOG frequency by fleet type, parts-availability rate (the leading driver), remote-diagnostic resolution rate, and contractual MRO response-time performance.

## Formula

```
Hours from AOG Event to Release to Service
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** aviation_maintenance_repair_overhaul
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1184 (batch 4)
