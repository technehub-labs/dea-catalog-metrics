# dea:metric-policy-renewal-rate

Candidate Performance Metric record for **Policy Renewal Rate** (PoRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-policy-renewal-rate`
- **Name:** Policy Renewal Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PoRR

## 2. Definition

Policy Renewal Rate (PoRR) addresses the retention of customers, users, or assets over time and is a fixture of insurance reporting. It is computed as Policies Renewed / Policies Due for Renewal, expressed in percent (%). Its use is concentrated in Insurance. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of expiring insurance policies that are renewed. It matters because retention is the dominant driver of lifetime profitability in insurance, where acquisition costs are front-loaded. Teams can prop it up with unsustainable discounting at renewal, buying volume at the cost of underwriting margin. Read with Loss Ratio and Customer Retention Rate to confirm renewals are profitable rather than merely retained.

## Formula

```
Policies Renewed / Policies Due for Renewal
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 63 (batch 1)
