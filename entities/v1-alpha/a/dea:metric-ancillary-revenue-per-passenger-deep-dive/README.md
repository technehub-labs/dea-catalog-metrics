# dea:metric-ancillary-revenue-per-passenger-deep-dive

Candidate Performance Metric record for **Ancillary Revenue per Passenger (Deep Dive)** (ARPP-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ancillary-revenue-per-passenger-deep-dive`
- **Name:** Ancillary Revenue per Passenger (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ARPP-D

## 2. Definition

Ancillary Revenue per Passenger (Deep Dive) (ARPP-D) measures the economic value created or preserved in the Airline Operations (Deep Dive) domain. Its calculation is Ancillary Revenue / Passengers, measured in currency per unit. It originates from and is most used in Airlines practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures non-ticket revenue (bags, seats, onboard sales, loyalty) per passenger. Ancillaries transformed airline economics - they monetize willingness-to-pay heterogeneity that fares cannot - and their trajectory and mix reveal both strategy maturity and customer-tolerance limits. Ancillary growth that degrades experience eventually reads in satisfaction and repeat purchase. Read with NPS and fare-versus-ancillary price positioning.

## Formula

```
ARPP-D = Ancillary Revenue / Passengers
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2266 (batch 6)
