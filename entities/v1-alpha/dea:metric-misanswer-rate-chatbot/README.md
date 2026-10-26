# dea:metric-misanswer-rate-chatbot

Candidate Performance Metric record for **Misanswer Rate (Chatbot)** (MAR-CB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-misanswer-rate-chatbot`
- **Name:** Misanswer Rate (Chatbot)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MAR-CB

## 2. Definition

Misanswer Rate (Chatbot) (MAR-CB) measures exposure to adverse outcomes in the Conversational AI & Chatbots domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Incorrect Answers on Sampled QA / Sampled Answers, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
MAR-CB = Incorrect Answers on Sampled QA / Sampled Answers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** conversational_ai_chatbots

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1488 (batch 5)
