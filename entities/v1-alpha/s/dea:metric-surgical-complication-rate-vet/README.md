# dea:metric-surgical-complication-rate-vet

Candidate Performance Metric record for **Surgical Complication Rate (Vet)** (SCR-V) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-surgical-complication-rate-vet`
- **Name:** Surgical Complication Rate (Vet)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCR-V

## 2. Definition

Surgical Complication Rate (Vet) (SCR-V) captures exposure to adverse outcomes for organizations tracking veterinary & animal health. It is computed as Complications / Surgical Procedures, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Healthcare.

## 3. Context

Measures adverse surgical outcomes against procedure volume, by procedure class. It is the core quality metric of veterinary medicine, where patients cannot report symptoms and complications surface late to owners. Case-mix adjustment is essential, since a referral hospital's rate is not comparable to a general practice's, and honest programs track death, infection, and dehiscence separately. Read with mortality within 30 days of procedure and anesthesia monitoring compliance.

## Formula

```
SCR-V = Complications / Surgical Procedures
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** veterinary_animal_health
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2032 (batch 6)
