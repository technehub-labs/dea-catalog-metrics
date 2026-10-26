# dea:metric-retail-revenue-per-passenger

Candidate Performance Metric record for **Retail Revenue per Passenger** (RRPP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-retail-revenue-per-passenger`
- **Name:** Retail Revenue per Passenger
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RRPP

## 2. Definition

Retail Revenue per Passenger (RRPP) addresses the economic value created or preserved and is a fixture of airport operations reporting. It is computed as Concession and Duty-Free Revenue / Passengers, expressed in currency per unit. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Airports.

## 3. Context

Retail revenue per passenger measures non-aeronautical commercial spend per enplaned passenger, and it is the margin-mix metric of the airport business model - aeronautical charges are regulated and capped while concessions are market-priced, so the profitable airport is one that monetizes dwell time. The metric decomposes into passenger mix (international passengers spend multiples of domestic in duty-free), dwell time (longer waits, paradoxically, can raise spend), and concession-mix quality (curated local concepts outperform generic chains in both rent and satisfaction). Spend per passenger is deliberately managed: the tension between smooth-flow operations (short dwell) and commercial revenue is real and resolved through terminal design. Read with spend per passenger by nationality and dwell time, concession revenue per square meter, and satisfaction impact of commercial layout.

## Formula

```
Concession and Duty-Free Revenue / Passengers
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1181 (batch 4)
