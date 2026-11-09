# dea:metric-earnings-release-lag

Candidate Performance Metric record for **Earnings Release Lag** (ERL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-earnings-release-lag`
- **Name:** Earnings Release Lag
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ERL

## 2. Definition

Within Investor Relations & Capital Markets, Earnings Release Lag (ERL) is used to gauge how efficiently resources are converted into outputs. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Days from Period End to Earnings Release, expressed in days. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Listed companies.

## 3. Context

Measures days from period close to earnings release. It matters because release speed signals control maturity and affects market perception. Teams can shorten it by rushing estimates that later restate, trading speed for accuracy. Read with Restatement history and Earnings Surprise trends to confirm fast releases are also reliable ones.

## Formula

```
ERL = Days from Period End to Earnings Release
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investor_relations_capital_markets
- **Sector:** listed_companies

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 628 (batch 2)
