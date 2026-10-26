# dea:metric-non-functional-requirement-coverage

Candidate Performance Metric record for **Non-Functional Requirement Coverage** (NFRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-non-functional-requirement-coverage`
- **Name:** Non-Functional Requirement Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NFRC

## 2. Definition

Within Requirements Engineering & Product Discovery, Non-Functional Requirement Coverage (NFRC) is used to gauge the quality of outputs and outcomes. It is computed as NFR Categories Addressed per Release / Applicable NFRs, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how thoroughly performance, security, scalability, and reliability requirements are specified and tested. Non-functional failures are the outages and breaches that functional testing cannot catch, and coverage gaps surface at the worst moments - peak load and attack. Coverage must include test evidence, since specified-but-untested NFRs are documentation of intent, not capability. Read with service scalability headroom (Deep Dive) and production incident root-cause analysis of NFR gaps.

## Formula

```
NFR Categories Addressed per Release / Applicable NFRs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** requirements_engineering_product_discovery

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2619 (batch 7)
