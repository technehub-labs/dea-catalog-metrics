# dea:metric-digital-insurance-cost-per-policy

Candidate Performance Metric record for **Digital Insurance Cost per Policy** (DICPP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-digital-insurance-cost-per-policy`
- **Name:** Digital Insurance Cost per Policy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DICPP

## 2. Definition

Digital Insurance Cost per Policy (DICPP) addresses how efficiently resources are converted into outputs and is a fixture of insurance distribution - direct & digital reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Digital Channel Cost / Policies, expressed in currency value. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Insurance.

## 3. Context

Measures fully loaded cost of issuing and servicing a digital-channel policy. It is the efficiency scorecard of digital underwriting economics, and its trajectory determines whether direct distribution beats intermediated alternatives at scale. Allocation of shared platform costs is the honesty battleground, since unallocated platform spend flatters the number. Read with digital policy issuance rate and lifetime value per policy against it.

## Formula

```
DICPP = Digital Channel Cost / Policies
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_direct_digital
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2211 (batch 6)
