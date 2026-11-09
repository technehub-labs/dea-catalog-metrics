# dea:metric-levelized-cost-of-energy

Candidate Performance Metric record for **Levelized Cost of Energy** (LCOE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-levelized-cost-of-energy`
- **Name:** Levelized Cost of Energy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LCOE

## 2. Definition

Within Energy Transition & Renewables, Levelized Cost of Energy (LCOE) is used to gauge the economic value created or preserved. It is computed as Lifetime Costs / Lifetime Energy Produced, expressed in currency per unit. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Renewable energy.

## 3. Context

Levelized cost of energy (LCOE) is the discounted lifetime cost per unit of energy produced - the metric that enables comparison across generation technologies with completely different cost structures (fuel-heavy thermal, capital-heavy renewables), and it is the number that has driven the entire energy transition narrative: LCOE methodology has shown solar and onshore wind declining below new fossil generation in many markets. Its honesty depends on boundary discipline: which costs are included (transmission connection, curtailment risk, decommissioning, financing costs at what cost of capital?), and the cost-of-capital assumption alone can swing results materially, which is why LCOE comparisons across studies need methodology alignment. System-cost critique is the deeper issue: LCOE ignores intermittency's integration costs, which load-balancing and storage must absorb. Read with capacity factor (the production-side driver), cost-of-capital assumption disclosure, and system-level cost metrics that price firm delivery.

## Formula

```
LCOE = Lifetime Costs / Lifetime Energy Produced
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1101 (batch 4)
