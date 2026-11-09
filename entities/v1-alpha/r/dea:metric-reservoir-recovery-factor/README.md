# dea:metric-reservoir-recovery-factor

Candidate Performance Metric record for **Reservoir Recovery Factor** (RRF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reservoir-recovery-factor`
- **Name:** Reservoir Recovery Factor
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRF

## 2. Definition

Reservoir Recovery Factor (RRF) addresses how efficiently resources are converted into outputs and is a fixture of oil & gas reporting. Its calculation is Hydrocarbons Recovered / Hydrocarbons in Place, measured in percent (%). It originates from and is most used in Oil & gas practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Reservoir recovery factor measures the share of original oil in place ultimately recoverable, and it is the petroleum engineer's defining number - the difference between a 25 percent and 35 percent recovery factor on a billion-barrel field is a hundred million barrels of reserve, which is why enhanced oil recovery techniques command so much attention. The factor is a projection as much as a measurement: it depends on the geological model, drive mechanism, and technology assumptions, all of which carry uncertainty. It is also economically conditioned - the recovery factor rises when prices justify more aggressive extraction, so it is a function of economics as well as physics. Read with reserve estimates audit quality, decline curve assumptions, and recovery-improvement project economics.

## Formula

```
RRF = Hydrocarbons Recovered / Hydrocarbons in Place
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** oil_gas
- **Sector:** oil_gas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 880 (batch 3)
