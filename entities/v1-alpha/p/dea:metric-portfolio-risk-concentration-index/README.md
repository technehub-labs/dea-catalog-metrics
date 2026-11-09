# dea:metric-portfolio-risk-concentration-index

Candidate Performance Metric record for **Portfolio Risk Concentration Index** (PRCI-PPM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-risk-concentration-index`
- **Name:** Portfolio Risk Concentration Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PRCI-PPM

## 2. Definition

Portfolio Risk Concentration Index (PRCI-PPM) measures exposure to adverse outcomes in the Program & Portfolio Management domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Concentration of Investment in Single Risk Classes, expressed in index (0-100 or normalized). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures whether portfolio risk is spread across initiatives, technologies, and vendors or concentrated in a few. Concentration turns single failures into portfolio-level shocks. Concentration in one vendor is often invisible until contract renewal. Read with risk exposure trend index and program interdependency health.

## Formula

```
PRCI-PPM = Concentration of Investment in Single Risk Classes
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** program_portfolio_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2964 (batch 7)
