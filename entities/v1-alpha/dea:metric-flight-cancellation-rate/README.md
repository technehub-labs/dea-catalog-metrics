# dea:metric-flight-cancellation-rate

Candidate Performance Metric record for **Flight Cancellation Rate** (FCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-flight-cancellation-rate`
- **Name:** Flight Cancellation Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FCR

## 2. Definition

A Airlines & Aviation indicator, Flight Cancellation Rate (FCR) quantifies exposure to adverse outcomes. Its calculation is Cancelled Flights / Scheduled Flights, measured in percent (%). It originates from and is most used in Airlines & aviation practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Cancelled flights as a share of scheduled flights - the disruption metric that passengers experience most bluntly, and strategically the one that sits closest to the airline's duty-of-care economics: cancellations trigger reaccommodation, compensation obligations under the passenger-rights regimes (the EU framework being the strictest), and crew-and-aircraft cascades that disrupt days of operation. Its significance is different from delay: a cancelled flight is a failure of the schedule, and unlike delay it transfers the passenger problem from operations to the commercial promise. The honest analysis separates cause: cancellations driven by weather and airspace are environmental exposure, cancellations driven by crew availability and maintenance planning are operational - and the controllable share is what management owns. Read with the completion-factor companion: carriers operating thin regional networks can show high cancellation rates concentrated at specific hubs, where the decision to cancel a marginal flight rather than delay it is an economics choice the metric records.

## Formula

```
Cancelled Flights / Scheduled Flights
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airlines_aviation
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 652 (batch 2)
