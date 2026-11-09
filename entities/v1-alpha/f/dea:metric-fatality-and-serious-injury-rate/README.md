# dea:metric-fatality-and-serious-injury-rate

Candidate Performance Metric record for **Fatality and Serious Injury Rate** (FSIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fatality-and-serious-injury-rate`
- **Name:** Fatality and Serious Injury Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FSIR

## 2. Definition

Within Mining & Metals, Fatality and Serious Injury Rate (FSIR) is used to gauge exposure to adverse outcomes. It is computed as Serious Injuries and Fatalities / Hours Worked x 1,000,000, expressed in events per thousand or million (scaled). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Mining & metals.

## 3. Context

Fatality and serious injury rates (FSIR) count deaths and life-altering injuries per hours worked, and in mining they are the non-negotiable floor of the social license to operate. Beyond ethics, one fatality can halt an operation, invite regulatory intervention, and erase a year of productivity gains, so leading indicators matter more than lagging counts. Beware underreporting incentives: injury classification is vulnerable to pressure, which is why serious-injury definitions must be externally auditable. Pair with high-potential incident counts, ground-control failures, and near-miss reporting rates, which move first and predict FSIR direction.

## Formula

```
FSIR = Serious Injuries and Fatalities / Hours Worked x 1,000,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** mining_metals
- **Sector:** mining_metals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 720 (batch 2)
