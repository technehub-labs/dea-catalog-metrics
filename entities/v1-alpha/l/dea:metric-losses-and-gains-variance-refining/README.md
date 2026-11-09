# dea:metric-losses-and-gains-variance-refining

Candidate Performance Metric record for **Losses and Gains Variance (Refining)** (LGV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-losses-and-gains-variance-refining`
- **Name:** Losses and Gains Variance (Refining)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LGV

## 2. Definition

Losses and Gains Variance (Refining) (LGV) measures the quality of outputs and outcomes in the Oil & Gas Downstream & Refining domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Measured Output vs Theoretical Output Variance, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Its use is concentrated in Oil & Gas.

## Formula

```
LGV = Measured Output vs Theoretical Output Variance
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** oil_gas_downstream_refining
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2303 (batch 6)
