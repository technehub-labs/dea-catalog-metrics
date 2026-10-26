# dea:metric-transmission-losses

Candidate Performance Metric record for **Transmission Losses** (TL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-transmission-losses`
- **Name:** Transmission Losses
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TL

## 2. Definition

Transmission Losses (TL) measures how efficiently resources are converted into outputs in the Energy & Utilities domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is (Energy Sent - Energy Billed) / Energy Sent, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Energy & utilities practice.

## 3. Context

The energy lost between generation and delivery - the share of power injected into the transmission grid that dissipates in conductors and transformers before reaching the distribution boundary. Its strategic significance is scale: transmission losses across a large grid run to percentage points of total generation, which is generation that must be produced, paid for, and emitted without ever serving a customer - so loss-reduction programs (conductor upgrades, voltage optimization, reactive power compensation) are among the highest-certainty efficiency investments available. Read with the loss-structure decomposition: technical losses follow physical law and vary with loading squared, while commercial losses (theft, metering gaps, billing failure) concentrate in specific areas and demand a different, more enforcement-shaped response. The honest trend separates the two before crediting the network for a loss reduction that was actually a collections campaign.

## Formula

```
(Energy Sent - Energy Billed) / Energy Sent
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 442 (batch 1)
