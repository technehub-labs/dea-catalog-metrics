# dea:metric-claim-settlement-ratio

Candidate Performance Metric record for **Claim Settlement Ratio** (CSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-claim-settlement-ratio`
- **Name:** Claim Settlement Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CSR

## 2. Definition

Claim Settlement Ratio (CSR) addresses the quality of outputs and outcomes and is a fixture of insurance reporting. It is defined as Claims Settled / Claims Received; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Insurance, it is a recognized element of the standard performance toolkit.

## 3. Context

Claims settled against claims received - the insurance industry's headline service-quality number, and in many markets the one regulators publish and consumers quote. Its strategic weight is trust economics: insurance is a promise, and this ratio is the observed probability the promise is kept, which drives renewal, referral, and brand in a way marketing spend cannot. The caution is the definitional wedge: what counts as settled, over what window, and how repudiated versus withdrawn claims are treated all move the number materially. A very high ratio can mean excellent service or under-reserving and rubber-stamp approval; a middling ratio with strong justification discipline is often the healthier book.

## Formula

```
Claims Settled / Claims Received
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 61 (batch 1)
