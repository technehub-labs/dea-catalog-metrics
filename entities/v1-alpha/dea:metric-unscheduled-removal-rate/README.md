# dea:metric-unscheduled-removal-rate

Candidate Performance Metric record for **Unscheduled Removal Rate** (URR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-unscheduled-removal-rate`
- **Name:** Unscheduled Removal Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** URR

## 2. Definition

A Aviation Maintenance Repair & Overhaul indicator, Unscheduled Removal Rate (URR) quantifies exposure to adverse outcomes. It is defined as Unscheduled Component Removals / Flight Hours x 1,000; the result is stated in events per thousand or million (scaled). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Airlines & aviation, it is a recognized element of the standard performance toolkit.

## 3. Context

Unscheduled removal rate measures component removals not planned by the maintenance program - the surprise failures that interrupt schedules, consume parts, and trigger troubleshooting - and it is the fleet-reliability metric of condition-based maintenance economics. The metric matters because removals are expensive in three dimensions simultaneously: parts cost (often with repair-versus-replace judgment), logistics, and aircraft unavailability. The maintenance-industry practice of no-fault-found deserves attention: a substantial share of unscheduled removals test serviceable in the shop, meaning troubleshooting removed the wrong component, so removal rate has an accuracy dimension within it. Read with mean time between unscheduled removals by component, no-fault-found rate (the diagnostic quality signal), premature-removal trend (new components failing early signals quality issues in the supply chain), and condition-monitoring coverage.

## Formula

```
Unscheduled Component Removals / Flight Hours x 1,000
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1191 (batch 4)
