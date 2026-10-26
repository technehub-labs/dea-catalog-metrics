# dea:metric-revenue-per-consultant

Candidate Performance Metric record for **Revenue per Consultant** (RPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-per-consultant`
- **Name:** Revenue per Consultant
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RPC

## 2. Definition

Revenue per Consultant (RPC) captures how efficiently resources are converted into outputs for organizations tracking professional services. It is computed as Fee Revenue / Consultant FTEs, expressed in currency value. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Professional services.

## 3. Context

Total revenue divided by consulting headcount - the productivity metric of the professional-services model, and the single number that summarizes the machine: rate times utilization times leverage compress into it, so it captures the combined result of pricing discipline, billable efficiency, and pyramid structure. Its strategic significance is the scale-credibility test: firms claim growth ambitions that revenue per consultant quietly refutes, since a firm cannot grow revenue faster than headcount indefinitely without the underlying levers moving - and the metric is the honest check on whether growth was bought with people or with productivity. The honest read is mix-adjusted: service lines and geographies carry different natural revenue-per-head levels, and blended trends move with mix as much as with performance. Read with profit per consultant alongside: revenue per head rising while profit per head falls is the signature of pricing growth purchased with senior cost - the growth that does not compound.

## Formula

```
Fee Revenue / Consultant FTEs
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** professional_services
- **Sector:** professional_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 688 (batch 2)
