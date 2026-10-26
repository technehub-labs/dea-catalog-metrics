# dea:metric-fundraising-efficiency

Candidate Performance Metric record for **Fundraising Efficiency** (FE-N) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fundraising-efficiency`
- **Name:** Fundraising Efficiency
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FE-N

## 2. Definition

Fundraising Efficiency (FE-N) measures how efficiently resources are converted into outputs in the Nonprofit & NGO domain. Its calculation is Funds Raised / Fundraising Costs, measured in ratio (x:1 or x). It originates from and is most used in Nonprofit & NGO practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Fundraising efficiency measures funds raised per unit of fundraising effort or cost, and it is the revenue-engine metric of nonprofit sustainability - organizations exist to deliver programs, but only exist at all if fundraising pays for itself. The metric's strategic texture is the donor-segment efficiency gradient: major-gift fundraising is expensive per ask but yields enormous returns per dollar raised, while direct-response fundraising operates at thin efficiency but scales, so blended efficiency is really a mix statement. The measurement honesty issue is lifetime versus first-gift: a channel that loses money on acquisition and profits on renewal looks inefficient in year one. Read with donor lifetime value by acquisition channel, retention by source, and the raising-versus-program balance - efficiency that suppresses program quality is not efficiency.

## Formula

```
FE-N = Funds Raised / Fundraising Costs
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** organization
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** nonprofit_ngo
- **Sector:** nonprofit_ngo

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1165 (batch 4)
