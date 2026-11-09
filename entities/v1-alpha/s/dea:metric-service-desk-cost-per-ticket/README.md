# dea:metric-service-desk-cost-per-ticket

Candidate Performance Metric record for **Service Desk Cost per Ticket** (SDCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-desk-cost-per-ticket`
- **Name:** Service Desk Cost per Ticket
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SDCT

## 2. Definition

Service Desk Cost per Ticket (SDCT) addresses how efficiently resources are converted into outputs and is a fixture of it service management reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Service Desk Cost / Tickets Handled, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
SDCT = Service Desk Cost / Tickets Handled
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 308 (batch 1)
