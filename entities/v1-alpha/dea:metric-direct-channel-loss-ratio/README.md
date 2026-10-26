# dea:metric-direct-channel-loss-ratio

Candidate Performance Metric record for **Direct Channel Loss Ratio** (DCLR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-direct-channel-loss-ratio`
- **Name:** Direct Channel Loss Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCLR

## 2. Definition

Direct Channel Loss Ratio (DCLR) addresses exposure to adverse outcomes and is a fixture of insurance distribution - direct & digital reporting. It is computed as Direct Channel Claims / Direct Premium, expressed in percent (%). Its use is concentrated in Insurance. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures loss ratio of policies originated through direct digital channels. Channel economics is the strategic question of digital insurance: direct channels save acquisition cost but attract different risk selection (adverse selection through self-selection), and the loss ratio reveals which effect dominates. Cohort by tenure and product, since digital-channel books are young and loss ratios develop. Read with digital policy issuance rate and underwriting model validation for that channel.

## Formula

```
DCLR = Direct Channel Claims / Direct Premium
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_direct_digital
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2210 (batch 6)
