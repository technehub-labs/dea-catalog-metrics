# dea:metric-r-d-intensity

Candidate Performance Metric record for **R&D Intensity** (RDI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-r-d-intensity`
- **Name:** R&D Intensity
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RDI

## 2. Definition

R&D Intensity (RDI) captures capability maturity or development for organizations tracking r&d and innovation. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is R&D Expenditure / Revenue - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Research and development expenditure as a share of revenue - the canonical innovation-input metric, whose strategic significance is the industry-structure arithmetic it encodes: software can innovate below 15 percent, pharma runs above 20, and aerospace and automotive sit between, so the number is meaningful only against sector norms - the persistent cross-sector comparison error this metric invites. Its interpretive weight is commitment signaling: R&D is discretionary spending that competitors cannot quickly replicate, and the intensity trend through a downturn is the classic separating signal - organizations that hold R&D through the cycle emerge with the next product cycle, those that cut it harvest their future. Read with the output companion (innovation revenue share, patent productivity, pipeline value): intensity is the input, and inputs without outputs is cost without strategy, which is why intensity alone has never been a sufficient innovation metric.

## Formula

```
R&D Expenditure / Revenue
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** r_d_and_innovation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 536 (batch 1)
