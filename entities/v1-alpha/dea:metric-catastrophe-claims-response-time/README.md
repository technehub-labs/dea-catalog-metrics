# dea:metric-catastrophe-claims-response-time

Candidate Performance Metric record for **Catastrophe Claims Response Time** (CCRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-catastrophe-claims-response-time`
- **Name:** Catastrophe Claims Response Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CCRT

## 2. Definition

A Claims Operations (Insurance) indicator, Catastrophe Claims Response Time (CCRT) quantifies conformance to standards, plans, or obligations. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Days from Catastrophe Event to First Claim Payment - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Insurance sector.

## 3. Context

Catastrophe claims response time measures how quickly insurers reach policyholders after major events - storms, wildfires, floods - and it is the moment that defines insurer reputation for years: a fast, empathetic CAT response builds lifetime loyalty while a slow one generates regulatory complaints, media coverage, and mass non-renewal at the next policy term. The operational challenge is surge capacity: CAT events concentrate thousands of claims geographically and temporally, requiring pre-positioned adjusters, mobile claims technology, and advance-payment protocols. Response time must be measured against event magnitude - a hurricane demanding 50,000 claims deployments is a different problem than a localized hail event. Read with time-to-first-contact versus time-to-final-payment, advance-payment deployment speed, and complaint rates in affected regions post-event.

## Formula

```
Days from Catastrophe Event to First Claim Payment
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 856 (batch 3)
