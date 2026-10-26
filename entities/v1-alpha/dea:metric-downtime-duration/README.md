# dea:metric-downtime-duration

Candidate Performance Metric record for **Downtime Duration** (DT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-downtime-duration`
- **Name:** Downtime Duration
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DT

## 2. Definition

Downtime Duration (DT) measures exposure to adverse outcomes in the IT Service Management domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Total Unplanned Unavailability per Period, measured in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The total time a service is unavailable in a period - the deconstructed form of availability that carries the information availability averages away. Its strategic value is the loss profile: frequency times duration, since a thousand short outages and one long outage can produce identical availability percentages with entirely different business meanings - transactional businesses suffer short outages painfully, while batch operations care only about total. Root-cause distribution is the actionable read: recurring downtime with the same cause is a maintenance or architecture failure, while distributed causes point to systemic fragility. The metric is also the settling metric for service credits in IT contracts, which makes its measurement definition (user-impacting versus infrastructure-affecting) a commercial matter, not just a technical one.

## Formula

```
Total Unplanned Unavailability per Period
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 312 (batch 1)
