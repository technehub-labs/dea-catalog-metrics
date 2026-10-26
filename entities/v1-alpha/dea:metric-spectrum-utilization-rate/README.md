# dea:metric-spectrum-utilization-rate

Candidate Performance Metric record for **Spectrum Utilization Rate** (SUR-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-spectrum-utilization-rate`
- **Name:** Spectrum Utilization Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SUR-T

## 2. Definition

Within Telecom Network Operations (Deep Dive), Spectrum Utilization Rate (SUR-T) is used to gauge the utilization or availability of capacity. Its calculation is Used Capacity / Licensed Spectrum Capacity, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It originates from and is most used in Telecommunications practice.

## 3. Context

Measures the efficiency of licensed spectrum use - traffic carried per unit of spectrum and time. Spectrum is the scarce, auction-priced input of mobile economics, and utilization discipline determines whether operators extract value from licenses or strand capital. Utilization must be read by band and geography, since low-band coverage layers run sparse by design. Read with capacity headroom forecasts and spectrum renewal or auction positioning.

## Formula

```
Used Capacity / Licensed Spectrum Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2135 (batch 6)
