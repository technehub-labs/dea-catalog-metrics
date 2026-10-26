# dea:metric-exit-plan-coverage

Candidate Performance Metric record for **Exit Plan Coverage** (EPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-exit-plan-coverage`
- **Name:** Exit Plan Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EPC

## 2. Definition

Exit Plan Coverage (EPC) measures exposure to adverse outcomes in the Outsourcing & Vendor Management domain. Its calculation is Contracts with Tested Exit or Step-In Plan / Critical Contracts, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Exit plan coverage measures the share of vendor relationships (usually critical ones) with documented, tested exit or contingency plans - and it is the negotiating-power and continuity metric of vendor management: the relationship's balance of power is set by the credibility of the exit option, not by the contract's terms alone. The measurement honesty problem is plan quality: a documented exit plan and a tested exit plan are different things - real exit readiness means data portability verified, transition cost estimated, alternative supply mapped, and the plan exercised at least through tabletop simulation. The strategic trade-off is investment: exit planning for every vendor is wasted effort, so tiering by criticality and concentration (from the concentration metric) targets the planning where failure would hurt. Read with data-portability verification status, alternative-supplier qualification progress, and the exit-cost estimate as the negotiating asymmetry measure.

## Formula

```
Contracts with Tested Exit or Step-In Plan / Critical Contracts
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** outsourcing_vendor_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1133 (batch 4)
